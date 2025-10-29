from pydantic import BaseModel, Field


class OHLCData(BaseModel):
    timestamp: int = Field(..., description="Timestamp of the data point")
    open: float = Field(..., description="Opening price")
    high: float = Field(..., description="Highest price")
    low: float = Field(..., description="Lowest price")
    close: float = Field(..., description="Closing price")
    volume: float = Field(..., description="Trading volume")

    @classmethod
    def from_raw(cls, raw: dict):
        ts, o, h, l, c, v = raw["v"]
        return cls(timestamp=ts, open=o, high=h, low=l, close=c, volume=v)


class HistoricalData(BaseModel):
    data: list[OHLCData] = Field(..., description="List of OHLC data points")
