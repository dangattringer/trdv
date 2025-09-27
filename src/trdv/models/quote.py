from __future__ import annotations
from typing import Any
from pydantic import BaseModel, Field
from datetime import datetime


class QuoteData(BaseModel):
    """
    Represents comprehensive quote, fundamental, and descriptive data for a trading symbol.
    This model is designed to parse the detailed JSON blob from the data endpoint.
    """

    # ==========================================================================
    # Section 1: Core Symbol & Exchange Information
    # ==========================================================================
    symbol: str
    short_name: str
    description: str
    short_description: str = Field(..., alias="short-description")
    local_description: str
    exchange: str
    listed_exchange: str
    exchange_listed_name: str
    country: str
    country_code: str
    type: str
    typespecs: list[str]
    timezone: str
    pro_name: str
    original_name: str
    base_name: list[str]
    symbol_primary_listing: str = Field(..., alias="symbol_primary_listing")
    symbol_proname: str = Field(..., alias="symbol-proname")
    pro_perm: str
    language: str
    is_tradable: bool | None = None
    is_replayable: bool | None = None
    has_adjustment: bool | None = None
    has_intraday: bool | None = None
    has_no_volume: bool = Field(..., alias="has-no-volume")
    has_options: bool | None = None
    has_bonds: bool | None = None
    fractional: bool | None = None
    is_primary_listing: bool = Field(..., alias="is-primary-listing")
    is_tickbars_available: bool = Field(..., alias="is-tickbars-available")
    provider_id: str
    source_id: str
    source_logoid: str = Field(..., alias="source-logoid")
    currency_logoid: str = Field(..., alias="currency-logoid")
    logoid: str | None = None
    mic: str
    cik_code: int = Field(..., alias="cik-code")
    figi: Figi
    isin: str
    isin_displayed: str = Field(..., alias="isin-displayed")
    cusip: str
    source2: Source2
    broker_names: dict[str, str]
    currency_code: str
    currency_id: str
    fundamental_currency_code: str
    perms: Perms

    # ==========================================================================
    # Section 2: Real-time & Quote Data
    # ==========================================================================
    update_mode: str
    current_session: str
    trade_loaded: bool
    hub_rt_loaded: bool
    lp: float
    lp_time: datetime
    ch: float
    chp: float
    rch: float | None
    rchp: float | None
    rtc: Any | None
    rtc_time: Any | None
    bid: float
    ask: float
    bid_size: float
    ask_size: float
    volume: int
    average_volume: float
    open_price: float
    high_price: float
    low_price: float
    prev_close_price: float
    regular_close: float
    regular_close_time: datetime
    all_time_high: float
    all_time_low: float
    all_time_high_day: datetime
    all_time_low_day: datetime
    all_time_open: float
    price_52_week_high: float
    price_52_week_low: float
    price_percent_change_1_week: float
    price_percent_change_52_week: float
    daily_bar: BarData = Field(..., alias="daily-bar")
    prev_daily_bar: BarData = Field(..., alias="prev-daily-bar")
    minute_bar: BarData | None = Field(None, alias="minute-bar")
    trade: TradeData | None = None
    market_status: MarketStatus = Field(..., alias="market-status")

    # ==========================================================================
    # Section 3: Session & Technical Details
    # ==========================================================================
    session_id: str = Field(..., alias="session-id")
    subsession_id: str
    session_display: str | None = None
    session_regular: str = Field(..., alias="session-regular")
    session_regular_display: str = Field(..., alias="session-regular-display")
    session_regular_correction: str = Field(..., alias="session-regular-correction")
    session_extended: str = Field(..., alias="session-extended")
    session_extended_display: str = Field(..., alias="session-extended-display")
    session_extended_correction: str = Field(..., alias="session-extended-correction")
    session_premarket: str = Field(..., alias="session-premarket")
    session_premarket_correction: str = Field(..., alias="session-premarket-correction")
    session_postmarket: str = Field(..., alias="session-postmarket")
    session_postmarket_correction: str = Field(
        ..., alias="session-postmarket-correction"
    )
    session_holidays: str
    subsessions: list[Subsession]
    pricescale: int
    minmov: int
    minmovement: int
    minmove2: int
    minmovement2: int
    pointvalue: int
    variable_tick_size: str = Field(..., alias="variable-tick-size")
    first_bar_time_1d: datetime | None
    first_bar_time_1m: datetime | None
    first_bar_time_1s: datetime | None
    trading_by: str = Field(..., alias="trading-by")
    visible_plots_set: str = Field(..., alias="visible-plots-set")
    allowed_adjustment: str

    # ==========================================================================
    # Section 4: Company Profile & Fundamental Overview
    # ==========================================================================
    business_description: str
    ceo: str
    web_site_url: str
    industry: str
    sector: str
    number_of_employees: int
    number_of_shareholders: int
    location: str
    popularity: int
    market_cap_basic: float
    market_cap_calc: float
    enterprise_value_current: float
    total_shares_outstanding: float
    total_shares_outstanding_current: float
    total_shares_outstanding_calculated: float
    float_shares_outstanding: float
    beta_1_year: float
    beta_3_year: float
    beta_5_year: float
    recommendation_mark: float
    recommendation_total: int
    recommendation_buy: int
    recommendation_over: int
    recommendation_hold: int
    recommendation_under: int
    recommendation_sell: int
    price_target_average: float | None
    price_target_high: float | None
    price_target_low: float | None
    price_target_median: float | None
    earnings_release_date: datetime | None
    earnings_release_next_date: datetime | None
    earnings_per_share_ttm: float
    earnings_per_share_basic_ttm: float
    earnings_per_share_diluted_ttm: float
    last_annual_eps: float
    last_annual_revenue: float
    total_revenue: float
    dividends_yield_current: float
    return_on_equity: float
    return_on_assets: float
    price_earnings_growth_ttm: float
    price_book_ratio: float
    price_sales_ratio: float
    gross_margin: float
    net_margin: float
    operating_margin: float
    quick_ratio: float
    current_ratio: float
    debt_to_equity: float

    # ==========================================================================
    # Section 5: Nested & Complex Fundamental Data Structures
    # ==========================================================================
    options_info: OptionsInfo | None = Field(None, alias="options-info")
    rates_fy: Rates
    rates_ttm: Rates
    rates_mc: Rates
    rates_fq: Rates
    rates_cf: Rates
    rates_pt: Rates
    rates_earnings_fy: Rates
    rates_earnings_next_fq: Rates
    revenues_fy_h: list[FinancialReport]
    revenues_fq_h: list[FinancialReport]
    earnings_fy_h: list[FinancialReport]
    earnings_fq_h: list[FinancialReport]
    revenue_seg_by_business_h: list[RevenueBySegment]
    revenue_seg_by_region_h: list[RevenueBySegment]

    # ==========================================================================
    # Section 6: Fundamental & Other Data Points
    # NOTE: Most of these are optional as they depend on asset type and data availability
    # ==========================================================================
    accum_deprec_buildings_fy_h: list[float | None]
    accum_deprec_comp_soft_fy_h: list[float | None]
    accum_deprec_construction_fy_h: list[float | None]
    accum_deprec_land_fy_h: list[float | None]
    accum_deprec_leased_prop_fy_h: list[float | None]
    accum_deprec_leases_fy_h: list[float | None]
    accum_deprec_machinery_fy_h: list[float | None]
    accum_deprec_other_fy_h: list[float | None]
    accum_deprec_other_intang_fy: float | None
    accum_deprec_other_intang_fy_h: list[float | None]
    accum_deprec_total_fq: float | None
    accum_deprec_total_fq_h: list[float | None]
    accum_deprec_total_fy: float | None
    accum_deprec_total_fy_h: list[float | None]
    accum_deprec_trans_equip_fy_h: list[float | None]
    accrued_expenses_fy: float | None
    accrued_expenses_fy_h: list[float | None]
    accrued_payroll_fq: float | None
    accrued_payroll_fq_h: list[float | None]
    accrued_payroll_fy: float | None
    accrued_payroll_fy_h: list[float | None]
    accounts_payable_fq: float | None
    accounts_payable_fq_h: list[float | None]
    accounts_payable_fy: float | None
    accounts_payable_fy_h: list[float | None]
    accounts_receivables_gross_fy: float | None
    accounts_receivables_gross_fy_h: list[float | None]
    accounts_receivables_net_fq: float | None
    accounts_receivables_net_fq_h: list[float | None]
    accounts_receivables_net_fy: float | None
    additional_paid_in_capital_fq: float | None
    additional_paid_in_capital_fq_h: list[float | None]
    additional_paid_in_capital_fy: float | None
    additional_paid_in_capital_fy_h: list[float | None]
    after_tax_margin: float | None
    after_tax_other_income_fq: float | None
    after_tax_other_income_fq_h: list[float | None]
    after_tax_other_income_fy: float | None
    after_tax_other_income_fy_h: list[float | None]
    after_tax_other_income_ttm: float | None
    altman_z_score_ttm: float | None
    amortization_fq_h: list[float | None]
    amortization_fy_h: list[float | None]
    amortization_of_deferred_charges_fy: float | None
    amortization_of_deferred_charges_fy_h: list[float | None]
    amortization_of_intangibles_fy: float | None
    amortization_of_intangibles_fy_h: list[float | None]
    asset_turnover_current: float | None
    asset_turnover_fq: float | None
    asset_turnover_fq_h: list[float | None]
    asset_turnover_fy: float | None
    asset_turnover_fy_h: list[float | None]
    basic_shares_outstanding_fq: float | None
    basic_shares_outstanding_fq_h: list[float | None]
    basic_shares_outstanding_fy: float | None
    basic_shares_outstanding_fy_h: list[float | None]
    book_per_share_fq: float | None
    book_per_share_fy: float | None
    book_tangible_per_share_current: float | None
    book_tangible_per_share_fq: float | None
    book_tangible_per_share_fq_h: list[float | None]
    book_tangible_per_share_fy: float | None
    book_tangible_per_share_fy_h: list[float | None]
    book_value_per_share_fq: float | None
    book_value_per_share_fq_h: list[float | None]
    book_value_per_share_fy: float | None
    book_value_per_share_fy_h: list[float | None]
    capital_expenditures_fh: float | None
    capital_expenditures_fixed_assets_fq: float | None
    capital_expenditures_fixed_assets_fq_h: list[float | None]
    capital_expenditures_fixed_assets_fy: float | None
    capital_expenditures_fixed_assets_fy_h: list[float | None]
    capital_expenditures_fixed_assets_ttm: float | None
    capital_expenditures_fq: float | None
    capital_expenditures_fq_h: list[float | None]
    capital_expenditures_fy: float | None
    capital_expenditures_fy_h: list[float | None]
    capital_expenditures_other_assets_fq: float | None
    capital_expenditures_other_assets_fq_h: list[float | None]
    capital_expenditures_other_assets_fy: float | None
    capital_expenditures_other_assets_fy_h: list[float | None]
    capital_expenditures_other_assets_ttm: float | None
    capital_expenditures_ttm: float | None
    capital_expenditures_unchanged_fq: float | None
    capital_expenditures_unchanged_fq_h: list[float | None]
    capital_expenditures_unchanged_fy: float | None
    capital_expenditures_unchanged_fy_h: list[float | None]
    capital_expenditures_unchanged_ttm: float | None
    capital_expenditures_unchanged_ttm_h: list[float | None]
    capital_lease_obligations_fq: float | None
    capital_lease_obligations_fq_h: list[float | None]
    capital_lease_obligations_fy: float | None
    capital_lease_obligations_fy_h: list[float | None]
    capital_operating_lease_obligations_fq: float | None
    capital_operating_lease_obligations_fq_h: list[float | None]
    capital_operating_lease_obligations_fy: float | None
    capital_operating_lease_obligations_fy_h: list[float | None]
    capex_per_share_current: float | None
    capex_per_share_fq: float | None
    capex_per_share_fq_h: list[float | None]
    capex_per_share_fy: float | None
    capex_per_share_fy_h: list[float | None]
    capex_per_share_ttm: float | None
    cash_f_financing_activities_fh: float | None
    cash_f_financing_activities_fq: float | None
    cash_f_financing_activities_fq_h: list[float | None]
    cash_f_financing_activities_fy: float | None
    cash_f_financing_activities_fy_h: list[float | None]
    cash_f_financing_activities_ttm: float | None
    cash_f_investing_activities_fh: float | None
    cash_f_investing_activities_fq: float | None
    cash_f_investing_activities_fq_h: list[float | None]
    cash_f_investing_activities_fy: float | None
    cash_f_investing_activities_fy_h: list[float | None]
    cash_f_investing_activities_ttm: float | None
    cash_f_operating_activities_fh: float | None
    cash_f_operating_activities_fq: float | None
    cash_f_operating_activities_fq_h: list[float | None]
    cash_f_operating_activities_fy: float | None
    cash_f_operating_activities_fy_h: list[float | None]
    cash_f_operating_activities_ttm: float | None
    cash_flow_deferred_taxes_fq: float | None
    cash_flow_deferred_taxes_fq_h: list[float | None]
    cash_flow_deferred_taxes_fy: float | None
    cash_flow_deferred_taxes_fy_h: list[float | None]
    cash_flow_deferred_taxes_ttm: float | None
    cash_flow_deprecation_n_amortization_fq: float | None
    cash_flow_deprecation_n_amortization_fq_h: list[float | None]
    cash_flow_deprecation_n_amortization_fy: float | None
    cash_flow_deprecation_n_amortization_fy_h: list[float | None]
    cash_flow_deprecation_n_amortization_ttm: float | None
    cash_n_equivalents_fq: float | None
    cash_n_equivalents_fq_h: list[float | None]
    cash_n_equivalents_fy: float | None
    cash_n_equivalents_fy_h: list[float | None]
    cash_n_short_term_invest_fq: float | None
    cash_n_short_term_invest_fq_h: list[float | None]
    cash_n_short_term_invest_fy: float | None
    cash_n_short_term_invest_fy_h: list[float | None]
    cash_per_share_fq: float | None
    cash_per_share_fq_h: list[float | None]
    cash_per_share_fy: float | None
    cash_per_share_fy_h: list[float | None]
    change_in_accounts_payable_fq: float | None
    change_in_accounts_payable_fq_h: list[float | None]
    change_in_accounts_payable_fy: float | None
    change_in_accounts_payable_fy_h: list[float | None]
    change_in_accounts_payable_ttm: float | None
    change_in_accounts_receivable_fq: float | None
    change_in_accounts_receivable_fq_h: list[float | None]
    change_in_accounts_receivable_fy: float | None
    change_in_accounts_receivable_fy_h: list[float | None]
    change_in_accounts_receivable_ttm: float | None
    change_in_accrued_expenses_fq: float | None
    change_in_accrued_expenses_fq_h: list[float | None]
    change_in_accrued_expenses_fy: float | None
    change_in_accrued_expenses_ttm: float | None
    change_in_inventories_fq: float | None
    change_in_inventories_fq_h: list[float | None]
    change_in_inventories_fy: float | None
    change_in_inventories_ttm: float | None
    change_in_other_assets_fq: float | None
    change_in_other_assets_fq_h: list[float | None]
    change_in_other_assets_fy: float | None
    change_in_other_assets_ttm: float | None
    change_in_taxes_payable_fq_h: list[Any | None]
    change_in_taxes_payable_fy_h: list[Any | None]
    changes_in_working_capital_fq: float | None
    changes_in_working_capital_fq_h: list[float | None]
    changes_in_working_capital_fy: float | None
    changes_in_working_capital_fy_h: list[float | None]
    changes_in_working_capital_ttm: float | None
    common_dividends_cash_flow_fq: float | None
    common_dividends_cash_flow_fq_h: list[float | None]
    common_dividends_cash_flow_fy: float | None
    common_dividends_cash_flow_fy_h: list[float | None]
    common_dividends_cash_flow_ttm: float | None
    common_equity_total_fq: float | None
    common_equity_total_fq_h: list[float | None]
    common_equity_total_fy: float | None
    common_equity_total_fy_h: list[float | None]
    common_stock_par_fq: float | None
    common_stock_par_fq_h: list[float | None]
    common_stock_par_fy: float | None
    common_stock_par_fy_h: list[float | None]
    cost_of_goods_excl_dep_amort_fq: float | None
    cost_of_goods_excl_dep_amort_fq_h: list[float | None]
    cost_of_goods_excl_dep_amort_fy: float | None
    cost_of_goods_excl_dep_amort_fy_h: list[float | None]
    cost_of_goods_excl_dep_amort_ttm: float | None
    cost_of_goods_fq: float | None
    cost_of_goods_fq_h: list[float | None]
    cost_of_goods_fy: float | None
    cost_of_goods_fy_h: list[float | None]
    cost_of_goods_ttm: float | None
    country_code_fund: datetime | None
    country_fund: datetime | None
    current_port_debt_capital_leases_fq: float | None
    current_port_debt_capital_leases_fq_h: list[float | None]
    current_port_debt_capital_leases_fy: float | None
    current_port_debt_capital_leases_fy_h: list[float | None]
    current_ratio_current: float | None
    current_ratio_fq: float | None
    current_ratio_fq_h: list[float | None]
    current_ratio_fy: float | None
    current_ratio_fy_h: list[float | None]
    debt_to_asset_current: float | None
    debt_to_asset_fq: float | None
    debt_to_asset_fq_h: list[float | None]
    debt_to_asset_fy: float | None
    debt_to_asset_fy_h: list[float | None]
    debt_to_equity_current: float | None
    debt_to_equity_fq: float | None
    debt_to_equity_fq_h: list[float | None]
    debt_to_equity_fy: float | None
    debt_to_equity_fy_h: list[float | None]
    debt_to_revenue_fy: float | None
    debt_to_revenue_ttm: float | None
    deferred_charges_fq_h: list[Any | None]
    deferred_charges_fy_h: list[Any | None]
    deferred_income_current_fq: float | None
    deferred_income_current_fq_h: list[float | None]
    deferred_income_current_fy: float | None
    deferred_income_current_fy_h: list[float | None]
    deferred_income_non_current_fq_h: list[Any | None]
    deferred_income_non_current_fy_h: list[Any | None]
    deferred_tax_assests_fq: float | None
    deferred_tax_assests_fq_h: list[float | None]
    deferred_tax_assests_fy: float | None
    deferred_tax_assests_fy_h: list[float | None]
    deferred_tax_liabilities_fq: float | None
    deferred_tax_liabilities_fq_h: list[float | None]
    deferred_tax_liabilities_fy: float | None
    deferred_tax_liabilities_fy_h: list[float | None]
    dep_amort_exp_income_s_fq: float | None
    dep_amort_exp_income_s_fq_h: list[float | None]
    dep_amort_exp_income_s_fy: float | None
    dep_amort_exp_income_s_fy_h: list[float | None]
    dep_amort_exp_income_s_ttm: float | None
    depreciation_depletion_fq_h: list[float | None]
    depreciation_depletion_fy_h: list[float | None]
    depreciation_fy: float | None
    depreciation_fy_h: list[float | None]
    diluted_net_income_fq: float | None
    diluted_net_income_fq_h: list[float | None]
    diluted_net_income_fy: float | None
    diluted_net_income_fy_h: list[float | None]
    diluted_net_income_ttm: float | None
    diluted_shares_outstanding_fq: float | None
    diluted_shares_outstanding_fq_h: list[float | None]
    diluted_shares_outstanding_fy: float | None
    diluted_shares_outstanding_fy_h: list[float | None]
    dilution_adjustment_fq: float | None
    dilution_adjustment_fq_h: list[float | None]
    dilution_adjustment_fy: float | None
    dilution_adjustment_fy_h: list[float | None]
    dilution_adjustment_ttm: float | None
    discontinued_operations_fq: float | None
    discontinued_operations_fq_h: list[float | None]
    discontinued_operations_fy: float | None
    discontinued_operations_fy_h: list[float | None]
    discontinued_operations_ttm: float | None
    dividend_amount_h: list[Any]
    dividend_ex_date_h: list[Any]
    dividend_payment_date_h: list[Any]
    dividend_payout_ratio_fq_h: list[float | None]
    dividend_payout_ratio_fy_h: list[Any | None]
    dividend_payout_ratio_ttm: float | None
    dividend_record_date_h: list[Any]
    dividend_type_h: list[Any]
    dividends_paid: float | None
    dividends_payable_fy: float | None
    dividends_payable_fy_h: list[float | None]
    dividends_per_share_fq: float | None
    dividends_yield_fq: float | None
    dividends_yield_fy: float | None
    dividends_yield_fy_h: list[float | None]
    documents: int | None
    doubtful_accounts_fy_h: list[Any | None]
    dps_common_stock_prim_issue_fh: float | None
    dps_common_stock_prim_issue_fq: float | None
    dps_common_stock_prim_issue_fq_h: list[float | None]
    dps_common_stock_prim_issue_fy: float | None
    dps_common_stock_prim_issue_fy_h: list[float | None]
    earnings_per_share_basic_fh: float | None
    earnings_per_share_basic_fq: float | None
    earnings_per_share_basic_fq_h: list[float | None]
    earnings_per_share_basic_fy: float | None
    earnings_per_share_basic_fy_h: list[float | None]
    earnings_per_share_diluted_fh: float | None
    earnings_per_share_diluted_fq: float | None
    earnings_per_share_diluted_fq_h: list[float | None]
    earnings_per_share_diluted_fy: float | None
    earnings_per_share_diluted_fy_h: list[float | None]
    earnings_per_share_fh: float | None
    earnings_per_share_forecast_fq: float | None
    earnings_per_share_forecast_fq_h: list[float | None]
    earnings_per_share_forecast_fy: float | None
    earnings_per_share_forecast_fy_h: list[float | None]
    earnings_per_share_forecast_next_fh: float | None
    earnings_per_share_forecast_next_fq: float | None
    earnings_per_share_forecast_next_fy: float | None
    earnings_per_share_fq: float | None
    earnings_per_share_fq_h: list[float | None]
    earnings_per_share_fy: float | None
    earnings_per_share_fy_h: list[float | None]
    earnings_publication_type_next_fy: int | None
    earnings_release_calendar_date: datetime | None
    earnings_release_calendar_date_fq: datetime | None
    earnings_release_date_fq_h: list[int | None]
    earnings_release_date_fy_h: list[int | None]
    earnings_release_next_calendar_date: datetime | None
    earnings_release_next_calendar_date_fq: datetime | None
    earnings_release_next_date_fq: datetime | None
    earnings_release_next_date_fy: datetime | None
    earnings_release_next_time: int | None
    earnings_release_next_time_fq: int | None
    earnings_release_next_trading_date_fq: datetime | None
    earnings_release_next_trading_date_fy: datetime | None
    earnings_release_trading_date_fy: datetime | None
    earnings_fiscal_period_fq: datetime | None
    earnings_fiscal_period_fq_h: list[datetime | None]
    earnings_fiscal_period_fy: datetime | None
    earnings_fiscal_period_fy_h: list[datetime | None]
    ebit_fq: float | None
    ebit_fq_h: list[float | None]
    ebit_fy: float | None
    ebit_fy_h: list[float | None]
    ebitda_fh: float | None
    ebitda_fq: float | None
    ebitda_fq_h: list[float | None]
    ebitda_fy: float | None
    ebitda_fy_h: list[float | None]
    ebitda_interst_cover_fy: float | None
    ebitda_interst_cover_ttm: float | None
    ebitda_less_capex_interst_cover_fy: float | None
    ebitda_less_capex_interst_cover_ttm: float | None
    ebitda_margin_fq: float | None
    ebitda_margin_fq_h: list[float | None]
    ebitda_margin_fy: float | None
    ebitda_margin_fy_h: list[float | None]
    ebitda_margin_ttm: float | None
    ebitda_per_employee_fy: float | None
    ebitda_per_share_fq: float | None
    ebitda_per_share_fq_h: list[float | None]
    ebitda_per_share_fy: float | None
    ebitda_per_share_fy_h: list[float | None]
    ebitda_per_share_ttm: float | None
    ebitda_ttm_h: list[float | None]
    ebit_per_share_fq: float | None
    ebit_per_share_fq_h: list[float | None]
    ebit_per_share_fy: float | None
    ebit_per_share_fy_h: list[float | None]
    ebit_per_share_ttm: float | None
    effective_interest_rate_on_debt_fy: float | None
    effective_interest_rate_on_debt_ttm: float | None
    enterprise_value_ebitda_fq_h: list[Any | None]
    enterprise_value_ebitda_fy_h: list[Any | None]
    enterprise_value_fq_h: list[float | None]
    enterprise_value_fy_h: list[float | None]
    eps_diluted_growth_percent_fq: float | None
    eps_diluted_growth_percent_fy: float | None
    equity_in_earnings_fq: float | None
    equity_in_earnings_fq_h: list[float | None]
    equity_in_earnings_fy: float | None
    equity_in_earnings_fy_h: list[float | None]
    equity_in_earnings_ttm: float | None
    exchange_ticker: datetime | None = Field(None, alias="exchange-ticker")
    exchange_traded: datetime | None = Field(None, alias="exchange-traded")
    exchange_traded_name: datetime | None
    fixed_assets_turnover_fq: float | None
    fixed_assets_turnover_fy: float | None
    float_shares_outstanding_fy: float | None
    float_shares_outstanding_fy_h: list[float | None]
    free_cash_flow_fh: float | None
    free_cash_flow_fq: float | None
    free_cash_flow_fq_h: list[float | None]
    free_cash_flow_fy: float | None
    free_cash_flow_fy_h: list[float | None]
    free_cash_flow_per_employee_fy: float | None
    free_cash_flow_per_share_fq: float | None
    free_cash_flow_per_share_fq_h: list[float | None]
    free_cash_flow_per_share_fy: float | None
    free_cash_flow_per_share_fy_h: list[float | None]
    free_cash_flow_per_share_ttm: float | None
    free_cash_flow_ttm_h: list[float | None]
    fund_view_mode: datetime | None
    funds_f_operations_fq: float | None
    funds_f_operations_fq_h: list[float | None]
    funds_f_operations_fy: float | None
    funds_f_operations_fy_h: list[float | None]
    funds_f_operations_ttm: float | None
    goodwill: float | None
    goodwill_amortization_fy_h: list[Any | None]
    goodwill_fq: float | None
    goodwill_fq_h: list[float | None]
    goodwill_fy: float | None
    goodwill_fy_h: list[float | None]
    goodwill_gross_fy: float | None
    goodwill_gross_fy_h: list[float | None]
    gross_margin_fq: float | None
    gross_margin_fq_h: list[float | None]
    gross_margin_fy: float | None
    gross_margin_fy_h: list[float | None]
    gross_margin_ttm: float | None
    gross_profit_fh: float | None
    gross_profit_fq: float | None
    gross_profit_fq_h: list[float | None]
    gross_profit_fy: float | None
    gross_profit_fy_h: list[float | None]
    gross_profit_ttm_h: list[float | None]
    group: datetime | None
    history_tag: datetime | None = Field(None, alias="history-tag")
    impairments_fy_h: list[Any | None]
    income_tax_credits_fy: float | None
    income_tax_credits_fy_h: list[float | None]
    income_tax_current_domestic_fy: float | None
    income_tax_current_domestic_fy_h: list[float | None]
    income_tax_current_foreign_fy: float | None
    income_tax_current_foreign_fy_h: list[float | None]
    income_tax_current_fy: float | None
    income_tax_current_fy_h: list[float | None]
    income_tax_deferred_domestic_fy: float | None
    income_tax_deferred_domestic_fy_h: list[float | None]
    income_tax_deferred_foreign_fy: float | None
    income_tax_deferred_foreign_fy_h: list[float | None]
    income_tax_deferred_fy: float | None
    income_tax_deferred_fy_h: list[float | None]
    income_tax_fq: float | None
    income_tax_fq_h: list[float | None]
    income_tax_fy: float | None
    income_tax_fy_h: list[float | None]
    income_tax_payable_fq_h: list[Any | None]
    income_tax_payable_fy_h: list[Any | None]
    intangibles_net_fq: float | None
    intangibles_net_fq_h: list[float | None]
    intangibles_net_fy: float | None
    intangibles_net_fy_h: list[float | None]
    interest_capitalized_fq: float | None
    interest_capitalized_fq_h: list[float | None]
    interest_capitalized_fy: float | None
    interest_capitalized_fy_h: list[float | None]
    interest_capitalized_ttm: float | None
    interest_expense_on_debt_fq: float | None
    interest_expense_on_debt_fq_h: list[float | None]
    interest_expense_on_debt_fy: float | None
    interest_expense_on_debt_ttm: float | None
    interst_cover_fy: float | None
    interst_cover_ttm: float | None
    invent_turnover_fq: float | None
    invent_turnover_fq_h: list[float | None]
    invent_turnover_fy: float | None
    invent_turnover_fy_h: list[float | None]
    inventory_finished_goods_fq: float | None
    inventory_finished_goods_fq_h: list[float | None]
    inventory_finished_goods_fy: float | None
    inventory_finished_goods_fy_h: list[float | None]
    inventory_progress_payments_fq: float | None
    inventory_progress_payments_fq_h: list[float | None]
    inventory_progress_payments_fy: float | None
    inventory_progress_payments_fy_h: list[float | None]
    inventory_raw_materials_fq: float | None
    inventory_raw_materials_fq_h: list[float | None]
    inventory_raw_materials_fy: float | None
    inventory_raw_materials_fy_h: list[float | None]
    inventory_work_in_progress_fq: float | None
    inventory_work_in_progress_fq_h: list[float | None]
    inventory_work_in_progress_fy: float | None
    inventory_work_in_progress_fy_h: list[float | None]
    invested_capital_fy: float | None
    investments_in_unconcsolidate_fq: float | None
    investments_in_unconcsolidate_fq_h: list[float | None]
    investments_in_unconcsolidate_fy: float | None
    investments_in_unconcsolidate_fy_h: list[float | None]
    issuance_of_debt_net_fq: float | None
    issuance_of_debt_net_fq_h: list[float | None]
    issuance_of_debt_net_fy: float | None
    issuance_of_debt_net_fy_h: list[float | None]
    issuance_of_debt_net_ttm: float | None
    issuance_of_long_term_debt_fq: float | None
    issuance_of_long_term_debt_fq_h: list[float | None]
    issuance_of_long_term_debt_fy: float | None
    issuance_of_long_term_debt_fy_h: list[float | None]
    issuance_of_long_term_debt_ttm: float | None
    issuance_of_other_debt_fq_h: list[Any | None]
    issuance_of_other_debt_fy_h: list[Any | None]
    issuance_of_short_term_debt_fq: float | None
    issuance_of_short_term_debt_fq_h: list[float | None]
    issuance_of_short_term_debt_fy: float | None
    issuance_of_short_term_debt_fy_h: list[float | None]
    issuance_of_short_term_debt_ttm: float | None
    issuance_of_stock_net_fq: float | None
    issuance_of_stock_net_fq_h: list[float | None]
    issuance_of_stock_net_fy: float | None
    issuance_of_stock_net_fy_h: list[float | None]
    issuance_of_stock_net_ttm: float | None
    kind_delay: int | None = Field(None, alias="kind-delay")
    legal_claim_expense_fy_h: list[Any | None]
    long_term_debt_excl_capital_lease_fq: float | None
    long_term_debt_excl_capital_lease_fq_h: list[float | None]
    long_term_debt_excl_capital_lease_fy: float | None
    long_term_debt_excl_capital_lease_fy_h: list[float | None]
    long_term_debt_fq: float | None
    long_term_debt_fq_h: list[float | None]
    long_term_debt_fy: float | None
    long_term_debt_fy_h: list[float | None]
    long_term_debt_to_assets_current: float | None
    long_term_debt_to_assets_fq: float | None
    long_term_debt_to_assets_fq_h: list[float | None]
    long_term_debt_to_assets_fy: float | None
    long_term_debt_to_assets_fy_h: list[float | None]
    long_term_debt_to_equity_current: float | None
    long_term_debt_to_equity_fq: float | None
    long_term_debt_to_equity_fq_h: list[float | None]
    long_term_debt_to_equity_fy: float | None
    long_term_debt_to_equity_fy_h: list[float | None]
    long_term_investments_fq: float | None
    long_term_investments_fq_h: list[float | None]
    long_term_investments_fy: float | None
    long_term_investments_fy_h: list[float | None]
    long_term_note_receivable_fq: float | None
    long_term_note_receivable_fq_h: list[float | None]
    long_term_note_receivable_fy: float | None
    long_term_note_receivable_fy_h: list[float | None]
    long_term_other_assets_total_fq: float | None
    long_term_other_assets_total_fq_h: list[float | None]
    long_term_other_assets_total_fy: float | None
    long_term_other_assets_total_fy_h: list[float | None]
    market_cap_basic_fq: float | None
    market_cap_basic_fq_h: list[float | None]
    market_cap_basic_fy: float | None
    market_cap_basic_fy_h: list[float | None]
    minority_interest_exp_fq: float | None
    minority_interest_exp_fq_h: list[float | None]
    minority_interest_exp_fy: float | None
    minority_interest_exp_fy_h: list[float | None]
    minority_interest_exp_ttm: float | None
    minority_interest_fq: float | None
    minority_interest_fq_h: list[float | None]
    minority_interest_fy: float | None
    minority_interest_fy_h: list[float | None]
    ncavps_ratio_current: float | None
    ncavps_ratio_fq: float | None
    ncavps_ratio_fq_h: list[float | None]
    ncavps_ratio_fy: float | None
    ncavps_ratio_fy_h: list[float | None]
    net_debt_fq: float | None
    net_debt_fq_h: list[float | None]
    net_debt_fy: float | None
    net_debt_fy_h: list[float | None]
    net_income_bef_disc_oper_fq: float | None
    net_income_bef_disc_oper_fq_h: list[float | None]
    net_income_bef_disc_oper_fy: float | None
    net_income_bef_disc_oper_fy_h: list[float | None]
    net_income_bef_disc_oper_ttm: float | None
    net_income_fh: float | None
    net_income_fq: float | None
    net_income_fq_h: list[float | None]
    net_income_fy: float | None
    net_income_fy_h: list[float | None]
    net_income_per_employee_fy: float | None
    net_income_starting_line_fq: float | None
    net_income_starting_line_fq_h: list[float | None]
    net_income_starting_line_fy: float | None
    net_income_starting_line_fy_h: list[float | None]
    net_income_starting_line_ttm: float | None
    net_income_ttm_h: list[float | None]
    net_margin_fq: float | None
    net_margin_fq_h: list[float | None]
    net_margin_fy: float | None
    net_margin_fy_h: list[float | None]
    net_margin_ttm: float | None
    news_langs: list[str] | None = Field(None, alias="news-langs")
    non_cash_items_fq: float | None
    non_cash_items_fq_h: list[float | None]
    non_cash_items_fy: float | None
    non_cash_items_fy_h: list[float | None]
    non_cash_items_ttm: float | None
    non_oper_income_fq: float | None
    non_oper_income_fq_h: list[float | None]
    non_oper_income_fy: float | None
    non_oper_income_fy_h: list[float | None]
    non_oper_interest_exp_fq: float | None
    non_oper_interest_exp_fq_h: list[float | None]
    non_oper_interest_exp_fy: float | None
    non_oper_interest_exp_fy_h: list[float | None]
    non_oper_interest_exp_ttm: float | None
    non_oper_interest_income_fq: float | None
    non_oper_interest_income_fq_h: list[float | None]
    non_oper_interest_income_fy: float | None
    non_oper_interest_income_fy_h: list[float | None]
    non_oper_interest_income_ttm: float | None
    notes_payable_short_term_debt_fy_h: list[Any | None]
    number_of_employees_fy: int | None
    number_of_shareholders_fy: int | None
    number_of_shareholders_fy_h: list[int | None]
    oper_income_fh: float | None
    oper_income_fq: float | None
    oper_income_fq_h: list[float | None]
    oper_income_fy: float | None
    oper_income_fy_h: list[float | None]
    oper_income_per_employee_fy: float | None
    operating_expenses_fq: float | None
    operating_expenses_fy: float | None
    operating_expenses_ttm: float | None
    operating_lease_liabilities_fq: float | None
    operating_lease_liabilities_fq_h: list[float | None]
    operating_lease_liabilities_fy: float | None
    operating_lease_liabilities_fy_h: list[float | None]
    operating_margin_fq: float | None
    operating_margin_fq_h: list[float | None]
    operating_margin_fy: float | None
    operating_margin_fy_h: list[float | None]
    other_common_equity_fq: float | None
    other_common_equity_fq_h: list[float | None]
    other_common_equity_fy: float | None
    other_common_equity_fy_h: list[float | None]
    other_current_assets_total_fq: float | None
    other_current_assets_total_fq_h: list[float | None]
    other_current_assets_total_fy: float | None
    other_current_assets_total_fy_h: list[float | None]
    other_current_liabilities_fq: float | None
    other_current_liabilities_fq_h: list[float | None]
    other_current_liabilities_fy: float | None
    other_current_liabilities_fy_h: list[float | None]
    other_exceptional_charges_fy_h: list[Any | None]
    other_financing_cash_flow_items_total_fq: float | None
    other_financing_cash_flow_items_total_fq_h: list[float | None]
    other_financing_cash_flow_items_total_fy: float | None
    other_financing_cash_flow_items_total_fy_h: list[float | None]
    other_financing_cash_flow_items_total_ttm: float | None
    other_financing_cash_flow_sources_fq: float | None
    other_financing_cash_flow_sources_fq_h: list[float | None]
    other_financing_cash_flow_sources_fy: float | None
    other_financing_cash_flow_sources_fy_h: list[float | None]
    other_financing_cash_flow_sources_ttm: float | None
    other_financing_cash_flow_uses_fq: float | None
    other_financing_cash_flow_uses_fq_h: list[float | None]
    other_financing_cash_flow_uses_fy: float | None
    other_financing_cash_flow_uses_fy_h: list[float | None]
    other_financing_cash_flow_uses_ttm: float | None
    other_income_fq: float | None
    other_income_fq_h: list[float | None]
    other_income_fy: float | None
    other_income_fy_h: list[float | None]
    other_income_ttm: float | None
    other_intangibles_gross_fy: float | None
    other_intangibles_gross_fy_h: list[float | None]
    other_intangibles_net_fq: float | None
    other_intangibles_net_fq_h: list[float | None]
    other_intangibles_net_fy: float | None
    other_intangibles_net_fy_h: list[float | None]
    other_investing_cash_flow_items_total_fq: float | None
    other_investing_cash_flow_items_total_fq_h: list[float | None]
    other_investing_cash_flow_items_total_fy: float | None
    other_investing_cash_flow_items_total_fy_h: list[float | None]
    other_investing_cash_flow_items_total_ttm: float | None
    other_investing_cash_flow_sources_fq: float | None
    other_investing_cash_flow_sources_fq_h: list[float | None]
    other_investing_cash_flow_sources_fy: float | None
    other_investing_cash_flow_sources_fy_h: list[float | None]
    other_investing_cash_flow_sources_ttm: float | None
    other_investing_cash_flow_uses_fq: float | None
    other_investing_cash_flow_uses_fq_h: list[float | None]
    other_investing_cash_flow_uses_fy: float | None
    other_investing_cash_flow_uses_fy_h: list[float | None]
    other_investing_cash_flow_uses_ttm: float | None
    other_investments_fq: float | None
    other_investments_fq_h: list[float | None]
    other_investments_fy: float | None
    other_investments_fy_h: list[float | None]
    other_liabilities_total_fq: float | None
    other_liabilities_total_fq_h: list[float | None]
    other_liabilities_total_fy: float | None
    other_liabilities_total_fy_h: list[float | None]
    other_oper_expense_total_fq: float | None
    other_oper_expense_total_fq_h: list[float | None]
    other_oper_expense_total_fy: float | None
    other_oper_expense_total_fy_h: list[float | None]
    other_oper_expense_total_ttm: float | None
    other_proceeds_from_stock_sales_fq: float | None
    other_proceeds_from_stock_sales_fq_h: list[float | None]
    other_proceeds_from_stock_sales_fy: float | None
    other_proceeds_from_stock_sales_fy_h: list[float | None]
    other_receivables_fq: float | None
    other_receivables_fq_h: list[float | None]
    other_receivables_fy: float | None
    other_receivables_fy_h: list[float | None]
    other_short_term_debt_fy: float | None
    other_short_term_debt_fy_h: list[float | None]
    paid_in_capital_fq: float | None
    paid_in_capital_fq_h: list[float | None]
    paid_in_capital_fy: float | None
    paid_in_capital_fy_h: list[float | None]
    ppe_gross_buildings_fy: float | None
    ppe_gross_buildings_fy_h: list[float | None]
    ppe_gross_comp_soft_fy: float | None
    ppe_gross_comp_soft_fy_h: list[float | None]
    ppe_gross_construction_fy: float | None
    ppe_gross_construction_fy_h: list[float | None]
    ppe_gross_land_fy_h: list[Any | None]
    ppe_gross_leased_prop_fy_h: list[Any | None]
    ppe_gross_leases_fy: float | None
    ppe_gross_leases_fy_h: list[float | None]
    ppe_gross_machinery_fy_h: list[Any | None]
    ppe_gross_other_fy: float | None
    ppe_gross_other_fy_h: list[float | None]
    ppe_gross_trans_equip_fy_h: list[Any | None]
    ppe_total_gross_fq: float | None
    ppe_total_gross_fq_h: list[float | None]
    ppe_total_gross_fy: float | None
    ppe_total_gross_fy_h: list[float | None]
    ppe_total_net_fq: float | None
    ppe_total_net_fq_h: list[float | None]
    ppe_total_net_fy: float | None
    ppe_total_net_fy_h: list[float | None]
    pre_tax_margin: float | None
    pre_tax_margin_current: float | None
    pre_tax_margin_fq: float | None
    pre_tax_margin_fq_h: list[float | None]
    pre_tax_margin_fy: float | None
    pre_tax_margin_fy_h: list[float | None]
    pre_tax_margin_ttm: float | None
    preferred_dividends_cash_flow_fq_h: list[Any | None]
    preferred_dividends_cash_flow_fy: float | None
    preferred_dividends_cash_flow_fy_h: list[float | None]
    preferred_dividends_cash_flow_ttm: float | None
    preferred_dividends_fq_h: list[Any | None]
    preferred_dividends_fy: float | None
    preferred_dividends_fy_h: list[float | None]
    preferred_stock_carrying_value_fq: float | None
    preferred_stock_carrying_value_fq_h: list[float | None]
    preferred_stock_carrying_value_fy: float | None
    preferred_stock_carrying_value_fy_h: list[float | None]
    prepaid_expenses_fq: float | None
    prepaid_expenses_fq_h: list[float | None]
    prepaid_expenses_fy: float | None
    prepaid_expenses_fy_h: list[float | None]
    pretax_equity_in_earnings_fq: float | None
    pretax_equity_in_earnings_fq_h: list[float | None]
    pretax_equity_in_earnings_fy: float | None
    pretax_equity_in_earnings_fy_h: list[float | None]
    pretax_equity_in_earnings_ttm: float | None
    pretax_income_fq: float | None
    pretax_income_fq_h: list[float | None]
    pretax_income_fy: float | None
    pretax_income_fy_h: list[float | None]
    price_annual_book: float | None
    price_annual_sales: float | None
    price_book_fq: float | None
    price_book_fq_h: list[float | None]
    price_book_fy_h: list[float | None]
    price_cash_flow_fq_h: list[Any | None]
    price_cash_flow_fy_h: list[Any | None]
    price_earnings_fq_h: list[Any | None]
    price_earnings_fy_h: list[Any | None]
    price_sales_fq: float | None
    price_sales_fq_h: list[float | None]
    price_sales_fy_h: list[float | None]
    proceeds_from_stock_options_fq: float | None
    proceeds_from_stock_options_fq_h: list[float | None]
    proceeds_from_stock_options_fy: float | None
    proceeds_from_stock_options_fy_h: list[float | None]
    provision_f_risks_fq: float | None
    provision_f_risks_fq_h: list[float | None]
    provision_f_risks_fy: float | None
    provision_f_risks_fy_h: list[float | None]
    purchase_of_business_fq: float | None
    purchase_of_business_fq_h: list[float | None]
    purchase_of_business_fy: float | None
    purchase_of_business_fy_h: list[float | None]
    purchase_of_business_ttm: float | None
    purchase_of_investments_fq: float | None
    purchase_of_investments_fq_h: list[float | None]
    purchase_of_investments_fy: float | None
    purchase_of_investments_ttm: float | None
    purchase_of_stock_fq: float | None
    purchase_of_stock_fq_h: list[float | None]
    purchase_of_stock_fy: float | None
    purchase_of_stock_fy_h: list[float | None]
    purchase_of_stock_ttm: float | None
    purchase_sale_business_fq: float | None
    purchase_sale_business_fq_h: list[float | None]
    purchase_sale_business_fy: float | None
    purchase_sale_business_fy_h: list[float | None]
    purchase_sale_business_ttm: float | None
    purchase_sale_investments_fq: float | None
    purchase_sale_investments_fq_h: list[float | None]
    purchase_sale_investments_fy: float | None
    purchase_sale_investments_fy_h: list[float | None]
    purchase_sale_investments_ttm: float | None
    quick_ratio_fq: float | None
    quick_ratio_fq_h: list[float | None]
    quick_ratio_fy: float | None
    quick_ratio_fy_h: list[float | None]
    receivables_turnover_fy: float | None
    reduction_of_long_term_debt_fq: float | None
    reduction_of_long_term_debt_fq_h: list[float | None]
    reduction_of_long_term_debt_fy: float | None
    reduction_of_long_term_debt_fy_h: list[float | None]
    reduction_of_long_term_debt_ttm: float | None
    region: datetime | None
    research_and_dev_fh: float | None
    research_and_dev_fq: float | None
    research_and_dev_fq_h: list[float | None]
    research_and_dev_fy: float | None
    research_and_dev_fy_h: list[float | None]
    research_and_dev_ttm: float | None
    restructuring_charge_fy: float | None
    restructuring_charge_fy_h: list[float | None]
    retained_earnings_fq: float | None
    retained_earnings_fq_h: list[float | None]
    retained_earnings_fy: float | None
    retained_earnings_fy_h: list[float | None]
    return_of_invested_capital_percent_ttm: float | None
    return_on_assets_fq: float | None
    return_on_assets_fq_h: list[float | None]
    return_on_assets_fy: float | None
    return_on_assets_fy_h: list[float | None]
    return_on_capital_employed_fy: float | None
    return_on_common_equity_fy: float | None
    return_on_equity_adjust_to_book_fy: float | None
    return_on_equity_adjust_to_book_ttm: float | None
    return_on_equity_fq: float | None
    return_on_equity_fq_h: list[float | None]
    return_on_equity_fy: float | None
    return_on_equity_fy_h: list[float | None]
    return_on_invested_capital_fy: float | None
    return_on_invested_capital_fy_h: list[float | None]
    return_on_tang_assets_fy: float | None
    return_on_tang_equity_fy: float | None
    return_on_total_capital_fq: float | None
    return_on_total_capital_fy: float | None
    revenue_forecast_fq: float | None
    revenue_forecast_fq_h: list[float | None]
    revenue_forecast_fy: float | None
    revenue_forecast_fy_h: list[float | None]
    revenue_forecast_next_fh: float | None
    revenue_forecast_next_fq: float | None
    revenue_forecast_next_fy: float | None
    revenue_fq: float | None
    revenue_fq_h: list[float | None]
    revenue_fy: float | None
    revenue_fy_h: list[float | None]
    revenue_h: list[float] | None = Field(None, alias="total_revenue_h")
    revenue_per_employee_fy: float | None
    revenue_per_share_fq: float | None
    revenue_per_share_fq_h: list[float | None]
    revenue_per_share_fy: float | None
    revenue_per_share_fy_h: list[float | None]
    rt_lag: datetime | None = Field(None, alias="rt-lag")
    rts_source: int | None = Field(None, alias="rts-source")
    sale_of_stock_fq: float | None
    sale_of_stock_fq_h: list[float | None]
    sale_of_stock_fy: float | None
    sale_of_stock_fy_h: list[float | None]
    sale_of_stock_ttm: float | None
    sales_of_business_fq: float | None
    sales_of_business_fq_h: list[float | None]
    sales_of_business_fy: float | None
    sales_of_business_fy_h: list[float | None]
    sales_of_investments_fq: float | None
    sales_of_investments_fq_h: list[float | None]
    sales_of_investments_fy: float | None
    sales_of_investments_fy_h: list[float | None]
    sales_of_investments_ttm: float | None
    sell_gen_admin_exp_other_fq: float | None
    sell_gen_admin_exp_other_fq_h: list[float | None]
    sell_gen_admin_exp_other_fy: float | None
    sell_gen_admin_exp_other_fy_h: list[float | None]
    sell_gen_admin_exp_other_ttm: float | None
    sell_gen_admin_exp_total_fq: float | None
    sell_gen_admin_exp_total_fq_h: list[float | None]
    sell_gen_admin_exp_total_fy: float | None
    sell_gen_admin_exp_total_fy_h: list[float | None]
    sell_gen_admin_exp_total_ttm: float | None
    series_key: datetime | None = Field(None, alias="series-key")
    share_buyback_ratio_fq: float | None
    share_buyback_ratio_fy: float | None
    short_term_debt_excl_current_port_fq: float | None
    short_term_debt_excl_current_port_fq_h: list[float | None]
    short_term_debt_excl_current_port_fy: float | None
    short_term_debt_excl_current_port_fy_h: list[float | None]
    short_term_debt_fq: float | None
    short_term_debt_fq_h: list[float | None]
    short_term_debt_fy: float | None
    short_term_debt_fy_h: list[float | None]
    short_term_invest_fq: float | None
    short_term_invest_fq_h: list[float | None]
    short_term_invest_fy: float | None
    short_term_invest_fy_h: list[float | None]
    shrhldrs_equity_fq: float | None
    shrhldrs_equity_fq_h: list[float | None]
    shrhldrs_equity_fy: float | None
    shrhldrs_equity_fy_h: list[float | None]
    sloan_ratio_fy: float | None
    sloan_ratio_ttm: float | None
    sum_for_enterprise_value: float | None
    supplying_of_long_term_debt_fq: float | None
    supplying_of_long_term_debt_fq_h: list[float | None]
    supplying_of_long_term_debt_fy: float | None
    supplying_of_long_term_debt_fy_h: list[float | None]
    supplying_of_long_term_debt_ttm: float | None
    tangible_assets_fq: float | None
    tangible_assets_fy: float | None
    tobin_q_ratio_fq: float | None
    tobin_q_ratio_fy: float | None
    top_revenue_country_code: datetime | None
    total_assets: float | None
    total_assets_fq: float | None
    total_assets_fq_h: list[float | None]
    total_assets_fy: float | None
    total_assets_fy_h: list[float | None]
    total_assets_h: list[float] | None
    total_assets_per_employee_fy: float | None
    total_assets_to_equity_fq: float | None
    total_assets_to_equity_fy: float | None
    total_cash_dividends_paid_fh: float | None
    total_cash_dividends_paid_fq: float | None
    total_cash_dividends_paid_fq_h: list[float | None]
    total_cash_dividends_paid_fy: float | None
    total_cash_dividends_paid_fy_h: list[float | None]
    total_cash_dividends_paid_ttm: float | None
    total_current_assets: float | None
    total_current_assets_fq: float | None
    total_current_assets_fq_h: list[float | None]
    total_current_assets_fy: float | None
    total_current_assets_fy_h: list[float | None]
    total_current_assets_h: list[float | None]
    total_current_liabilities_fq: float | None
    total_current_liabilities_fq_h: list[float | None]
    total_current_liabilities_fy: float | None
    total_current_liabilities_fy_h: list[float | None]
    total_debt: float | None
    total_debt_fq: float | None
    total_debt_fq_h: list[float | None]
    total_debt_fy: float | None
    total_debt_fy_h: list[float | None]
    total_debt_h: list[float | None]
    total_debt_per_employee_fy: float | None
    total_debt_per_share_current: float | None
    total_debt_per_share_fq: float | None
    total_debt_per_share_fq_h: list[float | None]
    total_debt_per_share_fy: float | None
    total_debt_per_share_fy_h: list[float | None]
    total_debt_to_capital_fq: float | None
    total_debt_to_capital_fy: float | None
    total_equity_fq: float | None
    total_equity_fq_h: list[float | None]
    total_equity_fy: float | None
    total_equity_fy_h: list[float | None]
    total_extra_items_fq: float | None
    total_extra_items_fq_h: list[float | None]
    total_extra_items_fy: float | None
    total_extra_items_fy_h: list[float | None]
    total_extra_items_ttm: float | None
    total_inventory_fq: float | None
    total_inventory_fq_h: list[float | None]
    total_inventory_fy: float | None
    total_inventory_fy_h: list[float | None]
    total_liabilities_fq: float | None
    total_liabilities_fq_h: list[float | None]
    total_liabilities_fy: float | None
    total_liabilities_fy_h: list[float | None]
    total_liabilities_shrhldrs_equity_fq: float | None
    total_liabilities_shrhldrs_equity_fq_h: list[float | None]
    total_liabilities_shrhldrs_equity_fy: float | None
    total_liabilities_shrhldrs_equity_fy_h: list[float | None]
    total_non_current_assets_fq: float | None
    total_non_current_assets_fq_h: list[float | None]
    total_non_current_assets_fy: float | None
    total_non_current_assets_fy_h: list[float | None]
    total_non_current_liabilities_fq: float | None
    total_non_current_liabilities_fq_h: list[float | None]
    total_non_current_liabilities_fy: float | None
    total_non_current_liabilities_fy_h: list[float | None]
    total_non_oper_income_fq: float | None
    total_non_oper_income_fq_h: list[float | None]
    total_non_oper_income_fy: float | None
    total_non_oper_income_fy_h: list[float | None]
    total_non_oper_income_ttm: float | None
    total_oper_expense_fq: float | None
    total_oper_expense_fq_h: list[float | None]
    total_oper_expense_fy: float | None
    total_oper_expense_fy_h: list[float | None]
    total_oper_expense_ttm: float | None
    total_receivables_net_fq: float | None
    total_receivables_net_fq_h: list[float | None]
    total_receivables_net_fy: float | None
    total_receivables_net_fy_h: list[float | None]
    total_revenue_fh: float | None
    total_revenue_fq: float | None
    total_revenue_fq_h: list[float | None]
    total_revenue_fy: float | None
    total_revenue_fy_h: list[float | None]
    total_shares_outstanding_fq: float | None
    total_shares_outstanding_fq_h: list[float | None]
    total_shares_outstanding_fy: float | None
    total_shares_outstanding_fy_h: list[float | None]
    treasury_stock_common_fq: float | None
    treasury_stock_common_fq_h: list[float | None]
    treasury_stock_common_fy: float | None
    treasury_stock_common_fy_h: list[float | None]
    unrealized_gain_loss_fy: float | None
    unrealized_gain_loss_fy_h: list[float | None]
    unusual_expense_inc_fq: float | None
    unusual_expense_inc_fq_h: list[float | None]
    unusual_expense_inc_fy: float | None
    unusual_expense_inc_fy_h: list[float | None]
    working_capital_fq: float | None
    working_capital_fy: float | None
    working_capital_per_share_current: float | None
    working_capital_per_share_fq: float | None
    working_capital_per_share_fq_h: list[float | None]
    working_capital_per_share_fy: float | None
    working_capital_per_share_fy_h: list[float | None]

    class Config:
        extra = "ignore"


class Figi(BaseModel):
    """Represents the Financial Instrument Global Identifier (FIGI)."""

    country_composite: str = Field(..., alias="country-composite")
    exchange_level: str = Field(..., alias="exchange-level")


class Source2(BaseModel):
    """Represents secondary source information."""

    country: str
    description: str
    exchange_type: str = Field(..., alias="exchange-type")
    id: str
    name: str
    url: str


class Subsession(BaseModel):
    """Represents a trading subsession (e.g., regular, premarket)."""

    description: str
    id: str
    private: bool
    session: str
    session_correction: str | None = Field(None, alias="session-correction")
    session_display: str | None = Field(None, alias="session-display")


class BarData(BaseModel):
    """Represents a single price bar (OHLCV)."""

    close: str
    data_update_time: datetime | None = Field(None, alias="data-update-time")
    high: str
    low: str
    open: str
    time: str
    update_time: datetime | None = Field(None, alias="update-time")
    volume: str


class TradeData(BaseModel):
    """Represents the last trade data."""

    data_update_time: str = Field(..., alias="data-update-time")
    price: str
    size: str
    time: str


class MarketStatus(BaseModel):
    """Represents the current market status."""

    phase: str
    tradingday: str


class Rates(BaseModel):
    """Represents currency conversion rates at a specific time."""

    time: datetime
    to_aud: float
    to_cad: float
    to_chf: float
    to_cny: float
    to_eur: float
    to_gbp: float
    to_inr: float
    to_jpy: float
    to_market: int
    to_symbol: int
    to_usd: int


class OptionSeries(BaseModel):
    """Represents a series of options for a specific expiration date."""

    exp: int
    id: str
    lotSize: int
    root: str
    strikes: list[float]
    underlying: str


class OptionFamily(BaseModel):
    """Represents a family of options (e.g., American style)."""

    description: str
    exercise: str
    name: str
    prefix: str
    series: list[OptionSeries]


class OptionsInfo(BaseModel):
    """Contains all information about available options for the symbol."""

    families: list[OptionFamily]


class FinancialReport(BaseModel):
    """Represents a single financial report line (e.g., revenue or earnings)."""

    Actual: float | None
    Estimate: float | None
    FiscalPeriod: str
    IsReported: bool
    Type: int


class RevenueSegment(BaseModel):
    """Represents a single segment of revenue (e.g., by business or region)."""

    label: str
    value: float


class RevenueBySegment(BaseModel):
    """Represents revenue broken down by segment for a specific date."""

    date: int
    segments: list[RevenueSegment]


class PermDetail(BaseModel):
    perm: datetime | None = None
    prefix: str


class Perms(BaseModel):
    delay: PermDetail | None = None
    rt: PermDetail | None = None
