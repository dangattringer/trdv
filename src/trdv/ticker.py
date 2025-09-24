import asyncio
import polars as pl
from .client import HttpClient
from .parsers import parse_ohlcv_to_dataframe
from .enums import Interval


class Ticker:
    def __init__(self, symbol: str, exchange: str = "NASDAQ"):
        self.symbol = symbol
        self.exchange = exchange
        self._client = HttpClient()

    def history(
        self, interval: Interval = Interval.DAY, n_bars: int = 200
    ) -> pl.DataFrame:
        """Fetches historical OHLCV data."""
        raw_data = asyncio.run(
            self._client.fetch_ohlcv(self.symbol, self.exchange, interval.value, n_bars)
        )
        return parse_ohlcv_to_dataframe(raw_data)
