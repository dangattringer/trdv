import logging
from datetime import datetime, timezone

import polars as pl
from polars.exceptions import ComputeError, SchemaError

from .enums import Interval
from .exceptions import TrdvException

logger = logging.getLogger(__name__)


class TradingViewDataCollector:
    """
    Handles data collection and processing for a specific symbol request.

    This class acts as a temporary store for data received from the WebSocket
    and provides a method to convert it into a structured Polars DataFrame.
    """

    _SCHEMA = {
        "timestamp": pl.Datetime(time_zone="UTC"),
        "open": pl.Float64,
        "high": pl.Float64,
        "low": pl.Float64,
        "close": pl.Float64,
        "volume": pl.Float64,
    }

    def __init__(self, series_id: str, symbol: str, interval: Interval):
        self.series_id = series_id
        self.symbol = symbol
        self.interval = interval
        self.all_series_data: list = []
        self.is_initial_series_loaded: bool = False

    def add_data(self, series_data: list) -> None:
        """Add new series data points from a WebSocket message."""
        self.all_series_data.extend(series_data)

    def to_polars(
        self, start_time: datetime | None = None, end_time: datetime | None = None
    ) -> pl.DataFrame:
        """
        Convert collected data to a Polars DataFrame with filtering and sorting.

        Raises:
            TrdvException: If processing fails, wrapping the original error.
        """
        if not self.all_series_data:
            logger.warning(f"No data was received for symbol '{self.symbol}'")
            return pl.DataFrame(schema=self._SCHEMA)

        try:
            logger.info(
                f"Converting {len(self.all_series_data)} data points to DataFrame for '{self.symbol}'"
            )

            df = pl.from_records(self.all_series_data)
            df = df.select(
                pl.col("v").list.get(0).alias("timestamp"),
                pl.col("v").list.get(1).alias("open"),
                pl.col("v").list.get(2).alias("high"),
                pl.col("v").list.get(3).alias("low"),
                pl.col("v").list.get(4).alias("close"),
                pl.col("v").list.get(5).alias("volume"),
            )
            df = df.with_columns(
                pl.from_epoch(pl.col("timestamp"), time_unit="s").dt.replace_time_zone(
                    "UTC"
                )
            )

            df = df.select([pl.col(c).cast(t) for c, t in self._SCHEMA.items()])

            if start_time and end_time:
                start_utc = (
                    start_time.astimezone(timezone.utc)
                    if start_time.tzinfo
                    else start_time.replace(tzinfo=timezone.utc)
                )
                end_utc = (
                    end_time.astimezone(timezone.utc)
                    if end_time.tzinfo
                    else end_time.replace(tzinfo=timezone.utc)
                )

                df = df.filter(
                    (pl.col("timestamp") >= start_utc)
                    & (pl.col("timestamp") <= end_utc)
                )

            return df.sort("timestamp")

        except (SchemaError, ComputeError) as e:
            logger.error(
                f"Error processing data for '{self.symbol}' into DataFrame: {e}"
            )
            raise TrdvException(
                f"Failed to process market data for '{self.symbol}': {e}"
            ) from e
