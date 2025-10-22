from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field, model_validator


class OptionChainEntry(BaseModel):
    s: str
    ask: float
    bid: float
    currency: str
    delta: float
    expiration_date: int = Field(..., alias="expiration")
    gamma: float
    implied_volatility: float = Field(..., alias="iv")
    option_type: Literal["call", "put"] = Field(..., alias="option-type")
    price_scale: int = Field(..., alias="pricescale")
    rho: float
    root_symbol: str = Field(..., alias="root")
    strike: float
    price: float = Field(..., alias="theoPrice")
    theta: float
    vega: float
    bid_iv: float | None
    ask_iv: float | None


class OptionChain(BaseModel):
    total_count: int = Field(..., alias="totalCount")
    fields: list[str]
    options: list[OptionChainEntry]
    time: datetime | None = Field(None)

    @model_validator(mode="before")
    @classmethod
    def unpack_api_format(cls, data: Any) -> dict[str, Any]:
        """Convert API's (fields + f) format into dictionaries."""
        if not isinstance(data, dict) or "symbols" not in data or "fields" not in data:
            return data

        field_names = data["fields"]
        options = []
        for sym in data["symbols"]:
            if "f" in sym:
                option = {"s": sym["s"]}
                option.update(zip(field_names, sym["f"]))
                options.append(option)
            else:
                options.append(sym)

        data["options"] = options
        return data


class Series(BaseModel):
    exp: int
    id: str
    lotSize: int
    root: str
    strikes: list[float]
    underlying: str


class OptionsInfoResponse(BaseModel):
    pro_name: str
    lp: float
    series: list[Series]
    country_code: str

    @model_validator(mode="before")
    @classmethod
    def inject_series(cls, data):
        if "options-info" in data and "families" in data["options-info"]:
            all_series = []
            for fam in data["options-info"]["families"]:
                all_series.extend(fam.get("series", []))
            data = data.copy()
            data["series"] = all_series
        return data
