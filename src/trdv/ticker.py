import asyncio
import polars as pl
from .parsers import parse_ohlcv_to_dataframe
from .enums import Interval


class Ticker:
    def __init__(self, symbol: str, exchange: str = "NASDAQ"):
        pass
