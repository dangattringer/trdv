import asyncio
from datetime import datetime
import json
import re
import logging
from typing import AsyncGenerator, Union

import websockets
from websockets.exceptions import ConnectionClosed, WebSocketException

from .session import Session
from .utils import format_message
from .exceptions import TrdvException, WebSocketTimeoutError
from .enums import MessageType, Interval
from .const import TRADINGVIEW_DATA_URL

logger = logging.getLogger(__name__)


class WebSocketClient:
    """A client for connecting to the TradingView WebSocket API."""

    def __init__(self, session: Session, connection_timeout: float = 10.0):
        self.session = session
        self._ws_connection: websockets.connect | None = None
        self._connection_timeout = connection_timeout
        self._closed = False

        current_date = datetime.now().isoformat()
        self.uri = f"wss://data.tradingview.com/socket.io/websocket?from=chart%2F&date={current_date}&type=chart"

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def connect(self):
        """Establish WebSocket connection with proper error handling."""
        logger.info("Connecting to WebSocket...")
        try:
            self._ws_connection = await asyncio.wait_for(
                websockets.connect(
                    self.uri,
                    origin=TRADINGVIEW_DATA_URL,
                    ping_interval=20,
                    ping_timeout=10,
                    close_timeout=10,
                ),
                timeout=self._connection_timeout,
            )
            self._closed = False
            logger.info("WebSocket connection established.")
        except asyncio.TimeoutError:
            raise WebSocketTimeoutError("WebSocket connection timed out") from None
        except (OSError, WebSocketException) as e:
            raise TrdvException(f"Failed to connect to WebSocket: {e}") from e

    async def close(self):
        """Close WebSocket connection gracefully."""
        if self._ws_connection and not self._closed:
            try:
                await self._ws_connection.close()
            except Exception as e:
                logger.warning(f"Error closing WebSocket connection: {e}")
            finally:
                self._closed = True
                logger.info("WebSocket connection closed.")

    @property
    def is_connected(self) -> bool:
        """Check if WebSocket is connected and open."""
        return (
            self._ws_connection is not None
            and not self._closed
            and self._ws_connection.state == websockets.protocol.State.OPEN
        )

    async def send_message(self, message_type: Union[MessageType, str], payload: list):
        """Send message with enum support."""
        if not self.is_connected:
            raise TrdvException("WebSocket is not connected.")

        try:
            msg_type = (
                str(message_type)
                if isinstance(message_type, MessageType)
                else message_type
            )
            message = format_message(msg_type, payload)
            logger.debug(f"SENDING: {message}")
            await self._ws_connection.send(message)
        except ConnectionClosed:
            self._closed = True
            raise TrdvException("WebSocket connection was closed during send") from None
        except Exception as e:
            raise TrdvException(f"Failed to send message: {e}") from e

    async def resolve_symbol(
        self, session_id: str, symbol: str, symbol_id: str = "symbol_1"
    ):
        """Convenience method for resolving symbols using enum."""
        await self.send_message(
            MessageType.RESOLVE_SYMBOL,
            [session_id, symbol_id, f'={{"symbol":"{symbol}","adjustment":"splits"}}'],
        )

    async def create_series(
        self,
        session_id: str,
        series_id: str,
        series_sub_id: str,
        symbol_id: str,
        interval: Union[Interval, str],
        bars_count: int = 300,
    ):
        """Create a data series with enum support."""
        interval_str = str(interval) if isinstance(interval, Interval) else interval
        await self.send_message(
            MessageType.CREATE_SERIES,
            [session_id, series_id, series_sub_id, symbol_id, interval_str, bars_count],
        )

    async def modify_series(
        self,
        chart_session_id: str,
        series_id: str,
        series_sub_id: str,
        symbol_id: str,
        interval: Union[Interval, str],
        range_str: str = "",
    ):
        """
        Send a modify_series message to update interval and/or range.

        Args:
            chart_session_id: The chart session ID (e.g., "cs_gFkIf8kZfcZu").
            series_id: The main series ID (e.g., "sds_1").
            series_sub_id: The subseries ID (e.g., "s2").
            symbol_id: The symbol ID (e.g., "sds_sym_2").
            interval: The new interval (e.g., "1D").
            range_str: The range string, e.g., "r,1432684800:1443139200" or "" for latest bars.
        """
        interval = str(interval) if isinstance(interval, Interval) else interval
        payload = [
            chart_session_id,
            series_id,
            series_sub_id,
            symbol_id,
            interval,
            range_str,
        ]
        await self.send_message(MessageType.MODIFY_SERIES, payload)

    async def quote_add_symbols(self, session_id: str, symbols: list[str]):
        """Add symbols to quote session."""
        await self.send_message(MessageType.QUOTE_ADD_SYMBOLS, [session_id, *symbols])

    async def _handle_keepalive(self, buffer: str) -> str:
        """Handle keep-alive messages."""
        try:
            await self._ws_connection.send(buffer)
            logger.debug(f"RESPONDED to keep-alive: {buffer}")
            return ""
        except ConnectionClosed:
            self._closed = True
            raise TrdvException("Connection closed during keep-alive") from None

    def _extract_messages(self, buffer: str) -> tuple[list[str], str]:
        """Extract complete messages from buffer."""
        messages = []

        while buffer:
            match = re.search(r"~m~(\d+)~m~", buffer)
            if not match:
                break

            msg_len = int(match.group(1))
            header_len = match.end()
            total_len = header_len + msg_len

            if len(buffer) < total_len:
                break

            payload_str = buffer[header_len:total_len]
            buffer = buffer[total_len:]

            if payload_str.startswith("{"):
                messages.append(payload_str)

        return messages, buffer

    async def _process_messages(self) -> AsyncGenerator[dict, None]:
        """Process incoming WebSocket messages with improved error handling."""
        buffer = ""

        try:
            while self.is_connected:
                try:
                    data = await asyncio.wait_for(
                        self._ws_connection.recv(), timeout=30.0
                    )
                    buffer += data

                except asyncio.TimeoutError:
                    logger.debug("Timeout waiting for WebSocket message")
                    continue

                except ConnectionClosed:
                    logger.warning("WebSocket connection was closed.")
                    self._closed = True
                    break

                if re.match(r"~h~\d+", buffer):
                    buffer = await self._handle_keepalive(buffer)
                    continue

                messages, buffer = self._extract_messages(buffer)
                logger.debug(f"Extracted {len(messages)} messages from buffer")
                for message_str in messages:
                    try:
                        message_data = json.loads(message_str)
                        yield message_data
                    except json.JSONDecodeError as e:
                        logger.warning(
                            f"JSON decode error for message '{message_str[:100]}...': {e}"
                        )

        except Exception as e:
            logger.error(f"Unexpected error in message processing: {e}")
            raise TrdvException(f"Message processing failed: {e}") from e

    async def listen(self) -> AsyncGenerator[dict, None]:
        """Public interface for listening to messages."""
        if not self.is_connected:
            raise TrdvException("WebSocket is not connected. Call connect() first.")

        async for message in self._process_messages():
            yield message
