from __future__ import annotations

from typing import get_args, get_origin

from pydantic import BaseModel, ConfigDict, Field, model_validator


class Fundamentals(BaseModel):
    """Comprehensive financial fundamentals data for an asset."""

    model_config = ConfigDict(extra="allow")

    analyst_ratings: AnalystRatings | None = Field(
        None, description="Analyst ratings data."
    )
    balance_sheet: BalanceSheet | None = Field(None, description="Balance sheet data.")
    company_info: CompanyInfo | None = Field(
        None, description="Information about the company."
    )
    dividends: Dividends | None = Field(None, description="Dividends data.")
    earnings: Earnings | None = Field(None, description="Earnings data.")
    market_data: MarketData | None = Field(
        None, description="Market data and pricing information."
    )
    ratios: Ratios | None = Field(None, description="Financial ratios.")
    revenue: Revenue | None = Field(None, description="Revenue data.")
    share_details: ShareDetails | None = Field(
        None, description="Details about the company's shares."
    )

    @model_validator(mode="before")
    @classmethod
    def group_nested_fields(cls, data: dict) -> dict:
        """
        Transforms flat input data by grouping fields into their respective
        nested model structures based on field definitions.
        """
        if not isinstance(data, dict):
            return data

        # Process each field in the Fundamentals model
        for field_name, field_info in Fundamentals.model_fields.items():
            model_type = cls._extract_model_type(field_info.annotation)
            if model_type is None:
                continue

            nested_fields = model_type.model_fields.keys()
            nested_data = {
                key: data.pop(key) for key in list(data.keys()) if key in nested_fields
            }

            if nested_data:
                data[field_name] = nested_data

        return data

    @staticmethod
    def _extract_model_type(annotation) -> type[BaseModel] | None:
        """
        Extracts the BaseModel type from a field annotation.
        Handles Union types (e.g., Model | None) and direct types.
        """
        origin = get_origin(annotation)
        if origin is not None:
            args = get_args(annotation)
            for arg in args:
                if isinstance(arg, type) and issubclass(arg, BaseModel):
                    return arg
        elif isinstance(annotation, type) and issubclass(annotation, BaseModel):
            return annotation

        return None


# --- Nested Models ---
class AnalystRatings(BaseModel):
    model_config = ConfigDict(extra="forbid")
    price_target_down_num: int | None = Field(
        None, description="Number of analysts with a 'down' price target"
    )
    price_target_up_num: int | None = Field(
        None, description="Number of analysts with an 'up' price target"
    )
    recommendation_buy: int | None = Field(
        None, description="Number of 'buy' recommendations"
    )
    recommendation_date: str | None = Field(
        None, description="Date of the latest recommendation summary"
    )
    recommendation_hold: int | None = Field(
        None, description="Number of 'hold' recommendations"
    )
    recommendation_mark: float | None = Field(
        None, description="Overall recommendation score"
    )
    recommendation_over: int | None = Field(
        None, description="Number of 'overweight' recommendations"
    )
    recommendation_sell: int | None = Field(
        None, description="Number of 'sell' recommendations"
    )
    recommendation_total: int | None = Field(
        None, description="Total number of recommendations"
    )
    recommendation_under: int | None = Field(
        None, description="Number of 'underweight' recommendations"
    )


class BalanceSheet(BaseModel):
    """Represents items typically found on a balance sheet."""

    model_config = ConfigDict(extra="forbid")

    # Assets
    total_assets_fy: float | None = Field(
        None, description="Total assets for the fiscal year."
    )
    total_assets_fq: float | None = Field(
        None, description="Total assets for the fiscal quarter."
    )
    total_assets_fq_h: list[float | None] | None = Field(
        None, description="List of total assets for the fiscal quarter."
    )
    total_assets_h: list[float | None] | None = Field(
        None, description="List of total assets for the fiscal year."
    )
    total_assets_per_employee_fy: float | None = Field(
        None, description="Total assets per employee for the fiscal year."
    )
    total_assets_to_equity_fy: float | None = Field(
        None, description="Total assets to equity ratio for the fiscal year."
    )
    total_current_assets_fy: float | None = Field(
        None, description="Total current assets for the fiscal year."
    )
    total_assets_to_equity_fq: float | None = Field(
        None, description="Total assets to equity ratio for the fiscal quarter."
    )
    total_current_assets_fq: float | None = Field(
        None, description="Total current assets for the fiscal quarter."
    )
    total_inventory_fy: float | None = Field(
        None, description="Total inventory for the fiscal year."
    )
    total_inventory_fq: float | None = Field(
        None, description="Total inventory for the fiscal quarter."
    )
    accounts_receivables_net_fy: float | None = Field(
        None, description="Net accounts receivables for the fiscal year."
    )
    accounts_receivables_net_fq: float | None = Field(
        None, description="Net accounts receivables for the fiscal quarter."
    )
    goodwill_fy: float | None = Field(None, description="Goodwill for the fiscal year.")
    goodwill_fq: float | None = Field(
        None, description="Goodwill for the fiscal quarter."
    )
    intangibles_net_fy: float | None = Field(
        None, description="Net intangible assets for the fiscal year."
    )
    intangibles_net_fq: float | None = Field(
        None, description="Net intangible assets for the fiscal quarter."
    )
    ppe_total_net_fy: float | None = Field(
        None, description="Net property, plant, and equipment for the fiscal year."
    )
    ppe_total_net_fq: float | None = Field(
        None, description="Net property, plant, and equipment for the fiscal quarter."
    )

    # Liabilities
    total_liabilities_fy: float | None = Field(
        None, description="Total liabilities for the fiscal year."
    )
    total_liabilities_fq: float | None = Field(
        None, description="Total liabilities for the fiscal quarter."
    )
    total_current_liabilities_fy: float | None = Field(
        None, description="Total current liabilities for the fiscal year."
    )
    total_current_liabilities_fq: float | None = Field(
        None, description="Total current liabilities for the fiscal quarter."
    )
    accounts_payable_fy: float | None = Field(
        None, description="Accounts payable for the fiscal year."
    )
    accounts_payable_fq: float | None = Field(
        None, description="Accounts payable for the fiscal quarter."
    )
    total_debt_fy: float | None = Field(
        None, description="Total debt for the fiscal year."
    )
    total_debt_fq: float | None = Field(
        None, description="Total debt for the fiscal quarter."
    )
    net_debt_fy: float | None = Field(None, description="Net debt for the fiscal year.")
    net_debt_fq: float | None = Field(
        None, description="Net debt for the fiscal quarter."
    )

    # Equity
    shrhldrs_equity_fy: float | None = Field(
        None, description="Shareholders' equity for the fiscal year."
    )
    shrhldrs_equity_fq: float | None = Field(
        None, description="Shareholders' equity for the fiscal quarter."
    )
    retained_earnings_fy: float | None = Field(
        None, description="Retained earnings for the fiscal year."
    )
    retained_earnings_fq: float | None = Field(
        None, description="Retained earnings for the fiscal quarter."
    )

    # Historical data examples
    total_assets_fy_h: list[float | None] | None = Field(
        None, description="List of historical total assets for the fiscal year."
    )
    accounts_payable_fy_h: list[float | None] | None = Field(
        None, description="List of historical accounts payable for the fiscal year."
    )
    total_debt_fy_h: list[float | None] | None = Field(
        None, description="List of historical total debt for the fiscal year."
    )
    shrhldrs_equity_fy_h: list[float | None] | None = Field(
        None, description="List of historical shareholders' equity for the fiscal year."
    )


class CompanyInfo(BaseModel):
    """Descriptive information about the company."""

    model_config = ConfigDict(extra="forbid")

    industry: str | None = Field(None, description="The company's industry.")
    sector: str | None = Field(None, description="The company's sector.")
    ceo: str | None = Field(
        None, description="The name of the Chief Executive Officer."
    )
    web_site_url: str | None = Field(
        None, description="The company's official website URL."
    )
    business_description: str | None = Field(
        None, description="A description of the company's business."
    )
    number_of_employees: int | None = Field(
        None, description="The total number of employees."
    )
    number_of_shareholders: int | None = Field(
        None, description="The total number of shareholders."
    )

    symbol: str | None = Field(None, description="The ticker symbol of the asset")
    pro_name: str | None = Field(
        None,
        description="The professional name of the asset, often used in professional terminals",
    )
    symbol_fullname: str | None = Field(
        None,
        alias="symbol-fullname",
        description="The full, unambiguous name of the symbol",
    )
    symbol_proname: str | None = Field(
        None,
        alias="symbol-proname",
        description="A professional-grade name for the symbol",
    )
    original_name: str | None = Field(
        None,
        description="The original name of the asset before any changes or mappings",
    )
    base_name: list[str] | None = Field(
        None,
        description="The base name components of the asset, often used for derivatives or complex instruments",
    )

    # Descriptive Information
    short_name: str | None = Field(
        None, description="The short or commonly used name of the asset"
    )
    description: str | None = Field(
        None,
        description="A detailed description of the asset or the underlying company",
    )
    short_description: str | None = Field(
        None, description="A brief, concise description of the asset"
    )
    local_description: str | None = Field(
        None, description="The description of the asset in a local language"
    )

    # Classification and Type
    type: str | None = Field(
        None, description="The type of the asset (e.g., 'stock', 'etf', 'fund')"
    )
    typespecs: list[str] | None = Field(
        None,
        description="Specific classifications or attributes related to the asset type",
    )

    # Standardized Codes
    isin: str | None = Field(
        None, description="International Securities Identification Number (ISIN)"
    )
    isin_displayed: str | None = Field(
        None, alias="isin-displayed", description="The display format for the ISIN"
    )
    cusip: str | None = Field(
        None,
        description="Committee on Uniform Securities Identification Procedures (CUSIP) number",
    )
    cik_code: int | None = Field(
        None,
        alias="cik-code",
        description="Central Index Key (CIK) code used by the SEC",
    )
    mic: str | None = Field(
        None, description="The Market Identifier Code (MIC) for the primary exchange"
    )


class Dividends(BaseModel):
    """
    Consolidates all dividend-related data, including yield, payments,
    and historical trends for both common and preferred shares.
    """

    model_config = ConfigDict(extra="forbid")

    # Core Snapshot Metrics
    dividends_paid: float | None = Field(
        None,
        description="The primary value of dividends paid in the most recent period.",
    )
    dividends_availability: float | None = Field(
        None,
        description="A code or status indicating dividend availability.",
    )
    dividends_per_share_fq: float | None = Field(
        None,
        description="Dividends paid per share for the most recent fiscal quarter.",
    )

    # Yield
    dividends_yield_current: float | None = Field(
        None, description="The current dividend yield."
    )
    dividends_yield_fq: float | None = Field(
        None,
        description="Dividend yield for the most recent fiscal quarter.",
    )
    dividends_yield_fy: float | None = Field(
        None,
        description="Dividend yield for the most recent fiscal year.",
    )

    # Total Cash Paid
    total_cash_dividends_paid_ttm: float | None = Field(
        None,
        description="Total cash dividends paid over the trailing twelve months.",
    )
    total_cash_dividends_paid_fy: float | None = Field(
        None,
        description="Total cash dividends paid for the fiscal year.",
    )
    total_cash_dividends_paid_fq: float | None = Field(
        None,
        description="Total cash dividends paid for the fiscal quarter.",
    )
    total_cash_dividends_paid_fh: float | None = Field(
        None,
        description="Total cash dividends paid for the fiscal half-year.",
    )

    # Cash Flow for Common/Preferred Shares
    common_dividends_cash_flow_ttm: float | None = Field(
        None, description="Cash flow for common dividends over the TTM."
    )
    common_dividends_cash_flow_fy: float | None = Field(
        None, description="Cash flow for common dividends for the fiscal year."
    )
    common_dividends_cash_flow_fq: float | None = Field(
        None, description="Cash flow for common dividends for the fiscal quarter."
    )
    preferred_dividends_cash_flow_ttm: float | None = Field(
        None, description="Cash flow for preferred dividends over the TTM."
    )
    preferred_dividends_cash_flow_fy: float | None = Field(
        None, description="Cash flow for preferred dividends for the fiscal year."
    )

    # Other Metrics
    preferred_dividends_fy: float | None = Field(
        None, description="Value of preferred dividends for the fiscal year."
    )
    dividends_payable_fy: float | None = Field(
        None, description="Dividends payable for the fiscal year."
    )

    # Historical Time Series Data
    historical_yield_yearly: list | None = Field(
        None, description="Historical dividend yield for fiscal years."
    )
    historical_total_paid_quarterly: list | None = Field(
        None, description="Historical total cash dividends paid for fiscal quarters."
    )
    historical_total_paid_yearly: list | None = Field(
        None, description="Historical total cash dividends paid for fiscal years."
    )
    historical_payable_yearly: list | None = Field(
        None, description="Historical dividends payable for fiscal years."
    )

    historical_common_cash_flow_quarterly: list | None = Field(
        None, description="Historical cash flow for common dividends by quarter."
    )
    historical_common_cash_flow_yearly: list | None = Field(
        None, description="Historical cash flow for common dividends by year."
    )

    historical_preferred_quarterly: list | None = Field(
        None, description="Historical value of preferred dividends by quarter."
    )
    historical_preferred_yearly: list | None = Field(
        None, description="Historical value of preferred dividends by year."
    )
    historical_preferred_cash_flow_quarterly: list | None = Field(
        None, description="Historical cash flow for preferred dividends by quarter."
    )
    historical_preferred_cash_flow_yearly: list | None = Field(
        None, description="Historical cash flow for preferred dividends by year."
    )


class Earnings(BaseModel):
    model_config = ConfigDict(extra="forbid")
    earnings_release_date: float | None = Field(
        None, description="Earnings release date"
    )
    earnings_per_share_forecast_next_fq: float | None = Field(
        None, description="Earnings per share forecast for the next fiscal quarter"
    )
    earnings_release_next_date: float | None = Field(
        None, description="Earnings release date for the next period"
    )
    earnings_per_share_fq: float | None = Field(
        None, description="Earnings per share for the fiscal quarter"
    )
    earnings_availability: float | None = Field(
        None, description="Earnings availability"
    )
    earnings_per_share_basic_ttm: float | None = Field(
        None, description="Earnings per share basic for the trailing twelve months"
    )
    earnings_per_share_basic_fq_h: list[float | None] | None = Field(
        None,
        description="List of historical earnings per share basic for the fiscal quarter",
    )
    earnings_publication_type_next_fy: float | None = Field(
        None, description="Earnings publication type for the next fiscal year"
    )
    earnings_per_share_forecast_next_fy: float | None = Field(
        None, description="Earnings per share forecast for the next fiscal year"
    )
    earnings_release_next_date_fy: float | None = Field(
        None, description="Earnings release date for the next fiscal year"
    )
    earnings_per_share_basic_fh: float | None = Field(
        None, description="Earnings per share basic for the fiscal half"
    )
    earnings_release_time_fq: float | None = Field(
        None, description="Earnings release time for the fiscal quarter"
    )
    earnings_release_calendar_date_fq: float | None = Field(
        None, description="Earnings release calendar date for the fiscal quarter"
    )
    earnings_per_share_fq_h: list[float | None] | None = Field(
        None, description="List of historical earnings per share for the fiscal quarter"
    )
    earnings_per_share_forecast_fy: float | None = Field(
        None, description="Earnings per share forecast for the fiscal year"
    )
    earnings_per_share_diluted_fq: float | None = Field(
        None, description="Earnings per share diluted for the fiscal quarter"
    )
    earnings_release_date_fq_h: list[float | None] | None = Field(
        None,
        description="List of historical earnings release dates for the fiscal quarter",
    )
    earnings_per_share_forecast_next_fh: float | None = Field(
        None, description="Earnings per share forecast for the next fiscal half"
    )
    earnings_release_next_time: float | None = Field(
        None, description="Earnings release time for the next period"
    )
    earnings_release_next_date_fq: float | None = Field(
        None, description="Earnings release date for the next fiscal quarter"
    )
    earnings_release_calendar_date: float | None = Field(
        None, description="Earnings release calendar date"
    )
    earnings_per_share_diluted_fh: float | None = Field(
        None, description="Earnings per share diluted for the fiscal half"
    )
    earnings_per_share_forecast_fq_h: list[float | None] | None = Field(
        None,
        description="List of historical earnings per share forecast for the fiscal quarter",
    )
    earnings_per_share_diluted_ttm: float | None = Field(
        None, description="Earnings per share diluted for the trailing twelve months"
    )
    earnings_release_time: float | None = Field(
        None, description="Earnings release time"
    )
    earnings_fiscal_period_fq: str | None = Field(
        None, description="Earnings fiscal period for the fiscal quarter"
    )
    earnings_release_next_trading_date_fq: float | None = Field(
        None, description="Earnings release next trading date for the fiscal quarter"
    )
    earnings_publication_type_fq: float | None = Field(
        None, description="Earnings publication type for the fiscal quarter"
    )
    earnings_per_share_diluted_fy: float | None = Field(
        None, description="Earnings per share diluted for the fiscal year"
    )
    earnings_per_share_basic_fq: float | None = Field(
        None, description="Earnings per share basic for the fiscal quarter"
    )
    earnings_per_share_diluted_fq_h: list[float | None] | None = Field(
        None,
        description="List of historical earnings per share diluted for the fiscal quarter",
    )
    earnings_per_share_ttm: float | None = Field(
        None, description="Earnings per share for the trailing twelve months"
    )
    earnings_release_date_fq: float | None = Field(
        None, description="Earnings release date for the fiscal quarter"
    )
    earnings_release_date_fy_h: list[float | None] | None = Field(
        None,
        description="List of historical earnings release dates for the fiscal year",
    )
    earnings_per_share_forecast_fy_h: list[float | None] | None = Field(
        None,
        description="List of historical earnings per share forecast for the fiscal year",
    )
    earnings_release_next_calendar_date_fq: float | None = Field(
        None, description="Earnings release next calendar date for the fiscal quarter"
    )
    earnings_release_next_time_fq: float | None = Field(
        None, description="Earnings release next time for the fiscal quarter"
    )
    earnings_per_share_fy: float | None = Field(
        None, description="Earnings per share for the fiscal year"
    )
    earnings_per_share_basic_fy: float | None = Field(
        None, description="Earnings per share basic for the fiscal year"
    )
    earnings_publication_type_next_fq: float | None = Field(
        None, description="Earnings publication type for the fiscal quarter"
    )
    earnings_per_share_basic_fy_h: list[float | None] | None = Field(
        None,
        description="List of historical earnings per share basic for the fiscal year",
    )
    earnings_per_share_fh: float | None = Field(
        None, description="Earnings per share for the fiscal half"
    )
    earnings_release_next_trading_date_fy: float | None = Field(
        None, description="Earnings release next trading date for the fiscal year"
    )
    earnings_release_trading_date_fy: float | None = Field(
        None, description="Earnings release trading date for the fiscal year"
    )
    earnings_per_share_forecast_fq: float | None = Field(
        None, description="Earnings per share forecast for the fiscal quarter"
    )
    earnings_fiscal_period_fy_h: list[str] | None = Field(
        None,
        description="List of historical earnings fiscal periods for the fiscal year",
    )
    earnings_release_next_calendar_date: float | None = Field(
        None, description="Earnings release next calendar date for the fiscal year"
    )
    earnings_publication_type_fq_h: list[float | None] | None = Field(
        None,
        description="List of historical earnings publication types for the fiscal quarter",
    )
    earnings_fq_h: list[dict] | None = Field(
        None, description="List of historical earnings for the fiscal quarter"
    )
    earnings_release_date_h: list[float | None] | None = Field(
        None,
        description="List of historical earnings release dates for the fiscal quarter",
    )
    earnings_fiscal_period_fq_h: list[str] | None = Field(
        None,
        description="List of historical earnings fiscal periods for the fiscal quarter",
    )
    earnings_per_share_diluted_ttm_h: list[float | None] | None = Field(
        None,
        description="List of historical earnings per share diluted for the trailing twelve months",
    )
    earnings_per_share_fy_h: list[float | None] | None = Field(
        None, description="List of historical earnings per share for the fiscal year"
    )
    earnings_fiscal_period_fy: str | None = Field(
        None, description="Earnings fiscal period for the fiscal year"
    )
    earnings_release_date_fy: float | None = Field(
        None, description="Earnings release date for the fiscal year"
    )
    earnings_publication_type_fy: float | None = Field(
        None, description="Earnings publication type for the fiscal year"
    )
    earnings_fy_h: list[dict] | None = Field(
        None, description="List of historical earnings for the fiscal year"
    )
    earnings_release_trading_date_fq: float | None = Field(
        None, description="Earnings release trading date for the fiscal quarter"
    )
    earnings_per_share_diluted_fy_h: list[float | None] | None = Field(
        None,
        description="List of historical earnings per share diluted for the fiscal year",
    )
    earnings_publication_type_fy_h: list[float | None] | None = Field(
        None,
        description="List of historical earnings publication types for the fiscal year",
    )


class MarketData(BaseModel):
    """Contains market data, pricing, and volume information."""

    model_config = ConfigDict(extra="forbid")

    # Pricing
    ask: float | None = Field(None, description="Current ask price")
    ask_size: int | None = Field(None, description="Current ask size")
    bid: float | None = Field(None, description="Current bid price")
    bid_size: int | None = Field(None, description="Current bid size")
    high_price: float | None = Field(
        None, description="High price for the current session"
    )
    low_price: float | None = Field(
        None, description="Low price for the current session"
    )
    open_price: float | None = Field(
        None, description="Open price for the current session"
    )
    prev_close_price: float | None = Field(None, description="Previous closing price")
    price_52_week_high: float | None = Field(None, description="The 52-week high price")
    price_52_week_low: float | None = Field(None, description="The 52-week low price")

    # Volume
    volume: int | None = Field(None, description="Current session's volume")
    average_volume: float | None = Field(None, description="Average trading volume")

    # Volatility
    beta_1_year: float | None = Field(None, description="1-year beta")
    beta_3_year: float | None = Field(None, description="3-year beta")

    # Shares
    float_shares_outstanding: float | None = Field(
        None, description="Float shares outstanding"
    )
    total_shares_outstanding: float | None = Field(
        None, description="Total shares outstanding"
    )


class Ratios(BaseModel):
    """Key financial and performance ratios."""

    model_config = ConfigDict(extra="forbid")

    # Asset & Inventory Turnover
    asset_turnover_current: float | None = Field(
        None, description="Asset turnover for the current period"
    )
    asset_turnover_fy: float | None = Field(
        None, description="Asset turnover for the fiscal year"
    )
    invent_turnover_current: float | None = Field(
        None, description="Inventory turnover for the current period"
    )
    invent_turnover_fy: float | None = Field(
        None, description="Inventory turnover for the fiscal year"
    )

    # Profitability Ratios
    return_on_assets_fy: float | None = Field(
        None, description="Return on assets for the fiscal year"
    )
    return_on_equity_fy: float | None = Field(
        None, description="Return on equity for the fiscal year"
    )
    return_on_invested_capital_fy: float | None = Field(
        None, description="Return on invested capital for the fiscal year"
    )

    # Liquidity Ratios
    current_ratio_fy: float | None = Field(
        None, description="Current ratio for the fiscal year"
    )
    quick_ratio_fy: float | None = Field(
        None, description="Quick ratio for the fiscal year"
    )

    # Others
    piotroski_f_score_fy: float | None = Field(
        None, description="Piotroski F-Score for the fiscal year"
    )
    altman_z_score_ttm: float | None = Field(
        None, description="Altman Z-Score for the trailing twelve months"
    )


class Revenue(BaseModel):
    """
    Holds current and historical revenue data, structured by fiscal period.
    """

    model_config = ConfigDict(extra="forbid")

    # Current Snapshot Metrics
    last_annual_revenue: float | None = Field(
        None, description="Last reported annual revenue"
    )
    total_revenue_ttm: float | None = Field(
        None, description="Total revenue for the trailing twelve months"
    )
    price_to_revenue_ttm: float | None = Field(
        None, description="Price to revenue ratio for the trailing twelve months"
    )
    revenue_per_employee: float | None = Field(
        None, description="Most recent revenue per employee"
    )
    top_revenue_country_code: str | None = Field(
        None, description="Country code with the highest revenue contribution"
    )

    # Revenue Reports (Actual vs. Estimate)
    historical_quarterly_reports: list | None = Field(
        None, description="Historical quarterly revenue reports (actual vs. estimate)"
    )
    historical_yearly_reports: list | None = Field(
        None, description="Historical yearly revenue reports (actual vs. estimate)"
    )

    # Total Revenue History
    historical_quarterly_total: list | None = Field(
        None, description="List of historical total revenue for fiscal quarters"
    )
    historical_yearly_total: list | None = Field(
        None, description="List of historical total revenue for fiscal years"
    )

    # Revenue Per Share History
    historical_quarterly_per_share: list | None = Field(
        None, description="List of historical revenue per share for fiscal quarters"
    )
    historical_yearly_per_share: list | None = Field(
        None, description="List of historical revenue per share for fiscal years"
    )

    # Revenue Forecast History
    historical_quarterly_forecast: list | None = Field(
        None, description="Historical revenue forecasts made for fiscal quarters"
    )
    historical_yearly_forecast: list | None = Field(
        None, description="Historical revenue forecasts made for fiscal years"
    )

    # Segment Revenue History
    historical_by_business_segment: list | None = Field(
        None, description="Historical revenue breakdown by business segment"
    )
    historical_by_region_segment: list | None = Field(
        None, description="Historical revenue breakdown by geographic region"
    )


class ShareDetails(BaseModel):
    """Information about the company's share structure."""

    model_config = ConfigDict(extra="forbid")

    basic_shares_outstanding_fy: float | None = Field(
        None, description="Basic shares outstanding for the fiscal year."
    )
    basic_shares_outstanding_fq: float | None = Field(
        None, description="Basic shares outstanding for the fiscal quarter."
    )
    diluted_shares_outstanding_fy: float | None = Field(
        None, description="Diluted shares outstanding for the fiscal year."
    )
    diluted_shares_outstanding_fq: float | None = Field(
        None, description="Diluted shares outstanding for the fiscal quarter."
    )

    book_value_per_share_fy: float | None = Field(
        None, description="Book value per share for the fiscal year."
    )
    book_value_per_share_fq: float | None = Field(
        None, description="Book value per share for the fiscal quarter."
    )
    book_tangible_per_share_fy: float | None = Field(
        None, description="Tangible book value per share for the fiscal year."
    )
    book_tangible_per_share_fq: float | None = Field(
        None, description="Tangible book value per share for the fiscal quarter."
    )
    basic_shares_outstanding_fq_h: list[float | None] | None = Field(
        None, description="Historical basic shares outstanding, fiscal quarter"
    )
    basic_shares_outstanding_fy_h: list[float | None] | None = Field(
        None, description="Historical basic shares outstanding, fiscal year"
    )
    book_per_share_fq: float | None = Field(
        None, description="Book value per share, fiscal quarter"
    )
    book_per_share_fy: float | None = Field(
        None, description="Book value per share, fiscal year"
    )
    book_tangible_per_share_current: float | None = Field(
        None, description="Tangible book value per share, current"
    )
    book_tangible_per_share_fq_h: list[float | None] | None = Field(
        None,
        description="Historical tangible book value per share, fiscal quarter",
    )
    book_tangible_per_share_fy_h: list[float | None] | None = Field(
        None, description="Historical tangible book value per share, fiscal year"
    )
    book_value_per_share_current: float | None = Field(
        None, description="Book value per share, current"
    )
    book_value_per_share_fq_h: list[float | None] | None = Field(
        None, description="Historical book value per share, fiscal quarter"
    )
    book_value_per_share_fy_h: list[float | None] | None = Field(
        None, description="Historical book value per share, fiscal year"
    )
    diluted_shares_outstanding_fq_h: list[float | None] | None = Field(
        None, description="Historical diluted shares outstanding, fiscal quarter"
    )
    diluted_shares_outstanding_fy_h: list[float | None] | None = Field(
        None, description="Historical diluted shares outstanding, fiscal year"
    )
    float_shares_outstanding_current: float | None = Field(
        None, description="Float shares outstanding, current"
    )
    float_shares_outstanding_fy: float | None = Field(
        None, description="Float shares outstanding, fiscal year"
    )
    float_shares_outstanding_fy_h: list[float | None] | None = Field(
        None, description="Historical float shares outstanding, fiscal year"
    )
    total_shares_outstanding_calculated: float | None = Field(
        None, description="Total shares outstanding (calculated)"
    )
    total_shares_outstanding_current: float | None = Field(
        None, description="Total shares outstanding, current"
    )
    total_shares_outstanding_fq: float | None = Field(
        None, description="Total shares outstanding, fiscal quarter"
    )
    total_shares_outstanding_fundamental: float | None = Field(
        None, description="Total shares outstanding (from fundamentals)"
    )
    total_shares_outstanding_fy: float | None = Field(
        None, description="Total shares outstanding, fiscal year"
    )
    total_shares_outstanding_fq_h: list[float | None] | None = Field(
        None, description="Historical total shares outstanding, fiscal quarter"
    )
    total_shares_outstanding_fy_h: list[float | None] | None = Field(
        None, description="Historical total shares outstanding, fiscal year"
    )
    working_capital_per_share_current: float | None = Field(
        None, description="Working capital per share, current"
    )
    working_capital_per_share_fq: float | None = Field(
        None, description="Working capital per share, fiscal quarter"
    )
    working_capital_per_share_fy: float | None = Field(
        None, description="Working capital per share, fiscal year"
    )
    working_capital_per_share_fq_h: list[float | None] | None = Field(
        None, description="Historical working capital per share, fiscal quarter"
    )
    working_capital_per_share_fy_h: list[float | None] | None = Field(
        None, description="Historical working capital per share, fiscal year"
    )
