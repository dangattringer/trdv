import asyncio
import logging
import re
from datetime import datetime, timezone

import polars as pl


from .collector import TradingViewDataCollector
from .enums import Interval, MessageType
from .exceptions import TrdvException
from .models.symbol import Symbol
from .session import Session
from .utils import generate_session_id
from .websocket import WebSocketClient

logger = logging.getLogger(__name__)


class TradingViewClient:
    """
    Asynchronous client to interact with the TradingView WebSocket API
    for fetching historical market data.
    """

    _DEFAULT_TIMEOUT = 10.0
    _GUEST_AUTH_TOKEN = "unauthorized_user_token"
    _CHART_SESSION_PREFIX = "cs"
    _SERIES_ID_PREFIX = "sds"
    _INTERNAL_SYMBOL_ID = "symbol_1"
    _INTERNAL_SERIES_NAME = "s1"

    def __init__(self, session: Session | None = None):
        self._session = session or Session()
        self._ws: WebSocketClient | None = None
        self._chart_session_id: str | None = None
        self._active_collectors: dict[str, TradingViewDataCollector] = {}

    async def __aenter__(self):
        """Initializes the WebSocket connection and performs the handshake."""
        self._ws = WebSocketClient(self._session)
        await self._ws.__aenter__()
        await self._handshake()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Closes the WebSocket connection."""
        if self._ws:
            await self._ws.__aexit__(exc_type, exc_val, exc_tb)

    async def _handshake(self):
        """Performs the initial authentication and session creation handshake."""
        logger.info("Performing WebSocket handshake...")
        auth_token = self._GUEST_AUTH_TOKEN
        if self._session.is_authenticated and self._session.user:
            auth_token = self._session.user.auth_token
            logger.info(f"Authenticating with user: {self._session.user.username}")
        else:
            logger.info("Proceeding with a guest session.")

        await self._ws.send_message(MessageType.SET_AUTH_TOKEN.value, [auth_token])

        self._chart_session_id = generate_session_id(self._CHART_SESSION_PREFIX)
        await self._ws.send_message(
            MessageType.CHART_CREATE_SESSION.value, [self._chart_session_id, ""]
        )
        logger.info("Handshake complete.")

    def _validate_parameters(
        self,
        symbol: str,
        interval: Interval,
        n_bars: int | None,
        start_time: datetime | None,
        end_time: datetime | None,
    ) -> None:
        """Validates input parameters to prevent basic errors."""
        if not re.match(r"^[A-Z_]+:[A-Z_]+$", symbol):
            raise TrdvException(
                "Symbol must be in the format 'EXCHANGE:SYMBOL', e.g., 'NASDAQ:AAPL'."
            )
        if not isinstance(interval, Interval):
            raise TrdvException(
                "Invalid interval provided. Must be an Interval enum member."
            )
        if not n_bars and not start_time:
            raise TrdvException("Either 'n_bars' or 'start_time' must be provided.")
        if n_bars and n_bars <= 0:
            raise TrdvException("'n_bars' must be a positive integer.")
        if start_time and end_time and start_time >= end_time:
            raise TrdvException("'start_time' must be before 'end_time'.")

    # --- Historical Data Fetching ---
    async def get_history(
        self,
        symbol: str,
        interval: Interval,
        n_bars: int | None = None,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
    ) -> pl.DataFrame:
        """
        Fetches historical OHLCV data for a given symbol and interval.

        The method first requests a small number of recent bars (`n_bars`) to initialize
        the data series. If a `start_time` is provided, it then makes a second request
        to fetch the full historical range.

        Args:
            symbol: The symbol to fetch data for (e.g., "NASDAQ:AAPL").
            interval: The time interval for the bars (e.g., Interval.in_1_hour).
            n_bars: The number of recent bars to fetch. Defaults to 10.
            start_time: The start of the historical date range.
            end_time: The end of the historical date range. Defaults to now.

        Returns:
            A Polars DataFrame containing the OHLCV data.
        """
        if not self._ws or not self._chart_session_id:
            raise TrdvException(
                "Client is not connected. Use 'async with' context manager."
            )

        # Set default values
        n_bars = n_bars or 10
        end_time = end_time or datetime.now(timezone.utc)
        symbol = symbol.strip().upper()
        self._validate_parameters(symbol, interval, n_bars, start_time, end_time)

        logger.info(f"Fetching history for {symbol} on interval {interval.value}...")

        series_id = generate_session_id(self._SERIES_ID_PREFIX)
        collector = TradingViewDataCollector(series_id, symbol, interval)
        self._active_collectors[series_id] = collector

        try:
            await self._ws.resolve_symbol(
                self._chart_session_id,
                symbol=symbol,
                symbol_id=self._INTERNAL_SYMBOL_ID,
            )
            await self._ws.create_series(
                self._chart_session_id,
                series_id,
                self._INTERNAL_SERIES_NAME,
                self._INTERNAL_SYMBOL_ID,
                str(interval),
                n_bars,
            )

            await self._process_messages_for_history(collector, start_time, end_time)

        finally:
            self._active_collectors.pop(series_id, None)

        logger.info(
            f"Total received {len(collector.all_series_data)} data points for {symbol}."
        )
        return collector.to_polars(start_time, end_time)

    async def _process_messages_for_history(
        self,
        collector: TradingViewDataCollector,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
    ):
        """Main message processing loop for a get_history request."""
        async_iter = self._ws._process_messages()

        while True:
            try:
                message = await asyncio.wait_for(
                    async_iter.__anext__(), timeout=self._DEFAULT_TIMEOUT
                )

                should_break = await self._handle_history_message(
                    message, collector, start_time, end_time
                )

                if should_break:
                    break

            except asyncio.TimeoutError:
                logger.error(
                    f"Timed out waiting for message for {collector.symbol}. Aborting."
                )
                break
            except StopAsyncIteration:
                logger.info("Message stream ended.")
                break

    async def _handle_history_message(
        self,
        message: dict,
        collector: TradingViewDataCollector,
        start_time: datetime | None,
        end_time: datetime | None,
    ) -> bool:
        """
        Handles a single WebSocket message.

        Returns:
            A boolean indicating if the message processing loop should terminate.
        """
        logger.debug(f"RECEIVED: {message}")
        msg_type = message.get("m")

        if msg_type in (
            MessageType.DATA_UPDATE.value,
            MessageType.TIMESCALE_UPDATE.value,
        ):
            payload: dict = message.get("p", [None, {}])[1]
            if payload and (
                series_data := payload.get(collector.series_id, {}).get("s")
            ):
                logger.info(
                    f"Adding {len(series_data)} data points to collector for '{collector.symbol}'."
                )
                collector.add_data(series_data)

        elif msg_type == MessageType.SERIES_COMPLETED.value:
            if not collector.is_initial_series_loaded:
                logger.info(f"Initial series load completed for {collector.symbol}.")

                if start_time:
                    range_str = (
                        f"r,{int(start_time.timestamp())}:{int(end_time.timestamp())}"
                    )
                    await self._ws.modify_series(
                        self._chart_session_id,
                        collector.series_id,
                        self._INTERNAL_SERIES_NAME,
                        self._INTERNAL_SYMBOL_ID,
                        str(collector.interval),
                        range_str,
                    )
                    logger.info(
                        f"Requested historical data from {start_time} to {end_time}."
                    )
                    collector.is_initial_series_loaded = True
                    return False
                else:
                    logger.info(
                        f"Initial data for {collector.symbol} received. Completing fetch."
                    )
                    return True
            else:
                logger.info(
                    f"Historical data range for {collector.symbol} received. Completing fetch."
                )
                return True

        elif msg_type == MessageType.PROTOCOL_ERROR.value:
            error_msg = message.get("p", ["Unknown error"])[0]
            raise TrdvException(f"Protocol error from server: {error_msg}")

        return False

    # --- Symbol Data ---
    async def get_symbol_info(self, symbol: str) -> dict | None:
        """
        Fetch detailed information for a single symbol.

        This includes session times, holidays, exchange details, splits, and more.

        Args:
            symbol (str): The symbol to fetch data for (e.g., "NASDAQ:AAPL").

        Returns:
            A dictionary containing the symbol information, or None if an error occurs.
        """
        if not self._ws or not self._chart_session_id:
            raise TrdvException(
                "Client is not connected. Use 'async with' context manager."
            )

        logger.info(f"Fetching symbol info for {symbol}...")

        try:
            await self._ws.resolve_symbol(
                self._chart_session_id,
                symbol=symbol,
                symbol_id=self._INTERNAL_SYMBOL_ID,
            )

            async_iter = self._ws._process_messages()
            while True:
                try:
                    message = await asyncio.wait_for(
                        async_iter.__anext__(), timeout=self._DEFAULT_TIMEOUT
                    )
                    logger.debug(f"RECEIVED: {message}")

                    msg_type = message.get("m")

                    if msg_type == MessageType.SYMBOL_RESOLVED.value:
                        symbol_info = message.get("p", [None, None, None])[2]
                        logger.info(f"Successfully resolved symbol info for {symbol}.")
                        return Symbol.model_validate(symbol_info)

                    if msg_type == MessageType.PROTOCOL_ERROR.value:
                        error_msg = message.get("p", ["Unknown error"])[0]
                        raise TrdvException(f"Protocol error from server: {error_msg}")

                except asyncio.TimeoutError:
                    logger.error(
                        f"Timed out waiting for symbol info for {symbol}. Aborting."
                    )
                    return None
                except StopAsyncIteration:
                    logger.info("Message stream ended before symbol info was received.")
                    return None

        except Exception as e:
            logger.error(
                f"An unexpected error occurred while fetching symbol info for {symbol}: {e}"
            )
            return None
