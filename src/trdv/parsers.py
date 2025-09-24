import polars as pl


def parse_ohlcv_to_dataframe(raw_data: dict) -> pl.DataFrame:
    """Transforms the raw JSON from fetch_ohlcv into a Polars DataFrame."""
    if not raw_data or "data" not in raw_data:
        return pl.DataFrame()

    df = pl.DataFrame(raw_data["data"])

    df = df.rename(
        {
            "t": "timestamp",
            "o": "open",
            "h": "high",
            "l": "low",
            "c": "close",
            "v": "volume",
        }
    )

    df = df.with_columns(
        pl.from_epoch(pl.col("timestamp"), time_unit="s").alias("timestamp")
    )
    return df
