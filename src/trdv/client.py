import asyncio
import json
import logging
import random
import re
from datetime import datetime, timezone
from typing import Any, Callable, TypeVar

import aiohttp

from .collector import (
    TradingViewFundamentalsDataCollector,
    TradingViewSeriesDataCollector,
)
from .const import (
    BASE_NEWS_MEDIATOR_URL,
    OPTIONS_DEFAULT_COLUMNS,
    OPTIONS_URL,
    USER_AGENTS,
)
from .enums import Interval, MessageType
from .exceptions import TrdvException
from .models import (
    CorpActivity,
    Crypto,
    Economics,
    Fundamentals,
    HistoricalData,
    MarketType,
    News,
    OHLCData,
    OptionChain,
    OptionsInfo,
    Priority,
    Provider,
    Region,
    SecFilings,
    Sentiment,
    Symbol,
)
from .session import Session
from .utils import generate_session_id
from .websocket import WebSocketClient

logger = logging.getLogger(__name__)

T = TypeVar("T")


class TradingViewClient:
    """
    Asynchronous client to interact with the TradingView WebSocket API
    for fetching historical market data.
    """

    _DEFAULT_TIMEOUT = 10.0
    _GUEST_AUTH_TOKEN = "unauthorized_user_token"
    _CHART_SESSION_PREFIX = "cs"
    _QUOTE_SESSION_PREFIX = "qs_multiplexer_full"
    _QS_OPTION_PREFIX = "qs_snapshoter_options-product_"
    _SERIES_ID_PREFIX = "sds"
    _INTERNAL_SYMBOL_ID = "symbol_1"
    _INTERNAL_SERIES_NAME = "s1"
    _SYMBOL_PATTERN = re.compile(r"^[A-Z_]+:[A-Z_]+$")
    _DATE_PATTERN = re.compile(r"^\d{8}$")

    def __init__(self, session: Session | None = None):
        self._session = session or Session()
        self._ws: WebSocketClient | None = None
        self._chart_session_id: str | None = None
        self._quote_session_id: str | None = None
        self._qs_option_id: str | None = None
        self._active_collectors: dict[str, TradingViewSeriesDataCollector] = {}

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
            MessageType.CHART_CREATE_SESSION.value, [self._chart_session_id]
        )
        self._quote_session_id = generate_session_id(self._QUOTE_SESSION_PREFIX)
        await self._ws.create_quote_session(self._quote_session_id)
        self._qs_option_id = generate_session_id(self._QS_OPTION_PREFIX)
        await self._ws.create_option_session(self._qs_option_id)

        logger.info("Handshake complete.")

    @staticmethod
    def _validate_parameters(
        symbol: str,
        interval: Interval,
        n_bars: int | None,
        start_time: datetime | None,
        end_time: datetime | None,
    ) -> None:
        """Validates input parameters to prevent basic errors."""
        if not TradingViewClient._SYMBOL_PATTERN.match(symbol):
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

    @staticmethod
    def _convert_date(date: str | datetime | None) -> datetime | None:
        if date is None:
            return None
        if isinstance(date, datetime):
            return (
                date.astimezone(timezone.utc)
                if date.tzinfo
                else date.replace(tzinfo=timezone.utc)
            )
        try:
            return datetime.fromisoformat(date).astimezone(timezone.utc)
        except ValueError as e:
            raise TrdvException(
                "'start_time' and 'end_time' must be datetime objects or ISO format strings."
            ) from e

    @staticmethod
    def _get_user_agent() -> str:
        """Get user agent from session or default."""
        browser = random.choice(list(USER_AGENTS.keys()))
        return random.choice(USER_AGENTS[browser])

    def _prepare_and_validate_args(
        self,
        symbol: str,
        interval: Interval,
        n_bars: int | None,
        start_time: datetime | str | None,
        end_time: datetime | str | None,
    ) -> tuple[str, int, datetime | None, datetime]:
        """Normalizes, defaults, and validates all user-provided arguments."""
        symbol = symbol.strip().upper()
        final_end_time = (
            self._convert_date(end_time)
            if end_time is not None
            else datetime.now(timezone.utc)
        )
        final_start_time = self._convert_date(start_time)
        final_n_bars = n_bars or 10
        self._validate_parameters(
            symbol, interval, final_n_bars, final_start_time, final_end_time
        )

        return symbol, final_n_bars, final_start_time, final_end_time

    # --- Historical Data Fetching ---
    async def get_history(
        self,
        symbol: str,
        interval: Interval,
        n_bars: int | None = None,
        start_time: datetime | str | None = None,
        end_time: datetime | str | None = None,
    ) -> HistoricalData:
        """
        Fetches historical OHLCV data for a given symbol and interval.

        The method first requests a small number of recent bars (`n_bars`) to initialize
        the data series. If a `start_time` is provided, it then makes a second request
        to fetch the full historical range.

        Args:
            symbol: The symbol to fetch data for (e.g., "NASDAQ:AAPL").
            interval: The time interval for the bars (e.g., Interval.DAY).
            n_bars: The number of recent bars to fetch. Defaults to 10.
            start_time: The start of the historical date range.
            end_time: The end of the historical date range. Defaults to now.

        Returns:
            HistoricalDataResponse: The historical OHLCV data.
        """
        if not self._ws or not self._chart_session_id:
            raise TrdvException(
                "Client is not connected. Use 'async with' context manager."
            )

        symbol, n_bars, start_time, end_time = self._prepare_and_validate_args(
            symbol, interval, n_bars, start_time, end_time
        )

        logger.info(f"Fetching history for {symbol} on interval {interval.value}...")

        series_id = generate_session_id(self._SERIES_ID_PREFIX)
        collector = TradingViewSeriesDataCollector(series_id, symbol, interval)
        self._active_collectors[series_id] = collector

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
        try:
            await self._process_messages_for_history(collector, start_time, end_time)
        finally:
            self._active_collectors.pop(series_id, None)

        logger.info(
            f"Total received {len(collector.all_series_data)} data points for {symbol}."
        )
        return HistoricalData(
            data=[
                OHLCData.from_raw(d)
                for d in sorted(collector.all_series_data, key=lambda x: x["i"])
            ]
        )

    async def _process_messages_for_history(
        self,
        collector: TradingViewSeriesDataCollector,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
    ):
        """Main message processing loop for a get_history request."""

        async def handler(message: dict) -> bool | None:
            should_break = await self._handle_history_message(
                message, collector, start_time, end_time
            )
            return True if should_break else None

        await self._process_messages_until(handler)

    async def _handle_history_message(
        self,
        message: dict,
        collector: TradingViewSeriesDataCollector,
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
    async def _process_messages_until(
        self,
        handler: Callable[[dict], Any],
        timeout: float | None = None,
        raise_on_timeout: bool = False,
    ) -> T | None:
        """
        Generic message processing loop with timeout.

        Args:
            handler: Callable that processes each message. Return non-None to stop.
            timeout: Timeout in seconds per message.
            raise_on_timeout: If True, raises TrdvException on timeout instead of returning None.

        Returns:
            The non-None value returned by handler, or None on timeout/stream end.
        """
        timeout = timeout or self._DEFAULT_TIMEOUT
        async_iter = self._ws._process_messages()

        try:
            while True:
                try:
                    message = await asyncio.wait_for(
                        async_iter.__anext__(), timeout=timeout
                    )
                    logger.debug(f"RECEIVED: {message}")

                    result = handler(message)
                    if asyncio.iscoroutine(result):
                        result = await result

                    if result is not None:
                        return result

                except asyncio.TimeoutError:
                    if raise_on_timeout:
                        raise TrdvException("Timed out waiting for message") from None
                    logger.error("Timed out waiting for message.")
                    return None
                except StopAsyncIteration:
                    logger.info("Message stream ended.")
                    return None
        finally:
            await async_iter.aclose()

    async def get_symbol_info(self, symbol: str) -> Symbol | None:
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

        await self._ws.resolve_symbol(
            self._chart_session_id,
            symbol=symbol,
            symbol_id=self._INTERNAL_SYMBOL_ID,
        )

        async def handler(message: dict) -> Symbol | None:
            msg_type = message.get("m")

            if msg_type == MessageType.SYMBOL_RESOLVED.value:
                symbol_info = message.get("p", [None, None, None])[2]
                logger.info(f"Successfully resolved symbol info for {symbol}.")
                return Symbol(**symbol_info)

            if msg_type == MessageType.PROTOCOL_ERROR.value:
                error_msg = message.get("p", ["Unknown error"])[0]
                raise TrdvException(f"Protocol error from server: {error_msg}")

            return None

        return await self._process_messages_until(handler)

    # --- Fundamental Data ---
    async def get_fundamentals(self, symbol: str) -> Fundamentals | None:
        """
        Fetch fundamental data for a given symbol.

        Args:
            symbol: The symbol to fetch fundamental data for (e.g., "NASDAQ:AAPL").
        Returns:
            A Fundamentals object containing the fundamental data.
        Raises:
            TrdvException: If the client is not connected or if an error occurs during data retrieval

        """
        if not self._ws or not self._quote_session_id:
            raise TrdvException(
                "Client is not connected. Use 'async with' context manager."
            )

        logger.info(f"Fetching fundamental data for {symbol}...")
        collector = TradingViewFundamentalsDataCollector(symbol)

        await self._ws.quote_add_symbols(
            self._quote_session_id,
            symbols_str=f'={{"adjustment":"splits","currency-id":"USD","symbol":"{symbol}"}}',
        )

        # await self._ws.quote_add_symbols(
        #     self._qs_snapshot_id,
        #     symbols_str=symbol,
        # )
        # await self._ws.quote_fast_symbols(
        #     self._quote_session_id,
        #     symbols_str=f'={{"adjustment":"splits","currency-id":"USD","symbol":"{symbol}"}}',
        # )
        async def handler(message: dict) -> Fundamentals | None:
            msg_type = message.get("m")
            payload = message.get("p", [])

            if (
                msg_type == MessageType.QUOTE_SERIES_DATA.value
                and payload[0] == self._quote_session_id
            ):
                data = payload[1].get("v", {})
                collector.add_data(data)
                return None

            if (
                msg_type == MessageType.QUOTE_COMPLETED.value
                and payload[0] == self._quote_session_id
            ):
                logger.info(f"Fundamental data for {symbol} received.")
                return Fundamentals(**collector.fundamentals_data)

            return None

        return await self._process_messages_until(handler)

    # --- News ---
    @staticmethod
    def _prepare_news_filters(
        symbol: str | None = None,
        market_type: MarketType | str | None = None,
        region: Region | str | None = None,
        corp_activity: CorpActivity | str | None = None,
        crypto: Crypto | str | None = None,
        economic_category: Economics | str | None = None,
        priority: Priority | str | None = None,
        provider: Provider | str | None = None,
        sec_filings: SecFilings | str | None = None,
        sentiment: Sentiment | str | None = None,
    ) -> list[tuple[str, str]]:
        if symbol and not TradingViewClient._SYMBOL_PATTERN.match(symbol):
            raise TrdvException(
                "Symbol must be in the format 'EXCHANGE:SYMBOL', e.g., 'NASDAQ:AAPL'."
            )

        enum_mapping = {
            "market": (market_type, MarketType),
            "area": (region, Region),
            "corp_activity": (corp_activity, CorpActivity),
            "crypto": (crypto, Crypto),
            "economic_category": (economic_category, Economics),
            "priority": (priority, Priority),
            "provider": (provider, Provider),
            "sec_filings": (sec_filings, SecFilings),
            "sentiment": (sentiment, Sentiment),
        }

        filters = {"lang": "en"}
        if symbol:
            filters["symbol"] = symbol

        for key, (value, enum_class) in enum_mapping.items():
            if value is None:
                continue

            try:
                enum_member = enum_class(value)
                filters[key] = enum_member.value
            except ValueError:
                valid_options = ", ".join([e.value for e in enum_class])
                raise TrdvException(
                    f"Invalid {key}: '{value}'. Valid options: {valid_options}"
                )
        return sorted([("filter", f"{k}:{v}") for k, v in filters.items()])

    async def get_news(
        self,
        symbol: str | None = None,
        market_type: MarketType | str | None = None,
        region: Region | str | None = None,
        corp_activity: CorpActivity | str | None = None,
        crypto: Crypto | str | None = None,
        economic_category: Economics | str | None = None,
        priority: Priority | str | None = None,
        provider: Provider | str | None = None,
        sec_filings: SecFilings | str | None = None,
        sentiment: Sentiment | str | None = None,
        streaming: bool = False,
    ) -> News:
        """
        Fetches news articles from TradingView's news API with optional filtering.

        Args:
            symbol: Filter news by a specific symbol (format: "EXCHANGE:SYMBOL").
            market_type: Filter by market type (e.g., MarketType.STOCKS).
            region: Filter by geographical region (e.g., Region.NORTH_AMERICA).
            corp_activity: Filter by corporate activities (e.g., CorpActivity.EARNINGS).
            crypto: Filter by cryptocurrency topics (e.g., Crypto.EXCHANGES).
            economic_category: Filter by economic categories (e.g., Economics.GDP).
            priority: Filter by news priority (e.g., Priority.TOP_STORIES).
            provider: Filter by news provider (e.g., Provider.REUTERS).
            sec_filings: Filter by SEC filing types (e.g., SecFilings.FORM_10K).
            sentiment: Filter by sentiment (e.g., Sentiment.POSITIVE).
            streaming: If True, fetches streaming news updates.

        Returns:
            A NewsResponse object containing the fetched news articles.

        Raises:
            TrdvException: If the request fails or the response cannot be parsed.
            ValueError: If the response data is invalid.
        """
        params = [("client", "web"), ("streaming", "true" if streaming else "false")]
        params.extend(
            self._prepare_news_filters(
                symbol=symbol,
                market_type=market_type,
                region=region,
                corp_activity=corp_activity,
                crypto=crypto,
                economic_category=economic_category,
                priority=priority,
                provider=provider,
                sec_filings=sec_filings,
                sentiment=sentiment,
            )
        )

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    BASE_NEWS_MEDIATOR_URL,
                    params=params,
                    headers={
                        "User-Agent": self._get_user_agent(),
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate, br, zstd",
                    },
                    timeout=10,
                ) as response:
                    response.raise_for_status()
                    data = await response.json()
                    return News(**data)

        except aiohttp.ClientError as e:
            raise TrdvException(f"Failed to fetch news: {e}") from e
        except (ValueError, TypeError) as e:
            raise TrdvException(f"Failed to parse JSON response: {e}") from e

    # --- Options Data ---
    def _build_request_payload(
        self,
        symbol: str,
        date: int | None,
    ) -> dict[str, Any]:
        """Build the request payload for options data."""
        filters = [{"left": "type", "operation": "equal", "right": "option"}]
        if date:
            filters.append({"left": "expiration", "operation": "equal", "right": date})

        return {
            "columns": OPTIONS_DEFAULT_COLUMNS,
            "filter": filters,
            "ignore_unknown_fields": False,
            "index_filters": [{"name": "underlying_symbol", "values": [symbol]}],
        }

    async def get_available_options(self, symbol: str) -> OptionsInfo:
        """Fetches available option expiration dates for a given symbol.

        Args:
            symbol: The symbol to fetch options data for (e.g., "NASDAQ:AAPL").

        Returns:
            An OptionInfoResponse object containing the available expiration dates.
        """
        collector = []
        await self._ws.quote_add_symbols(
            self._qs_option_id,
            symbols_str=symbol,
        )

        async def handler(message: dict) -> list[dict] | None:
            msg_type = message.get("m")
            payload = message.get("p", [])

            if (
                msg_type == MessageType.QUOTE_SERIES_DATA.value
                and payload[0] == self._qs_option_id
            ):
                data = payload[1].get("v", {})
                collector.append(data)
                logger.debug(f"Options data chunk received: {len(data)} items")
                return None

            if (
                msg_type == MessageType.QUOTE_COMPLETED.value
                and payload[0] == self._qs_option_id
            ):
                logger.info(
                    f"Options data collection complete: {len(collector)} chunks"
                )
                return OptionsInfo(**collector[0])

            return None

        return await self._process_messages_until(handler)

    @staticmethod
    def _validate_date(date: str) -> None:
        """Validate date format and value."""
        if not TradingViewClient._DATE_PATTERN.match(date):
            raise TrdvException(
                f"Invalid date format: '{date}'. "
                "Must be 'YYYYMMDD' (e.g., '20251114')"
            )
        try:
            datetime.strptime(date, "%Y%m%d")
        except ValueError:
            raise TrdvException(f"Invalid date value: '{date}'")

    async def get_options_data(
        self, symbol: str, expiration_date: str | None = None
    ) -> OptionChain:
        """Fetches options data for a given symbol and expiration date.


        Args:
            symbol: The symbol to fetch options data for (e.g., "NASDAQ:AAPL").
            expiration_date: The expiration date in 'YYYYMMDD' format. If None, fetches all available expiration dates.

        Returns:
            An OptionResponse object containing the options data.
        """
        if not TradingViewClient._SYMBOL_PATTERN.match(symbol):
            raise TrdvException(
                f"Invalid symbol format: '{symbol}'. "
                "Must be 'EXCHANGE:SYMBOL' (e.g., 'NASDAQ:AAPL')"
            )
        if expiration_date:
            available_options = await self.get_available_options(symbol)
            available_dates = [exp.exp for exp in available_options.series]

            self._validate_date(expiration_date)
            expiration_date = int(expiration_date)
            if expiration_date not in available_dates:
                raise TrdvException(
                    f"Invalid expiration date: '{expiration_date}'. "
                    f"Available dates: {available_dates}"
                )

        data = self._build_request_payload(symbol, expiration_date)
        params = {"label-product": "options-builder"}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                OPTIONS_URL,
                params=params,
                data=json.dumps(data),
                headers={
                    "User-Agent": self._get_user_agent(),
                    "Content-Type": "text/plain;charset=UTF-8",
                    "Accept": "application/json",
                    "Accept-Encoding": "gzip, deflate, br, zstd",
                    "Origin": "https://www.tradingview.com",
                },
                timeout=10,
            ) as response:
                response.raise_for_status()
                data = await response.json()
                return OptionChain(**data)
