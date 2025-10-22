from typing import Any

from pydantic import BaseModel, Field


class Source2(BaseModel):
    """
    Represents the secondary source of information for a trading symbol.
    """

    country: str
    description: str
    exchange_type: str = Field(..., alias="exchange-type")
    id: str
    name: str
    url: str


class Subsession(BaseModel):
    """
    Represents a subsession within a trading session, such as pre-market or regular trading hours.
    """

    description: str
    id: str
    private: bool
    session: str
    session_correction: str | None = Field(None, alias="session-correction")
    session_display: str = Field(..., alias="session-display")


class Figi(BaseModel):
    """
    Represents the Financial Instrument Global Identifier (FIGI) for a trading symbol.
    """

    country_composite: str = Field(..., alias="country-composite")
    exchange_level: str = Field(..., alias="exchange-level")


class Symbol(BaseModel):
    """
    Represents detailed descriptive information for a trading symbol.
    """

    local_description: str
    name: str
    full_name: str
    pro_name: str
    base_name: list[str]
    description: str
    currency_code: str
    exchange: str
    source_id: str
    session_holidays: str
    subsession_id: str
    provider_id: str
    currency_id: str
    country: str
    pro_perm: str
    measure: str
    allowed_adjustment: str
    short_description: str
    variable_tick_size: str
    cusip: str
    isin: str
    language: str
    pricescale: int
    pointvalue: float
    minmov: int
    session: str
    session_display: str
    source2: Source2
    subsessions: list[Subsession]
    type: str
    typespecs: list[str]
    has_intraday: bool
    fractional: bool
    listed_exchange: str
    legs: list[str]
    is_tradable: bool
    minmove2: int
    timezone: str
    aliases: list[Any]
    alternatives: list[str]
    is_replayable: bool
    has_adjustment: bool
    has_extended_hours: bool
    bar_source: str
    bar_transform: str
    bar_fillgaps: bool
    visible_plots_set: str
    isin_displayed: str = Field(..., alias="isin-displayed")
    is_tickbars_available: bool = Field(..., alias="is-tickbars-available")
    figi: Figi
    exchange_listed_name: str
