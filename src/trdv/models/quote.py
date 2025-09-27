from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class QuoteData(BaseModel):
    """
    Represents comprehensive quote, fundamental, and descriptive data for a trading symbol.
    This model is designed to parse the detailed JSON blob from the data endpoint.
    """

    # ==========================================================================
    # Section 1: Core Symbol & Exchange Information
    # ==========================================================================
    symbol: str | None = None
    short_name: str | None = None
    description: str | None = None
    short_description: str | None = Field(None, alias="short-description")
    local_description: str | None = None
    exchange: str | None = None
    listed_exchange: str | None = None
    exchange_listed_name: str | None = None
    country: str | None = None
    country_code: str | None = None
    type: str | None = None
    currency: str | None = None
    typespecs: list[str] | None = None
    timezone: str | None = None
    pro_name: str | None = None
    original_name: str | None = None
    base_name: list[str] | None = None
    symbol_primary_listing: str = Field(None, alias="symbol_primary_listing")
    symbol_proname: str | None = Field(None, alias="symbol-proname")
    pro_perm: str | None = None
    language: str | None = None
    is_tradable: bool | None = None
    is_replayable: bool | None = None
    has_adjustment: bool | None = None
    has_intraday: bool | None = None
    has_no_volume: bool | None = Field(None, alias="has-no-volume")
    has_options: bool | None = None
    has_bonds: bool | None = None
    fractional: bool | None = None
    is_primary_listing: bool | None = Field(None, alias="is-primary-listing")
    is_tickbars_available: bool | None = Field(None, alias="is-tickbars-available")
    provider_id: str | None = None
    source_id: str | None = None
    source_logoid: str | None = Field(None, alias="source-logoid")
    currency_logoid: str | None = Field(None, alias="currency-logoid")
    logoid: str | None
    mic: str | None
    cik_code: int | None = Field(None, alias="cik-code")
    figi: Figi | None = None
    isin: str | None = None
    isin_displayed: str | None = Field(None, alias="isin-displayed")
    cusip: str | None = None
    source2: Source2 | None = None
    broker_names: dict[str, str] | None = None
    currency_code: str | None = None
    currency_id: str | None = None
    fundamental_currency_code: str | None = None
    perms: Perms | None = None

    # ==========================================================================
    # Section 2: Real-time & Quote Data
    # ==========================================================================
    update_mode: str | None = None
    current_session: str | None = None
    trade_loaded: bool | None = None
    hub_rt_loaded: bool | None = None
    lp: float | None = None
    lp_time: datetime | None = None
    ch: float | None = None
    chp: float | None = None
    rch: float | None = None
    rchp: float | None = None
    rtc: Any | None = None
    rtc_time: Any | None = None
    bid: float | None = None
    ask: float | None = None
    bid_size: float | None = None
    ask_size: float | None = None
    volume: int | None = None
    average_volume: float | None = None
    open_price: float | None = None
    high_price: float | None = None
    low_price: float | None = None
    prev_close_price: float | None = None
    regular_close: float | None = None
    regular_close_time: datetime | None = None
    all_time_high: float | None = None
    all_time_low: float | None = None
    all_time_high_day: datetime | None = None
    all_time_low_day: datetime | None = None
    all_time_open: float | None = None
    price_52_week_high: float | None = None
    price_52_week_low: float | None = None
    price_percent_change_1_week: float | None = None
    price_percent_change_52_week: float | None = None
    daily_bar: BarData | None = Field(None, alias="daily-bar")
    prev_daily_bar: BarData | None = Field(None, alias="prev-daily-bar")
    minute_bar: BarData | None = Field(None, alias="minute-bar")
    trade: TradeData | None = None
    market_status: MarketStatus | None = Field(None, alias="market-status")

    # ==========================================================================
    # Section 3: Session & Technical Details
    # ==========================================================================
    session_id: str | None = Field(None, alias="session-id")
    subsession_id: str | None = None
    session_display: str | None = None
    session_regular: str | None = Field(None, alias="session-regular")
    session_regular_display: str | None = Field(None, alias="session-regular-display")
    session_regular_correction: str | None = Field(
        None, alias="session-regular-correction"
    )
    session_extended: str | None = Field(None, alias="session-extended")
    session_extended_display: str | None = Field(None, alias="session-extended-display")
    session_extended_correction: str | None = Field(
        None, alias="session-extended-correction"
    )
    session_premarket: str | None = Field(None, alias="session-premarket")
    session_premarket_correction: str | None = Field(
        None, alias="session-premarket-correction"
    )
    session_postmarket: str | None = Field(None, alias="session-postmarket")
    session_postmarket_correction: str | None = Field(
        None, alias="session-postmarket-correction"
    )
    session_holidays: str | None = None
    subsessions: list[Subsession] | None = None
    pricescale: int | None = None
    minmov: int | None = None
    minmovement: int | None = None
    minmove2: int | None = None
    minmovement2: int | None = None
    pointvalue: int | None = None
    variable_tick_size: str | None = Field(None, alias="variable-tick-size")
    first_bar_time_1d: datetime | None = None
    first_bar_time_1m: datetime | None = None
    first_bar_time_1s: datetime | None = None
    trading_by: str | None = Field(None, alias="trading-by")
    visible_plots_set: str | None = Field(None, alias="visible-plots-set")
    allowed_adjustment: str | None = None

    # ==========================================================================
    # Section 4: Company Profile & Fundamental Overview
    # ==========================================================================
    business_description: str | None = None
    ceo: str | None = None
    web_site_url: str | None = None
    industry: str | None = None
    sector: str | None = None
    number_of_employees: int | None = None
    number_of_shareholders: int | None = None
    location: str | None = None
    popularity: int | None = None
    market_cap_basic: float | None = None
    market_cap_calc: float | None = None
    enterprise_value_current: float | None = None
    total_shares_outstanding: float | None = None
    total_shares_outstanding_current: float | None = None
    total_shares_outstanding_calculated: float | None = None
    total_shares_outstanding_fundamental: int | None = None
    float_shares_outstanding: float | None = None
    beta_1_year: float | None = None
    beta_3_year: float | None = None
    beta_5_year: float | None = None
    recommendation_mark: float | None = None
    recommendation_total: int | None = None
    recommendation_buy: int | None = None
    recommendation_over: int | None = None
    recommendation_hold: int | None = None
    recommendation_under: int | None = None
    recommendation_sell: int | None = None
    price_target_average: float | None = None
    price_target_high: float | None = None
    price_target_low: float | None = None
    price_target_median: float | None = None
    earnings_release_date: datetime | None = None
    earnings_release_next_date: datetime | None = None
    earnings_per_share_ttm: float | None = None
    earnings_per_share_basic_ttm: float | None = None
    earnings_per_share_diluted_ttm: float | None = None
    last_annual_eps: float | None = None
    last_annual_revenue: float | None = None
    total_revenue: float | None = None
    dividends_yield_current: float | None = None
    return_on_equity: float | None = None
    return_on_assets: float | None = None
    price_earnings_growth_ttm: float | None = None
    price_book_ratio: float | None = None
    price_sales_ratio: float | None = None
    gross_margin: float | None = None
    net_margin: float | None = None
    operating_margin: float | None = None
    quick_ratio: float | None = None
    current_ratio: float | None = None
    debt_to_equity: float | None = None
    symbol_primaryname: str | None = Field(None, alias="symbol-primaryname")
    dividends_availability: int | None = None
    financials_availability: int | None = None
    days_to_maturity: Any | None = None
    earnings_availability: int | None = None
    rt_update_period: int | None = None
    open_time: datetime | None = None
    measure: str | None = None
    last_report_frequency: int | None = None
    receivables_turnover_fq: float | None = None
    rts_source: int | None = Field(None, alias="rts-source")
    market_cap_basic_current: float | None = None
    operating_margin_ttm: float | None = None
    quick_ratio_current: float | None = None
    research_and_dev_per_employee_fy: float | None = None
    is_primary_listing: bool | None = Field(None, alias="is-primary-listing")
    fiscal_period_end_current: datetime | None = None
    operating_margin_current: float | None = None
    earnings_release_time_fq: int | None = None
    return_on_equity_current: float | None = None
    price_target_down_num: int | None = None
    return_on_invested_capital: float | None = None
    exchange_listed_symbol: str | None = Field(None, alias="exchange-listed-symbol")
    net_debt: float | None = None
    ebit_ttm: float | None = None
    book_value_per_share_current: float | None = None
    sales_of_business_ttm: float | None = None
    currency_fund: str | None = None

    # ==========================================================================
    # Section 5: Nested & Complex Fundamental Data Structures
    # ==========================================================================
    options_info: OptionsInfo | None = Field(None, alias="options-info")
    rates_fy: Rates | None = None
    rates_ttm: Rates | None = None
    rates_mc: Rates | None = None
    rates_fq: Rates | None = None
    rates_cf: Rates | None = None
    rates_pt: Rates | None = None
    rates_earnings_fy: Rates | None = None
    rates_earnings_next_fq: Rates | None = None
    revenues_fy_h: list[FinancialReport] | None = None
    revenues_fq_h: list[FinancialReport] | None = None
    earnings_fy_h: list[FinancialReport] | None = None
    earnings_fq_h: list[FinancialReport] | None = None
    revenue_seg_by_business_h: list[RevenueBySegment] | None = None
    revenue_seg_by_region_h: list[RevenueBySegment] | None = None

    # ==========================================================================
    # Section 6: Fundamental & Other Data Points
    # NOTE: Most of these are optional as they depend on asset type and data availability
    # ==========================================================================
    adjustment: str | None = None
    accum_deprec_buildings_fy_h: list[float | None] | None = None
    accum_deprec_comp_soft_fy_h: list[float | None] | None = None
    accum_deprec_construction_fy_h: list[float | None] | None = None
    accum_deprec_land_fy_h: list[float | None] | None = None
    accum_deprec_leased_prop_fy_h: list[float | None] | None = None
    accum_deprec_leases_fy_h: list[float | None] | None = None
    accum_deprec_machinery_fy_h: list[float | None] | None = None
    accum_deprec_other_fy_h: list[float | None] | None = None
    accum_deprec_other_intang_fy: float | None = None
    accum_deprec_other_intang_fy_h: list[float | None] | None = None
    accum_deprec_total_fq: float | None = None
    accum_deprec_total_fq_h: list[float | None] | None = None
    accum_deprec_total_fy: float | None = None
    accum_deprec_total_fy_h: list[float | None] | None = None
    accum_deprec_trans_equip_fy_h: list[float | None] | None = None
    accrued_expenses_fy: float | None = None
    accrued_expenses_fy_h: list[float | None] | None = None
    accrued_payroll_fq: float | None = None
    accrued_payroll_fq_h: list[float | None] | None = None
    accrued_payroll_fy: float | None = None
    accrued_payroll_fy_h: list[float | None] | None = None
    accounts_payable_fq: float | None = None
    accounts_payable_fq_h: list[float | None] | None = None
    accounts_payable_fy: float | None = None
    accounts_payable_fy_h: list[float | None] | None = None
    accounts_receivables_gross_fy: float | None = None
    accounts_receivables_gross_fy_h: list[float | None] | None = None
    accounts_receivables_net_fq: float | None = None
    accounts_receivables_net_fq_h: list[float | None] | None = None
    accounts_receivables_net_fy: float | None = None
    additional_paid_in_capital_fq: float | None = None
    additional_paid_in_capital_fq_h: list[float | None] | None = None
    additional_paid_in_capital_fy: float | None = None
    additional_paid_in_capital_fy_h: list[float | None] | None = None
    after_tax_margin: float | None = None
    after_tax_other_income_fq: float | None = None
    after_tax_other_income_fq_h: list[float | None] | None = None
    after_tax_other_income_fy: float | None = None
    after_tax_other_income_fy_h: list[float | None] | None = None
    after_tax_other_income_ttm: float | None = None
    altman_z_score_ttm: float | None = None
    amortization_fq_h: list[float | None] | None = None
    amortization_fy_h: list[float | None] | None = None
    amortization_of_deferred_charges_fy: float | None = None
    amortization_of_deferred_charges_fy_h: list[float | None] | None = None
    amortization_of_intangibles_fy: float | None = None
    amortization_of_intangibles_fy_h: list[float | None] | None = None
    asset_turnover_current: float | None = None
    asset_turnover_fq: float | None = None
    asset_turnover_fq_h: list[float | None] | None = None
    asset_turnover_fy: float | None = None
    asset_turnover_fy_h: list[float | None] | None = None
    basic_shares_outstanding_fq: float | None = None
    basic_shares_outstanding_fq_h: list[float | None] | None = None
    basic_shares_outstanding_fy: float | None = None
    basic_shares_outstanding_fy_h: list[float | None] | None = None
    book_per_share_fq: float | None = None
    book_per_share_fy: float | None = None
    book_tangible_per_share_current: float | None = None
    book_tangible_per_share_fq: float | None = None
    book_tangible_per_share_fq_h: list[float | None] | None = None
    book_tangible_per_share_fy: float | None = None
    book_tangible_per_share_fy_h: list[float | None] | None = None
    book_value_per_share_fq: float | None = None
    book_value_per_share_current: float | None = None
    book_value_per_share_fq_h: list[float | None] | None = None
    book_value_per_share_fy: float | None = None
    book_value_per_share_fy_h: list[float | None] | None = None
    capital_expenditures_fh: float | None = None
    capital_expenditures_fixed_assets_fq: float | None = None
    capital_expenditures_fixed_assets_fq_h: list[float | None] | None = None
    capital_expenditures_fixed_assets_fy: float | None = None
    capital_expenditures_fixed_assets_fy_h: list[float | None] | None = None
    capital_expenditures_fixed_assets_ttm: float | None = None
    capital_expenditures_fq: float | None = None
    capital_expenditures_fq_h: list[float | None] | None = None
    capital_expenditures_fy: float | None = None
    capital_expenditures_fy_h: list[float | None] | None = None
    capital_expenditures_other_assets_fq: float | None = None
    capital_expenditures_other_assets_fq_h: list[float | None] | None = None
    capital_expenditures_other_assets_fy: float | None = None
    capital_expenditures_other_assets_fy_h: list[float | None] | None = None
    capital_expenditures_other_assets_ttm: float | None = None
    capital_expenditures_ttm: float | None = None
    capital_expenditures_unchanged_fq: float | None = None
    capital_expenditures_unchanged_fq_h: list[float | None] | None = None
    capital_expenditures_unchanged_fy: float | None = None
    capital_expenditures_unchanged_fy_h: list[float | None] | None = None
    capital_expenditures_unchanged_ttm: float | None = None
    capital_expenditures_unchanged_ttm_h: list[float | None] | None = None
    capital_lease_obligations_fq: float | None = None
    capital_lease_obligations_fq_h: list[float | None] | None = None
    capital_lease_obligations_fy: float | None = None
    capital_lease_obligations_fy_h: list[float | None] | None = None
    capital_operating_lease_obligations_fq: float | None = None
    capital_operating_lease_obligations_fq_h: list[float | None] | None = None
    capital_operating_lease_obligations_fy: float | None = None
    capital_operating_lease_obligations_fy_h: list[float | None] | None = None
    capex_per_share_current: float | None = None
    capex_per_share_fq: float | None = None
    capex_per_share_fq_h: list[float | None] | None = None
    capex_per_share_fy: float | None = None
    capex_per_share_fy_h: list[float | None] | None = None
    capex_per_share_ttm: float | None = None
    cash_f_financing_activities_fh: float | None = None
    cash_f_financing_activities_fq: float | None = None
    cash_f_financing_activities_fq_h: list[float | None] | None = None
    cash_f_financing_activities_fy: float | None = None
    cash_f_financing_activities_fy_h: list[float | None] | None = None
    cash_f_financing_activities_ttm: float | None = None
    cash_f_investing_activities_fh: float | None = None
    cash_f_investing_activities_fq: float | None = None
    cash_f_investing_activities_fq_h: list[float | None] | None = None
    cash_f_investing_activities_fy: float | None = None
    cash_f_investing_activities_fy_h: list[float | None] | None = None
    cash_f_investing_activities_ttm: float | None = None
    cash_f_operating_activities_fh: float | None = None
    cash_f_operating_activities_fq: float | None = None
    cash_f_operating_activities_fq_h: list[float | None] | None = None
    cash_f_operating_activities_fy: float | None = None
    cash_f_operating_activities_fy_h: list[float | None] | None = None
    cash_f_operating_activities_ttm: float | None = None
    cash_flow_deferred_taxes_fq: float | None = None
    cash_flow_deferred_taxes_fq_h: list[float | None] | None = None
    cash_flow_deferred_taxes_fy: float | None = None
    cash_flow_deferred_taxes_fy_h: list[float | None] | None = None
    cash_flow_deferred_taxes_ttm: float | None = None
    cash_flow_deprecation_n_amortization_fq: float | None = None
    cash_flow_deprecation_n_amortization_fq_h: list[float | None] | None = None
    cash_flow_deprecation_n_amortization_fy: float | None = None
    cash_flow_deprecation_n_amortization_fy_h: list[float | None] | None = None
    cash_flow_deprecation_n_amortization_ttm: float | None = None
    cash_n_equivalents_fq: float | None = None
    cash_n_equivalents_fq_h: list[float | None] | None = None
    cash_n_equivalents_fy: float | None = None
    cash_n_equivalents_fy_h: list[float | None] | None = None
    cash_n_short_term_invest_fq: float | None = None
    cash_n_short_term_invest_fq_h: list[float | None] | None = None
    cash_n_short_term_invest_fy: float | None = None
    cash_n_short_term_invest_fy_h: list[float | None] | None = None
    cash_per_share_fq: float | None = None
    cash_per_share_fq_h: list[float | None] | None = None
    cash_per_share_fy: float | None = None
    cash_per_share_fy_h: list[float | None] | None = None
    change_in_accounts_payable_fq: float | None = None
    change_in_accounts_payable_fq_h: list[float | None] | None = None
    change_in_accounts_payable_fy: float | None = None
    change_in_accounts_payable_fy_h: list[float | None] | None = None
    change_in_accounts_payable_ttm: float | None = None
    change_in_accounts_receivable_fq: float | None = None
    change_in_accounts_receivable_fq_h: list[float | None] | None = None
    change_in_accounts_receivable_fy: float | None = None
    change_in_accounts_receivable_fy_h: list[float | None] | None = None
    change_in_accounts_receivable_ttm: float | None = None
    change_in_accrued_expenses_fq: float | None = None
    change_in_accrued_expenses_fq_h: list[float | None] | None = None
    change_in_accrued_expenses_fy: float | None = None
    change_in_accrued_expenses_ttm: float | None = None
    change_in_inventories_fq: float | None = None
    change_in_inventories_fq_h: list[float | None] | None = None
    change_in_inventories_fy: float | None = None
    change_in_inventories_ttm: float | None = None
    change_in_other_assets_fq: float | None = None
    change_in_other_assets_fq_h: list[float | None] | None = None
    change_in_other_assets_fy: float | None = None
    change_in_other_assets_ttm: float | None = None
    change_in_taxes_payable_fq_h: list[Any | None] = None
    change_in_taxes_payable_fy_h: list[Any | None] | None = None
    changes_in_working_capital_fq: float | None = None
    changes_in_working_capital_fq_h: list[float | None] | None = None
    changes_in_working_capital_fy: float | None = None
    changes_in_working_capital_fy_h: list[float | None] | None = None
    changes_in_working_capital_ttm: float | None = None
    common_dividends_cash_flow_fq: float | None = None
    common_dividends_cash_flow_fq_h: list[float | None] | None = None
    common_dividends_cash_flow_fy: float | None = None
    common_dividends_cash_flow_fy_h: list[float | None] | None = None
    common_dividends_cash_flow_ttm: float | None = None
    common_equity_total_fq: float | None = None
    common_equity_total_fq_h: list[float | None] | None = None
    common_equity_total_fy: float | None = None
    common_equity_total_fy_h: list[float | None] | None = None
    common_stock_par_fq: float | None = None
    common_stock_par_fq_h: list[float | None] | None = None
    common_stock_par_fy: float | None = None
    common_stock_par_fy_h: list[float | None] | None = None
    cost_of_goods_excl_dep_amort_fq: float | None = None
    cost_of_goods_excl_dep_amort_fq_h: list[float | None] | None = None
    cost_of_goods_excl_dep_amort_fy: float | None = None
    cost_of_goods_excl_dep_amort_fy_h: list[float | None] | None = None
    cost_of_goods_excl_dep_amort_ttm: float | None = None
    cost_of_goods_fq: float | None = None
    cost_of_goods_fq_h: list[float | None] | None = None
    cost_of_goods_fy: float | None = None
    cost_of_goods_fy_h: list[float | None] | None = None
    cost_of_goods_ttm: float | None = None
    country_code_fund: str | None = None
    country_fund: str | None = None
    current_port_debt_capital_leases_fq: float | None = None
    current_port_debt_capital_leases_fq_h: list[float | None] | None = None
    current_port_debt_capital_leases_fy: float | None = None
    current_port_debt_capital_leases_fy_h: list[float | None] | None = None
    current_ratio_current: float | None = None
    current_ratio_fq: float | None = None
    current_ratio_fq_h: list[float | None] | None = None
    current_ratio_fy: float | None = None
    current_ratio_fy_h: list[float | None] | None = None
    debt_to_asset_current: float | None = None
    debt_to_asset_fq: float | None = None
    debt_to_asset_fq_h: list[float | None] | None = None
    debt_to_asset_fy: float | None = None
    debt_to_asset_fy_h: list[float | None] | None = None
    debt_to_equity_current: float | None = None
    debt_to_equity_fq: float | None = None
    debt_to_equity_fq_h: list[float | None] | None = None
    debt_to_equity_fy: float | None = None
    debt_to_equity_fy_h: list[float | None] | None = None
    debt_to_revenue_fy: float | None = None
    debt_to_revenue_ttm: float | None = None
    deferred_charges_fq_h: list[Any | None] = None
    deferred_charges_fy_h: list[Any | None] | None = None
    deferred_income_current_fq: float | None = None
    deferred_income_current_fq_h: list[float | None] | None = None
    deferred_income_current_fy: float | None = None
    deferred_income_current_fy_h: list[float | None] | None = None
    deferred_income_non_current_fq_h: list[Any | None] = None
    deferred_income_non_current_fy_h: list[Any | None] = None
    deferred_tax_assests_fq: float | None = None
    deferred_tax_assests_fq_h: list[float | None] | None = None
    deferred_tax_assests_fy: float | None = None
    deferred_tax_assests_fy_h: list[float | None] | None = None
    deferred_tax_liabilities_fq: float | None = None
    deferred_tax_liabilities_fq_h: list[float | None] | None = None
    deferred_tax_liabilities_fy: float | None = None
    deferred_tax_liabilities_fy_h: list[float | None] | None = None
    dep_amort_exp_income_s_fq: float | None = None
    dep_amort_exp_income_s_fq_h: list[float | None] | None = None
    dep_amort_exp_income_s_fy: float | None = None
    dep_amort_exp_income_s_fy_h: list[float | None] | None = None
    dep_amort_exp_income_s_ttm: float | None = None
    depreciation_depletion_fq_h: list[float | None] | None = None
    depreciation_depletion_fy_h: list[float | None] | None = None
    depreciation_fy: float | None = None
    depreciation_fy_h: list[float | None] | None = None
    diluted_net_income_fq: float | None = None
    diluted_net_income_fq_h: list[float | None] | None = None
    diluted_net_income_fy: float | None = None
    diluted_net_income_fy_h: list[float | None] | None = None
    diluted_net_income_ttm: float | None = None
    diluted_shares_outstanding_fq: float | None = None
    diluted_shares_outstanding_fq_h: list[float | None] | None = None
    diluted_shares_outstanding_fy: float | None = None
    diluted_shares_outstanding_fy_h: list[float | None] | None = None
    dilution_adjustment_fq: float | None = None
    dilution_adjustment_fq_h: list[float | None] | None = None
    dilution_adjustment_fy: float | None = None
    dilution_adjustment_fy_h: list[float | None] | None = None
    dilution_adjustment_ttm: float | None = None
    discontinued_operations_fq: float | None = None
    discontinued_operations_fq_h: list[float | None] | None = None
    discontinued_operations_fy: float | None = None
    discontinued_operations_fy_h: list[float | None] | None = None
    discontinued_operations_ttm: float | None = None
    dividend_amount_h: list[Any] | None = None
    dividend_ex_date_h: list[Any] | None = None
    dividend_payment_date_h: list[Any] | None = None
    dividend_payout_ratio_fq_h: list[float | None] | None = None
    dividend_payout_ratio_fy_h: list[Any | None] = None
    dividend_payout_ratio_ttm: float | None = None
    dividend_record_date_h: list[Any] = None
    dividend_type_h: list[Any] = None
    dividends_paid: float | None = None
    dividends_payable_fy: float | None = None
    dividends_payable_fy_h: list[float | None] | None = None
    dividends_per_share_fq: float | None = None
    dividends_yield_fq: float | None = None
    dividends_yield_fy: float | None = None
    dividends_yield_fy_h: list[float | None] | None = None
    documents: int | None = None
    doubtful_accounts_fy_h: list[Any | None] = None
    dps_common_stock_prim_issue_fh: float | None = None
    dps_common_stock_prim_issue_fq: float | None = None
    dps_common_stock_prim_issue_fq_h: list[float | None] | None = None
    dps_common_stock_prim_issue_fy: float | None = None
    dps_common_stock_prim_issue_fy_h: list[float | None] | None = None
    earnings_per_share_basic_fh: float | None = None
    earnings_per_share_basic_fq: float | None = None
    earnings_per_share_basic_fq_h: list[float | None] | None = None
    earnings_per_share_basic_fy: float | None = None
    earnings_per_share_basic_fy_h: list[float | None] | None = None
    earnings_per_share_diluted_fh: float | None = None
    earnings_per_share_diluted_fq: float | None = None
    earnings_per_share_diluted_fq_h: list[float | None] | None = None
    earnings_per_share_diluted_fy: float | None = None
    earnings_per_share_diluted_fy_h: list[float | None] | None = None
    earnings_per_share_fh: float | None = None
    earnings_per_share_forecast_fq: float | None = None
    earnings_per_share_forecast_fq_h: list[float | None] | None = None
    earnings_per_share_forecast_fy: float | None = None
    earnings_per_share_forecast_fy_h: list[float | None] | None = None
    earnings_per_share_forecast_next_fh: float | None = None
    earnings_per_share_forecast_next_fq: float | None = None
    earnings_per_share_forecast_next_fy: float | None = None
    earnings_per_share_fq: float | None = None
    earnings_per_share_fq_h: list[float | None] | None = None
    earnings_per_share_fy: float | None = None
    earnings_per_share_fy_h: list[float | None] | None = None
    earnings_publication_type_next_fy: int | None = None
    earnings_release_calendar_date: datetime | None = None
    earnings_release_calendar_date_fq: datetime | None = None
    earnings_release_date_fq_h: list[int | None] = None
    earnings_release_date_fy_h: list[int | None] | None = None
    earnings_release_next_calendar_date: datetime | None = None
    earnings_release_next_calendar_date_fq: datetime | None = None
    earnings_release_next_date_fq: datetime | None = None
    earnings_release_next_date_fy: datetime | None = None
    earnings_release_next_time: int | None = None
    earnings_release_next_time_fq: int | None = None
    earnings_release_next_trading_date_fq: datetime | None = None
    earnings_release_next_trading_date_fy: datetime | None = None
    earnings_release_trading_date_fy: datetime | None = None
    earnings_fiscal_period_fq: str | None = None
    earnings_fiscal_period_fq_h: list[str | None] = None
    earnings_fiscal_period_fy: str | None = None
    earnings_fiscal_period_fy_h: list[str | None] = None
    ebit_fq: float | None = None
    ebit_fq_h: list[float | None] | None = None
    ebit_fy: float | None = None
    ebit_fy_h: list[float | None] | None = None
    ebitda_fh: float | None = None
    ebitda_fq: float | None = None
    ebitda_fq_h: list[float | None] | None = None
    ebitda_fy: float | None = None
    ebitda_fy_h: list[float | None] | None = None
    ebitda_interst_cover_fy: float | None = None
    ebitda_interst_cover_ttm: float | None = None
    ebitda_less_capex_interst_cover_fy: float | None = None
    ebitda_less_capex_interst_cover_ttm: float | None = None
    ebitda_margin_fq: float | None = None
    ebitda_margin_fq_h: list[float | None] | None = None
    ebitda_margin_fy: float | None = None
    ebitda_margin_fy_h: list[float | None] | None = None
    ebitda_margin_ttm: float | None = None
    ebitda_per_employee_fy: float | None = None
    ebitda_per_share_fq: float | None = None
    ebitda_per_share_fq_h: list[float | None] | None = None
    ebitda_per_share_fy: float | None = None
    ebitda_per_share_fy_h: list[float | None] | None = None
    ebitda_per_share_ttm: float | None = None
    ebitda_per_share_current: float | None = None
    ebitda_ttm_h: list[float | None] | None = None
    ebit_per_share_fq: float | None = None
    ebit_per_share_fq_h: list[float | None] | None = None
    ebit_per_share_fy: float | None = None
    ebit_per_share_fy_h: list[float | None] | None = None
    ebit_per_share_ttm: float | None = None
    effective_interest_rate_on_debt_fy: float | None = None
    effective_interest_rate_on_debt_ttm: float | None = None
    enterprise_value_ebitda_fq_h: list[Any | None] = None
    enterprise_value_ebitda_fy_h: list[Any | None] = None
    enterprise_value_fq_h: list[float | None] | None = None
    enterprise_value_fy_h: list[float | None] | None = None
    enterprise_value_fy: float | None = None
    eps_diluted_growth_percent_fq: float | None = None
    eps_diluted_growth_percent_fy: float | None = None
    equity_in_earnings_fq: float | None = None
    equity_in_earnings_fq_h: list[float | None] | None = None
    equity_in_earnings_fy: float | None = None
    equity_in_earnings_fy_h: list[float | None] | None = None
    equity_in_earnings_ttm: float | None = None
    exchange_ticker: str | None = Field(None, alias="exchange-ticker")
    exchange_traded: str | None = Field(None, alias="exchange-traded")
    exchange_traded_name: str | None = None
    exchange_listed: str | None = Field(None, alias="exchange-listed")
    fixed_assets_turnover_fq: float | None = None
    fixed_assets_turnover_fy: float | None = None
    float_shares_outstanding_fy: float | None = None
    float_shares_outstanding_fy_h: list[float | None] | None = None
    free_cash_flow_fh: float | None = None
    free_cash_flow_fq: float | None = None
    free_cash_flow_fq_h: list[float | None] | None = None
    free_cash_flow_fy: float | None = None
    free_cash_flow_fy_h: list[float | None] | None = None
    free_cash_flow_per_employee_fy: float | None = None
    free_cash_flow_per_share_fq: float | None = None
    free_cash_flow_per_share_fq_h: list[float | None] | None = None
    free_cash_flow_per_share_fy: float | None = None
    free_cash_flow_per_share_fy_h: list[float | None] | None = None
    free_cash_flow_per_share_ttm: float | None = None
    free_cash_flow_per_share_current: float | None = None
    free_cash_flow_ttm_h: list[float | None] | None = None
    fund_view_mode: str | None = None
    funds_f_operations_fq: float | None = None
    funds_f_operations_fq_h: list[float | None] | None = None
    funds_f_operations_fy: float | None = None
    funds_f_operations_fy_h: list[float | None] | None = None
    funds_f_operations_ttm: float | None = None
    fundamental_data: bool | None = None
    goodwill: float | None = None
    goodwill_amortization_fy_h: list[Any | None] = None
    goodwill_fq: float | None = None
    goodwill_fq_h: list[float | None] | None = None
    goodwill_fy: float | None = None
    goodwill_fy_h: list[float | None] | None = None
    goodwill_gross_fy: float | None = None
    gross_profit: float | None = None
    goodwill_gross_fy_h: list[float | None] | None = None
    gross_margin_fq: float | None = None
    gross_margin_fq_h: list[float | None] | None = None
    gross_margin_fy: float | None = None
    gross_margin_fy_h: list[float | None] | None = None
    gross_margin_ttm: float | None = None
    gross_profit_fh: float | None = None
    gross_margin_current: float | None = None
    gross_profit_fq: float | None = None
    gross_profit_fq_h: list[float | None] | None = None
    gross_profit_fy: float | None = None
    gross_profit_fy_h: list[float | None] | None = None
    gross_profit_ttm_h: list[float | None] | None = None
    group: str | None = None
    history_tag: str | None = Field(None, alias="history-tag")
    has_dwm: bool | None = Field(None, alias="has-dwm")
    has_etf_ownership: bool | None = None
    has_no_realtime: bool | None = Field(None, alias="has-no-realtime")
    has_price_snapshot: bool | None = Field(None, alias="has-price-snapshot")
    impairments_fy_h: list[Any | None] | None = None
    income_tax_credits_fy: float | None = None
    income_tax_credits_fy_h: list[float | None] | None = None
    income_tax_current_domestic_fy: float | None = None
    income_tax_current_domestic_fy_h: list[float | None] | None = None
    income_tax_current_foreign_fy: float | None = None
    income_tax_current_foreign_fy_h: list[float | None] | None = None
    income_tax_current_fy: float | None = None
    income_tax_current_fy_h: list[float | None] | None = None
    income_tax_deferred_domestic_fy: float | None = None
    income_tax_deferred_domestic_fy_h: list[float | None] | None = None
    income_tax_deferred_foreign_fy: float | None = None
    income_tax_deferred_foreign_fy_h: list[float | None] | None = None
    income_tax_deferred_fy: float | None = None
    income_tax_deferred_fy_h: list[float | None] | None = None
    income_tax_fq: float | None = None
    income_tax_fq_h: list[float | None] | None = None
    income_tax_fy: float | None = None
    income_tax_fy_h: list[float | None] | None = None
    income_tax_payable_fq_h: list[Any | None] = None
    income_tax_payable_fy_h: list[Any | None] = None
    income_tax_ttm: float | None = None
    intangibles_net_fq: float | None = None
    intangibles_net_fq_h: list[float | None] | None = None
    intangibles_net_fy: float | None = None
    intangibles_net_fy_h: list[float | None] | None = None
    interest_capitalized_fq: float | None = None
    interest_capitalized_fq_h: list[float | None] | None = None
    interest_capitalized_fy: float | None = None
    interest_capitalized_fy_h: list[float | None] | None = None
    interest_capitalized_ttm: float | None = None
    interest_expense_on_debt_fq: float | None = None
    interest_expense_on_debt_fq_h: list[float | None] | None = None
    interest_expense_on_debt_fy: float | None = None
    interest_expense_on_debt_fy_h: list[float | None] | None = None
    interest_expense_on_debt_ttm: float | None = None
    interst_cover_fy: float | None = None
    interst_cover_ttm: float | None = None
    invent_turnover_fq: float | None = None
    invent_turnover_fq_h: list[float | None] | None = None
    invent_turnover_fy: float | None = None
    invent_turnover_fy_h: list[float | None] | None = None
    invent_turnover_current: float | None = None
    inventory_finished_goods_fq: float | None = None
    inventory_finished_goods_fq_h: list[float | None] | None = None
    inventory_finished_goods_fy: float | None = None
    inventory_finished_goods_fy_h: list[float | None] | None = None
    inventory_progress_payments_fq: float | None = None
    inventory_progress_payments_fq_h: list[float | None] | None = None
    inventory_progress_payments_fy: float | None = None
    inventory_progress_payments_fy_h: list[float | None] | None = None
    inventory_progress_payments_fy_h: list[float | None] | None = None
    inventory_raw_materials_fq: float | None = None
    inventory_raw_materials_fq_h: list[float | None] | None = None
    inventory_raw_materials_fy: float | None = None
    inventory_raw_materials_fy_h: list[float | None] | None = None
    inventory_work_in_progress_fq: float | None = None
    inventory_work_in_progress_fq_h: list[float | None] | None = None
    inventory_work_in_progress_fy: float | None = None
    inventory_work_in_progress_fy_h: list[float | None] | None = None
    inventory_work_in_progress_fy_h: list[float | None] | None = None
    invested_capital_fy: float | None = None
    investments_in_unconcsolidate_fq: float | None = None
    investments_in_unconcsolidate_fq_h: list[float | None] | None = None
    investments_in_unconcsolidate_fy: float | None = None
    investments_in_unconcsolidate_fy_h: list[float | None] | None = None
    issuance_of_debt_net_fq: float | None = None
    issuance_of_debt_net_fq_h: list[float | None] | None = None
    issuance_of_debt_net_fy: float | None = None
    issuance_of_debt_net_fy_h: list[float | None] | None = None
    issuance_of_debt_net_ttm: float | None = None
    issuance_of_long_term_debt_fq: float | None = None
    issuance_of_long_term_debt_fq_h: list[float | None] | None = None
    issuance_of_long_term_debt_fy: float | None = None
    issuance_of_long_term_debt_fy_h: list[float | None] | None = None
    issuance_of_long_term_debt_ttm: float | None = None
    issuance_of_other_debt_fq_h: list[Any | None] = None
    issuance_of_other_debt_fy_h: list[Any | None] = None
    issuance_of_short_term_debt_fq: float | None = None
    issuance_of_short_term_debt_fq_h: list[float | None] | None = None
    issuance_of_short_term_debt_fy: float | None = None
    issuance_of_short_term_debt_fy_h: list[float | None] | None = None
    issuance_of_short_term_debt_ttm: float | None = None
    issuance_of_stock_net_fq: float | None = None
    issuance_of_stock_net_fq_h: list[float | None] | None = None
    issuance_of_stock_net_fy: float | None = None
    issuance_of_stock_net_fy_h: list[float | None] | None = None
    issuance_of_stock_net_ttm: float | None = None
    kind_delay: int | None = Field(None, alias="kind-delay")
    is_primary: bool | None = Field(None, alias="is-primary")
    legal_claim_expense_fy_h: list[Any | None] | None = None
    long_term_debt_excl_capital_lease_fq: float | None = None
    long_term_debt_excl_capital_lease_fq_h: list[float | None] | None = None
    long_term_debt_excl_capital_lease_fy: float | None = None
    long_term_debt_excl_capital_lease_fy_h: list[float | None] | None = None
    long_term_debt_fq: float | None = None
    long_term_debt_fq_h: list[float | None] | None = None
    long_term_debt_fy: float | None = None
    long_term_debt_fy_h: list[float | None] | None = None
    long_term_debt_to_assets_current: float | None = None
    long_term_debt_to_assets_fq: float | None = None
    long_term_debt_to_assets_fq_h: list[float | None] | None = None
    long_term_debt_to_assets_fy: float | None = None
    long_term_debt_to_assets_fy_h: list[float | None] | None = None
    long_term_debt_to_equity_current: float | None = None
    long_term_debt_to_equity_fq: float | None = None
    long_term_debt_to_equity_fq_h: list[float | None] | None = None
    long_term_debt_to_equity_fy: float | None = None
    long_term_debt_to_equity_fy_h: list[float | None] | None = None
    long_term_investments_fq: float | None = None
    long_term_investments_fq_h: list[float | None] | None = None
    long_term_investments_fy: float | None = None
    long_term_investments_fy_h: list[float | None] | None = None
    long_term_note_receivable_fq: float | None = None
    long_term_note_receivable_fq_h: list[float | None] | None = None
    long_term_note_receivable_fy: float | None = None
    long_term_note_receivable_fy_h: list[float | None] | None = None
    long_term_other_assets_total_fq: float | None = None
    long_term_other_assets_total_fq_h: list[float | None] | None = None
    long_term_other_assets_total_fy: float | None = None
    long_term_other_assets_total_fy_h: list[float | None] | None = None
    market_cap_basic_fq: float | None = None
    local_popularity: dict[str, int] | None = None
    market_cap_basic_fq_h: list[float | None] | None = None
    market_cap_basic_fy: float | None = None
    market_cap_basic_fy_h: list[float | None] | None = None
    minority_interest_exp_fq: float | None = None
    minority_interest_exp_fq_h: list[float | None] | None = None
    minority_interest_exp_fy: float | None = None
    minority_interest_exp_fy_h: list[float | None] | None = None
    minority_interest_exp_ttm: float | None = None
    minority_interest_fq: float | None = None
    minority_interest_fq_h: list[float | None] | None = None
    minority_interest_fy: float | None = None
    minority_interest_fy_h: list[float | None] | None = None
    ncavps_ratio_current: float | None = None
    ncavps_ratio_fq: float | None = None
    ncavps_ratio_fq_h: list[float | None] | None = None
    ncavps_ratio_fy: float | None = None
    ncavps_ratio_fy_h: list[float | None] | None = None
    net_debt_fq: float | None = None
    net_debt_fq_h: list[float | None] | None = None
    net_debt_fy: float | None = None
    net_debt_fy_h: list[float | None] | None = None
    net_income: float | None = None
    net_income_bef_disc_oper_fq: float | None = None
    net_income_bef_disc_oper_fq_h: list[float | None] | None = None
    net_income_bef_disc_oper_fy: float | None = None
    net_income_bef_disc_oper_fy_h: list[float | None] | None = None
    net_income_bef_disc_oper_ttm: float | None = None
    net_income_fh: float | None = None
    net_income_fq: float | None = None
    net_income_fq_h: list[float | None] | None = None
    net_income_fy: float | None = None
    net_income_fy_h: list[float | None] | None = None
    net_income_per_employee_fy: float | None = None
    net_income_starting_line_fq: float | None = None
    net_income_starting_line_fq_h: list[float | None] | None = None
    net_income_ttm: float | None = None
    net_income_starting_line_fy: float | None = None
    net_income_starting_line_fy_h: list[float | None] | None = None
    net_income_starting_line_ttm: float | None = None
    net_income_ttm_h: list[float | None] | None = None
    net_margin_fq: float | None = None
    net_margin_fq_h: list[float | None] | None = None
    net_margin_fy: float | None = None
    net_margin_fy_h: list[float | None] | None = None
    net_margin_current: float | None = None
    net_margin_ttm: float | None = None
    news_langs: list[str] | None = Field(None, alias="news-langs")
    non_cash_items_fq: float | None = None
    non_cash_items_fq_h: list[float | None] | None = None
    non_cash_items_fy: float | None = None
    non_cash_items_fy_h: list[float | None] | None = None
    non_cash_items_ttm: float | None = None
    non_oper_income_ttm: float | None = None
    non_oper_income_fq: float | None = None
    non_oper_income_fq_h: list[float | None] | None = None
    non_oper_income_fy: float | None = None
    non_oper_income_fy_h: list[float | None] | None = None
    non_oper_interest_exp_fq: float | None = None
    non_oper_interest_exp_fq_h: list[float | None] | None = None
    non_oper_interest_exp_fy: float | None = None
    non_oper_interest_exp_fy_h: list[float | None] | None = None
    non_oper_interest_exp_ttm: float | None = None
    non_oper_interest_income_fq: float | None = None
    non_oper_interest_income_fq_h: list[float | None] | None = None
    non_oper_interest_income_fy: float | None = None
    non_oper_interest_income_fy_h: list[float | None] | None = None
    non_oper_interest_income_ttm: float | None = None
    notes_payable_short_term_debt_fy_h: list[Any | None] = None
    number_of_employees_fy: int | None = None
    number_of_shareholders_fy: int | None = None
    number_of_employees_fy_h: list[int | None] = None
    number_of_shareholders_fy_h: list[int | None] = None
    oper_income_fh: float | None = None
    oper_income_fq: float | None = None
    oper_income_fq_h: list[float | None] | None = None
    oper_income_fy: float | None = None
    oper_income_fy_h: list[float | None] | None = None
    oper_income_per_employee_fy: float | None = None
    oper_income_ttm: float | None = None
    operating_expenses_fq: float | None = None
    operating_expenses_fy: float | None = None
    operating_expenses_ttm: float | None = None
    operating_lease_liabilities_fq: float | None = None
    operating_lease_liabilities_fq_h: list[float | None] | None = None
    operating_lease_liabilities_fy: float | None = None
    operating_lease_liabilities_fy_h: list[float | None] | None = None
    operating_margin_fq: float | None = None
    operating_margin_fq_h: list[float | None] | None = None
    operating_margin_fy: float | None = None
    operating_cash_flow_per_share: float | None = None
    operating_cash_flow_per_share_current: float | None = None
    operating_cash_flow_per_share_fq: float | None = None
    operating_cash_flow_per_share_fq_h: list[float | None] | None = None
    operating_cash_flow_per_share_fy: float | None = None
    operating_margin_fy_h: list[float | None] | None = None
    other_common_equity_fq: float | None = None
    other_common_equity_fq_h: list[float | None] | None = None
    other_common_equity_fy: float | None = None
    other_common_equity_fy_h: list[float | None] | None = None
    other_current_assets_total_fq: float | None = None
    other_current_assets_total_fq_h: list[float | None] | None = None
    other_current_assets_total_fy: float | None = None
    other_current_assets_total_fy_h: list[float | None] | None = None
    other_current_liabilities_fq: float | None = None
    other_current_liabilities_fq_h: list[float | None] | None = None
    other_current_liabilities_fy: float | None = None
    other_current_liabilities_fy_h: list[float | None] | None = None
    other_exceptional_charges_fy_h: list[Any | None] = None
    other_financing_cash_flow_items_total_fq: float | None = None
    other_financing_cash_flow_items_total_fq_h: list[float | None] | None = None
    other_financing_cash_flow_items_total_fy: float | None = None
    other_financing_cash_flow_items_total_fy_h: list[float | None] | None = None
    other_financing_cash_flow_items_total_ttm: float | None = None
    other_financing_cash_flow_sources_fq: float | None = None
    other_financing_cash_flow_sources_fq_h: list[float | None] | None = None
    other_financing_cash_flow_sources_fy: float | None = None
    other_financing_cash_flow_sources_fy_h: list[float | None] | None = None
    other_financing_cash_flow_sources_ttm: float | None = None
    other_financing_cash_flow_uses_fq: float | None = None
    other_financing_cash_flow_uses_fq_h: list[float | None] | None = None
    other_financing_cash_flow_uses_fy: float | None = None
    other_financing_cash_flow_uses_fy_h: list[float | None] | None = None
    other_financing_cash_flow_uses_ttm: float | None = None
    other_income_fq: float | None = None
    other_income_fq_h: list[float | None] | None = None
    other_income_fy: float | None = None
    other_income_fy_h: list[float | None] | None = None
    other_income_ttm: float | None = None
    other_intangibles_gross_fy: float | None = None
    other_intangibles_gross_fy_h: list[float | None] | None = None
    other_intangibles_net_fq: float | None = None
    other_intangibles_net_fq_h: list[float | None] | None = None
    other_intangibles_net_fy: float | None = None
    other_intangibles_net_fy_h: list[float | None] | None = None
    other_investing_cash_flow_items_total_fq: float | None = None
    other_investing_cash_flow_items_total_fq_h: list[float | None] | None = None
    other_investing_cash_flow_items_total_fy: float | None = None
    other_investing_cash_flow_items_total_fy_h: list[float | None] | None = None
    other_investing_cash_flow_items_total_ttm: float | None = None
    other_investing_cash_flow_sources_fq: float | None = None
    other_investing_cash_flow_sources_fq_h: list[float | None] | None = None
    other_investing_cash_flow_sources_fy: float | None = None
    other_investing_cash_flow_sources_fy_h: list[float | None] | None = None
    other_investing_cash_flow_sources_ttm: float | None = None
    other_investing_cash_flow_uses_fq: float | None = None
    other_investing_cash_flow_uses_fq_h: list[float | None] | None = None
    other_investing_cash_flow_uses_fy: float | None = None
    other_investing_cash_flow_uses_fy_h: list[float | None] | None = None
    other_investing_cash_flow_uses_ttm: float | None = None
    other_investments_fq: float | None = None
    other_investments_fq_h: list[float | None] | None = None
    other_investments_fy: float | None = None
    other_investments_fy_h: list[float | None] | None = None
    other_liabilities_total_fq: float | None = None
    other_liabilities_total_fq_h: list[float | None] | None = None
    other_liabilities_total_fy: float | None = None
    other_liabilities_total_fy_h: list[float | None] | None = None
    other_oper_expense_total_fq: float | None = None
    other_oper_expense_total_fq_h: list[float | None] | None = None
    other_oper_expense_total_fy: float | None = None
    other_oper_expense_total_fy_h: list[float | None] | None = None
    other_oper_expense_total_ttm: float | None = None
    other_proceeds_from_stock_sales_fq: float | None = None
    other_proceeds_from_stock_sales_fq_h: list[float | None] | None = None
    other_proceeds_from_stock_sales_fy: float | None = None
    other_proceeds_from_stock_sales_fy_h: list[float | None] | None = None
    other_receivables_fq: float | None = None
    other_receivables_fq_h: list[float | None] | None = None
    other_receivables_fy: float | None = None
    other_receivables_fy_h: list[float | None] | None = None
    other_short_term_debt_fy: float | None = None
    other_short_term_debt_fy_h: list[float | None] | None = None
    paid_in_capital_fq: float | None = None
    paid_in_capital_fq_h: list[float | None] | None = None
    paid_in_capital_fy: float | None = None
    paid_in_capital_fy_h: list[float | None] | None = None
    ppe_gross_buildings_fy: float | None = None
    ppe_gross_buildings_fy_h: list[float | None] | None = None
    ppe_gross_comp_soft_fy: float | None = None
    ppe_gross_comp_soft_fy_h: list[float | None] | None = None
    ppe_gross_construction_fy: float | None = None
    ppe_gross_construction_fy_h: list[float | None] | None = None
    ppe_gross_land_fy_h: list[Any | None] = None
    ppe_gross_leased_prop_fy_h: list[Any | None] = None
    ppe_gross_leases_fy: float | None = None
    ppe_gross_leases_fy_h: list[float | None] | None = None
    ppe_gross_machinery_fy_h: list[Any | None] = None
    ppe_gross_other_fy: float | None = None
    ppe_gross_other_fy_h: list[float | None] | None = None
    ppe_gross_trans_equip_fy_h: list[Any | None] = None
    ppe_total_gross_fq: float | None = None
    ppe_total_gross_fq_h: list[float | None] | None = None
    ppe_total_gross_fy: float | None = None
    ppe_total_gross_fy_h: list[float | None] | None = None
    ppe_total_net_fq: float | None = None
    ppe_total_net_fq_h: list[float | None] | None = None
    ppe_total_net_fy: float | None = None
    piotroski_f_score_fy: int | None = None
    ppe_total_net_fy_h: list[float | None] | None = None
    pre_tax_margin: float | None = None
    pre_tax_margin_current: float | None = None
    pre_tax_margin_fq: float | None = None
    pre_tax_margin_fq_h: list[float | None] | None = None
    pre_tax_margin_fy: float | None = None
    pre_tax_margin_fy_h: list[float | None] | None = None
    pretax_income_ttm: float | None = None
    pre_tax_margin_ttm: float | None = None
    preferred_dividends_cash_flow_fq_h: list[Any | None] = None
    preferred_dividends_cash_flow_fy: float | None = None
    preferred_dividends_cash_flow_fy_h: list[float | None] | None = None
    preferred_dividends_cash_flow_ttm: float | None = None
    preferred_dividends_fq_h: list[Any | None] = None
    preferred_dividends_fy: float | None = None
    preferred_dividends_fy_h: list[float | None] | None = None
    preferred_stock_carrying_value_fq: float | None = None
    preferred_stock_carrying_value_fq_h: list[float | None] | None = None
    preferred_stock_carrying_value_fy: float | None = None
    preferred_stock_carrying_value_fy_h: list[float | None] | None = None
    prepaid_expenses_fq: float | None = None
    popularity_rank: float | None = None
    prepaid_expenses_fq_h: list[float | None] | None = None
    prepaid_expenses_fy: float | None = None
    prepaid_expenses_fy_h: list[float | None] | None = None
    pretax_equity_in_earnings_fq: float | None = None
    pretax_equity_in_earnings_fq_h: list[float | None] | None = None
    pretax_equity_in_earnings_fy: float | None = None
    pretax_equity_in_earnings_fy_h: list[float | None] | None = None
    pretax_equity_in_earnings_ttm: float | None = None
    pretax_income_fq: float | None = None
    pretax_income_fq_h: list[float | None] | None = None
    pretax_income_fy: float | None = None
    price_target_date: str | None = None
    pretax_income_fy_h: list[float | None] | None = None
    price_annual_book: float | None = None
    price_annual_sales: float | None = None
    price_book_fq: float | None = None
    price_book_fq_h: list[float | None] | None = None
    price_book_fy_h: list[float | None] | None = None
    price_cash_flow_fq_h: list[Any | None] = None
    price_cash_flow_fy_h: list[Any | None] = None
    price_book_current: float | None = None
    price_earnings_fq_h: list[Any | None] = None
    price_earnings_fy_h: list[Any | None] = None
    price_sales_fq: float | None
    price_sales_fq_h: list[float | None] | None = None
    price_sales_fy_h: list[float | None] | None = None
    proceeds_from_stock_options_fq: float | None
    proceeds_from_stock_options_fq_h: list[float | None] | None = None
    proceeds_from_stock_options_fy: float | None = None
    price_target_estimates_num: int | None
    proceeds_from_stock_options_fy_h: list[float | None] | None = None
    provision_f_risks_fq: float | None
    provision_f_risks_fq_h: list[float | None] | None = None
    provision_f_risks_fy: float | None
    provision_f_risks_fy_h: list[float | None] | None = None
    purchase_of_business_fq: float | None
    purchase_of_business_fq_h: list[float | None] | None = None
    purchase_of_business_fy: float | None
    purchase_of_business_fy_h: list[float | None] | None = None
    purchase_of_business_ttm: float | None
    purchase_of_investments_fq: float | None
    purchase_of_investments_fq_h: list[float | None] | None = None
    purchase_of_investments_fy: float | None
    purchase_of_investments_ttm: float | None
    purchase_of_stock_fq: float | None
    purchase_of_stock_fq_h: list[float | None] | None = None
    purchase_of_stock_fy: float | None
    purchase_of_stock_fy_h: list[float | None] | None = None
    purchase_of_stock_ttm: float | None
    purchase_sale_business_fq: float | None
    purchase_sale_business_fq_h: list[float | None] | None = None
    purchase_sale_business_fy: float | None
    purchase_sale_business_fy_h: list[float | None] | None = None
    purchase_sale_business_ttm: float | None
    purchase_sale_investments_fq: float | None
    purchase_sale_investments_fq_h: list[float | None] | None = None
    purchase_sale_investments_fy: float | None
    purchase_sale_investments_fy_h: list[float | None] | None = None
    purchase_sale_investments_ttm: float | None
    quick_ratio_fq: float | None = None
    quick_ratio_fq_h: list[float | None] | None = None
    quick_ratio_fy: float | None = None
    quick_ratio_fy_h: list[float | None] | None = None
    receivables_turnover_fy: float | None = None
    receivables_turnover_fy: float | None = None
    reduction_of_long_term_debt_fq: float | None = None
    reduction_of_long_term_debt_fq_h: list[float | None] | None = None
    reduction_of_long_term_debt_fy: float | None = None
    reduction_of_long_term_debt_fy_h: list[float | None] | None = None
    reduction_of_long_term_debt_ttm: float | None = None
    region: str | None = None
    recommendation_date: str | None = None
    research_and_dev_fh: float | None = None
    research_and_dev_fq: float | None = None
    research_and_dev_fq_h: list[float | None] | None = None
    research_and_dev_fy: float | None = None
    research_and_dev_fy_h: list[float | None] | None = None
    research_and_dev_ttm: float | None = None
    restructuring_charge_fy: float | None = None
    report_type: str | None = None
    restructuring_charge_fy_h: list[float | None] | None = None
    retained_earnings_fq: float | None = None
    retained_earnings_fq_h: list[float | None] | None = None
    retained_earnings_fy: float | None = None
    retained_earnings_fy_h: list[float | None] | None = None
    return_of_invested_capital_percent_ttm: float | None = None
    return_on_assets_current: float | None = None
    return_on_assets_fq: float | None = None
    return_on_assets_fq_h: list[float | None] | None = None
    return_on_assets_fy: float | None = None
    return_on_assets_fy_h: list[float | None] | None = None
    return_on_capital_employed_fy: float | None = None
    return_on_common_equity_fy: float | None = None
    return_on_equity_adjust_to_book_fy: float | None = None
    return_on_common_equity_ttm: float | None = None
    return_on_equity_adjust_to_book_ttm: float | None = None
    return_on_equity_fq: float | None = None
    return_on_equity_fq_h: list[float | None] | None = None
    return_on_equity_fy: float | None = None
    return_on_equity_fy_h: list[float | None] | None = None
    return_on_invested_capital_fq: float | None = None
    return_on_invested_capital_fy: float | None = None
    return_on_invested_capital_current: float | None = None
    return_on_invested_capital_fy_h: list[float | None] | None = None
    return_on_tang_assets_fy: float | None = None
    return_on_tang_equity_fy: float | None = None
    return_on_total_capital_fq: float | None = None
    return_on_total_capital_fy: float | None = None
    revenue_forecast_fq: float | None = None
    revenue_forecast_fq_h: list[float | None] | None = None
    revenue_forecast_fy: float | None = None
    revenue_estimate_ntm: float | None = None
    revenue_forecast_fy_h: list[float | None] | None = None
    revenue_forecast_next_fh: float | None = None
    revenue_forecast_next_fq: float | None = None
    revenue_forecast_next_fy: float | None = None
    revenue_fq: float | None = None
    revenue_fq_h: list[float | None] | None = None
    revenue_per_employee: float | None = None
    revenue_fy: float | None = None
    revenue_fy_h: list[float | None] | None = None
    revenue_h: list[float] | None = Field(None, alias="total_revenue_h")
    revenue_per_employee_fy: float | None = None
    revenue_per_share_fq: float | None = None
    revenue_per_share_fq_h: list[float | None] | None = None
    revenue_per_share_fy: float | None = None
    revenue_per_share_current: float | None = None
    revenue_per_share_fy_h: list[float | None] | None = None
    rt_lag: datetime | None = Field(None, alias="rt-lag")
    rts_source: int | None = Field(None, alias="rts-source")
    sale_of_stock_fq: float | None = None
    sale_of_stock_fq_h: list[float | None] | None = None
    sale_of_stock_fy: float | None = None
    sale_of_stock_fy_h: list[float | None] | None = None
    sale_of_stock_ttm: float | None = None
    sales_of_business_fq: float | None = None
    sales_of_business_fq_h: list[float | None] | None = None
    sales_of_business_fy: float | None = None
    sales_of_business_fy_h: list[float | None] | None = None
    sales_of_investments_fq: float | None = None
    sales_of_investments_fq_h: list[float | None] | None = None
    sales_of_investments_fy: float | None = None
    sales_of_investments_fy_h: list[float | None] | None = None
    sales_of_investments_ttm: float | None = None
    sell_gen_admin_exp_other_fq: float | None = None
    sell_gen_admin_exp_other_fq_h: list[float | None] | None = None
    sell_gen_admin_exp_other_fy: float | None = None
    sell_gen_admin_exp_other_fy_h: list[float | None] | None = None
    sell_gen_admin_exp_other_ttm: float | None = None
    sell_gen_admin_exp_total_fq: float | None = None
    sell_gen_admin_exp_total_fq_h: list[float | None] | None = None
    sell_gen_admin_exp_total_fy: float | None = None
    sell_gen_admin_exp_total_fy_h: list[float | None] | None = None
    sell_gen_admin_exp_total_ttm: float | None = None
    session_correction: str | None = None
    series_key: str | None = Field(None, alias="series-key")
    share_buyback_ratio_fq: float | None = None
    share_buyback_ratio_fy: float | None = None
    short_term_debt_excl_current_port_fq: float | None = None
    short_term_debt_excl_current_port_fq_h: list[float | None] | None = None
    short_term_debt_excl_current_port_fy: float | None = None
    short_term_debt_excl_current_port_fy_h: list[float | None] | None = None
    short_term_debt_fq: float | None = None
    short_term_debt_fq_h: list[float | None] | None = None
    short_term_debt_fy: float | None = None
    short_term_debt_fy_h: list[float | None] | None = None
    short_term_invest_fq: float | None = None
    short_term_invest_fq_h: list[float | None] | None = None
    short_term_invest_fy: float | None = None
    short_term_invest_fy_h: list[float | None] | None = None
    shrhldrs_equity_fq: float | None = None
    shrhldrs_equity_fq_h: list[float | None] | None = None
    shrhldrs_equity_fy: float | None = None
    shrhldrs_equity_fy_h: list[float | None] | None = None
    sloan_ratio_fy: float | None = None
    sloan_ratio_ttm: float | None = None
    sum_for_enterprise_value: float | None = None
    supplying_of_long_term_debt_fq: float | None = None
    supplying_of_long_term_debt_fq_h: list[float | None] | None = None
    supplying_of_long_term_debt_fy: float | None = None
    supplying_of_long_term_debt_fy_h: list[float | None] | None = None
    supplying_of_long_term_debt_ttm: float | None = None
    tangible_assets_fq: float | None = None
    tangible_assets_fy: float | None = None
    tobin_q_ratio_fq: float | None = None
    tobin_q_ratio_fy: float | None = None
    total_revenue_ttm: float | None = None
    top_revenue_country_code: str | None = None
    total_assets: float | None = None
    total_assets_fq: float | None = None
    total_assets_fq_h: list[float | None] | None = None
    total_assets_fy: float | None = None
    total_assets_fy_h: list[float | None] | None = None
    total_assets_h: list[float] | None = None
    total_assets_per_employee_fy: float | None = None
    total_assets_to_equity_fq: float | None = None
    total_assets_to_equity_fy: float | None = None
    total_cash_dividends_paid_fh: float | None = None
    total_cash_dividends_paid_fq: float | None = None
    total_cash_dividends_paid_fq_h: list[float | None] | None = None
    total_cash_dividends_paid_fy: float | None = None
    total_cash_dividends_paid_fy_h: list[float | None] | None = None
    total_cash_dividends_paid_ttm: float | None = None
    total_current_assets: float | None = None
    total_current_assets_fq: float | None = None
    total_current_assets_fq_h: list[float | None] | None = None
    total_current_assets_fy: float | None = None
    total_current_assets_fy_h: list[float | None] | None = None
    total_current_assets_h: list[float | None] | None = None
    total_current_liabilities_fq: float | None = None
    total_current_liabilities_fq_h: list[float | None] | None = None
    total_current_liabilities_fy: float | None = None
    total_current_liabilities_fy_h: list[float | None] | None = None
    total_debt: float | None = None
    total_debt_fq: float | None = None
    total_debt_fq_h: list[float | None] | None = None
    total_debt_fy: float | None = None
    total_debt_fy_h: list[float | None] | None = None
    total_debt_h: list[float | None] | None = None
    total_debt_per_employee_fy: float | None = None
    total_debt_per_share_current: float | None = None
    total_debt_per_share_fq: float | None = None
    total_debt_per_share_fq_h: list[float | None] | None = None
    total_debt_per_share_fy: float | None = None
    total_debt_per_share_fy_h: list[float | None] | None = None
    total_debt_to_capital_fq: float | None = None
    total_debt_to_capital_fy: float | None = None
    total_equity_fq: float | None = None
    total_equity_fq_h: list[float | None] | None = None
    total_equity_fy: float | None = None
    total_equity_fy_h: list[float | None] | None = None
    total_extra_items_fq: float | None = None
    total_extra_items_fq_h: list[float | None] | None = None
    total_extra_items_fy: float | None = None
    total_extra_items_fy_h: list[float | None] | None = None
    total_extra_items_ttm: float | None = None
    total_inventory_fq: float | None = None
    total_inventory_fq_h: list[float | None] | None = None
    total_inventory_fy: float | None = None
    total_inventory_fy_h: list[float | None] | None = None
    total_liabilities_fq: float | None = None
    total_liabilities_fq_h: list[float | None] | None = None
    total_liabilities_fy: float | None = None
    total_liabilities_fy_h: list[float | None] | None = None
    total_liabilities_shrhldrs_equity_fq: float | None = None
    total_liabilities_shrhldrs_equity_fq_h: list[float | None] | None = None
    total_liabilities_shrhldrs_equity_fy: float | None = None
    total_liabilities_shrhldrs_equity_fy_h: list[float | None] | None = None
    total_non_current_assets_fq: float | None = None
    total_non_current_assets_fq_h: list[float | None] | None = None
    total_non_current_assets_fy: float | None = None
    total_non_current_assets_fy_h: list[float | None] | None = None
    total_non_current_liabilities_fq: float | None = None
    total_non_current_liabilities_fq_h: list[float | None] | None = None
    total_non_current_liabilities_fy: float | None = None
    total_non_current_liabilities_fy_h: list[float | None] | None = None
    total_non_oper_income_fq: float | None = None
    total_non_oper_income_fq_h: list[float | None] | None = None
    total_non_oper_income_fy: float | None = None
    total_non_oper_income_fy_h: list[float | None] | None = None
    total_non_oper_income_ttm: float | None = None
    total_oper_expense_fq: float | None = None
    total_oper_expense_fq_h: list[float | None] | None = None
    total_oper_expense_fy: float | None = None
    total_oper_expense_fy_h: list[float | None] | None = None
    total_oper_expense_ttm: float | None = None
    total_revenue_h: list[float] | None = None
    total_receivables_net_fq: float | None = None
    total_receivables_net_fq_h: list[float | None] | None = None
    total_receivables_net_fy: float | None = None
    total_receivables_net_fy_h: list[float | None] | None = None
    total_revenue_fh: float | None = None
    total_revenue_fq: float | None = None
    total_revenue_fq_h: list[float | None] | None = None
    total_revenue_fy: float | None = None
    total_revenue_fy_h: list[float | None] | None = None
    total_shares_outstanding_fq: float | None = None
    total_shares_outstanding_fq_h: list[float | None] | None = None
    total_shares_outstanding_fy: float | None
    total_shares_outstanding_fy_h: list[float | None] | None = None
    treasury_stock_common_fq: float | None = None
    treasury_stock_common_fq_h: list[float | None] | None = None
    treasury_stock_common_fy: float | None = None
    treasury_stock_common_fy_h: list[float | None] | None = None
    unrealized_gain_loss_fy: float | None = None
    unrealized_gain_loss_fy_h: list[float | None] | None = None
    unusual_expense_inc_fq: float | None = None
    unusual_expense_inc_fq_h: list[float | None] | None = None
    unusual_expense_inc_fy: float | None = None
    unusual_expense_inc_fy_h: list[float | None] | None = None
    working_capital_fq: float | None = None
    zmijewski_score_fy: float | None = None
    zmijewski_score_ttm: float | None = None
    working_capital_fy: float | None = None
    working_capital_per_share_current: float | None = None
    working_capital_per_share_fq: float | None = None
    working_capital_per_share_fq_h: list[float | None] | None = None
    working_capital_per_share_fy: float | None = None
    working_capital_per_share_fy_h: list[float | None] | None = None
    alt_prefixes: list[str] | None = Field(None, alias="alt-prefixes")
    basic_eps_net_income: float | None = None
    daily_confirm_offset: int | None = None
    ebitda: float | None = None
    earnings_publication_type_fq: int | None = None
    earnings_publication_type_fq_h: list[int] | None = None
    earnings_publication_type_fy: int | None = None
    earnings_publication_type_fy_h: list[int] | None = None
    earnings_publication_type_next_fq: int | None = None
    eps_estimate_ntm: float | None = None
    feed: str | None = None
    feed_has_dwm: bool | None = Field(None, alias="feed-has-dwm")
    feed_has_intraday: bool | None = Field(None, alias="feed-has-intraday")
    feed_ticker: str | None = Field(None, alias="feed-ticker")
    fiscal_period_current: str | None = None
    fiscal_period_end_fq: datetime | None = None
    fiscal_period_end_fq_h: list[datetime] | None = None
    fiscal_period_end_fy: datetime | None = None
    fiscal_period_end_fy_h: list[datetime] | None = None
    fiscal_period_fq: str | None = None
    fiscal_period_fy: str | None = None
    free_cash_flow: float | None = None

    class Config:
        extra = "allow"


class Figi(BaseModel):
    """Represents the Financial Instrument Global Identifier (FIGI)."""

    country_composite: str | None = Field(None, alias="country-composite")
    exchange_level: str | None = Field(None, alias="exchange-level")


class Source2(BaseModel):
    """Represents secondary source information."""

    country: str | None = None
    description: str | None = None
    exchange_type: str | None = Field(None, alias="exchange-type")
    id: str | None = None
    name: str | None = None
    url: str | None = None


class Subsession(BaseModel):
    """Represents a trading subsession (e.g., regular, premarket)."""

    description: str | None = None
    id: str | None = None
    private: bool | None = None
    session: str | None = None
    session_correction: str | None = Field(None, alias="session-correction")
    session_display: str | None = Field(None, alias="session-display")


class BarData(BaseModel):
    """Represents a single price bar (OHLCV)."""

    close: str | None = None
    data_update_time: datetime | None = Field(None, alias="data-update-time")
    high: str | None = None
    low: str | None = None
    open: str | None = None
    time: str | None = None
    update_time: datetime | None = Field(None, alias="update-time")
    volume: str | None = None


class TradeData(BaseModel):
    """Represents the last trade data."""

    data_update_time: str | None = Field(None, alias="data-update-time")
    price: str | None = None
    size: str | None = None
    time: str | None = None


class MarketStatus(BaseModel):
    """Represents the current market status."""

    phase: str | None = None
    tradingday: str | None = None


class Rates(BaseModel):
    """Represents currency conversion rates at a specific time."""

    time: datetime | None = None
    to_aud: float | None = None
    to_cad: float | None = None
    to_chf: float | None = None
    to_cny: float | None = None
    to_eur: float | None = None
    to_gbp: float | None = None
    to_inr: float | None = None
    to_jpy: float | None = None
    to_market: int | None = None
    to_symbol: int | None = None
    to_usd: int | None = None


class OptionSeries(BaseModel):
    """Represents a series of options for a specific expiration date."""

    exp: int | None = None
    id: str | None = None
    lotSize: int | None = None
    root: str | None = None
    strikes: list[float] | None = None
    underlying: str | None = None


class OptionFamily(BaseModel):
    """Represents a family of options (e.g., American style)."""

    description: str | None = None
    exercise: str | None = None
    name: str | None = None
    prefix: str | None = None
    series: list[OptionSeries] | None = None


class OptionsInfo(BaseModel):
    """Contains all information about available options for the symbol."""

    families: list[OptionFamily] | None = None


class FinancialReport(BaseModel):
    """Represents a single financial report line (e.g., revenue or earnings)."""

    Actual: float | None = None
    Estimate: float | None = None
    FiscalPeriod: str | None = None
    IsReported: bool | None = None
    Type: int | None = None


class RevenueSegment(BaseModel):
    """Represents a single segment of revenue (e.g., by business or region)."""

    label: str | None = None
    value: float | None = None


class RevenueBySegment(BaseModel):
    """Represents revenue broken down by segment for a specific date."""

    date: int | None = None
    segments: list[RevenueSegment] | None = None


class PermDetail(BaseModel):
    perm: str | None = None
    prefix: str | None = None


class Perms(BaseModel):
    delay: PermDetail | None = None
    rt: PermDetail | None = None
