from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, Field, computed_field


class ProviderInfo(BaseModel):
    id: str
    name: str
    logo_id: str | None = None


class RelatedSymbol(BaseModel):
    symbol: str
    logoid: str | None = None


class NewsItem(BaseModel):
    id: str
    title: str
    published: int  # Unix timestamp
    urgency: int
    relatedSymbols: list[RelatedSymbol]
    storyPath: str
    provider: ProviderInfo

    @computed_field
    @property
    def published_dt(self) -> datetime:
        """The publication time as a timezone-aware datetime object."""
        return datetime.fromtimestamp(self.published, tz=timezone.utc)


class News(BaseModel):
    news: list[NewsItem] = Field(..., alias="items")
    pagination: dict[str, str] | None = Field(None, alias="pagination")


class MarketType(str, Enum):
    STOCKS = "stock"
    ETF = "etf"
    CRYPTO = "crypto"
    FOREX = "forex"
    INDICES = "index"
    FUTURES = "futures"
    OPTIONS = "options"
    ECONOMICS = "economic"
    BONDS = "bond"
    CORP_BONDS = "corp_bond"


class CorpActivity(str, Enum):
    CREDIT_RATINGS = "credit_ratings"
    DIVIDENDS = "dividends"
    EARNINGS = "earnings"
    ESG = "esg"
    INSIDER_TRADING = "insider_trading"
    IPO = "ipo"
    MANAGEMENT = "management"
    MERGERS_AND_ACQUISITIONS = "mergers_and_acquisitions"
    RECOMMENDATION = "recommendation"
    SHARE_BUYBACKS = "share_buybacks"
    STRATEGY_BUSINESS_PRODUCTS = "strategy_business_products"


class SecFilings(str, Enum):
    FORM_10K = "form_10k"
    FORM_10Q = "form_10q"
    FORM_4 = "form_4"


class Crypto(str, Enum):
    EXCHANGES = "exchanges"
    FUNDRAISING = "fundraising"
    MARKET_INSIGHTS = "market_insights"
    REGULATION = "regulation"
    SUPPLY_AND_LISTINGS = "supply_and_listings"
    TECHNOLOGY_AND_ADOPTION = "technology_and_adoption"


class Economics(str, Enum):
    BUSINESS = "business"
    CONSUMER = "consumer"
    GDP = "gdp"
    GOVERNMENT = "government"
    HEALTH = "health"
    HOUSING = "housing"
    LABOR = "labor"
    MONEY = "money"
    PRICES = "prices"
    TAXES = "taxes"
    TRADE = "trade"


class Region(str, Enum):
    GLOBAL = "WLD"
    NORTH_AMERICA = "NAM"
    CENTRAL_AMERICA = "CAM"
    SOUTH_AMERICA = "SAM"
    MIDDLE_EAST = "MEA"
    UK_IRELAND = "UKI"
    EUROPE = "EUR"
    ASIA = "ASI"
    OCEANIA = "OCN"
    AFRICA = "AFR"


class Provider(str, Enum):
    ESTATE_11TH = "11thestate"
    BITCOINS_99 = "99Bitcoins"
    ACCESWIRE = "acceswire"
    ACN = "acn"
    BARCHART = "barchart"
    BEINCRYPTO = "beincrypto"
    CME_GROUP = "cme_group"
    COINDAR = "coindar"
    COINMARKETCAL = "coinmarketcal"
    COINPEDIA = "coinpedia"
    COINTELEGRAPH = "cointelegraph"
    CONGRESSIONAL_QUARTERLY = "congressional_quarterly"
    CRYPTOBRIEFING = "cryptobriefing"
    CRYPTOGLOBE = "cryptoglobe"
    CRYPTONEWS = "cryptonews"
    CRYPTOPOTATO = "cryptopotato"
    CSE = "cse"
    DAILYFX = "dailyfx"
    DOW_JONES = "dow-jones"
    EQS = "eqs"
    ETFCOM = "etfcom"
    FINANCEMAGNATES = "financemagnates"
    FINANCIAL_JUICE = "financial_juice"
    FOREXLIVE = "forexlive"
    GURUFOCUS = "gurufocus"
    HSE = "hse"
    ICE = "ice"
    INVESTORPLACE = "investorplace"
    INVEZZ = "invezz"
    JCN = "jcn"
    LEVERAGE_SHARES = "leverage_shares"
    LSE = "lse"
    MACENEWS = "macenews"
    MARKET_WATCH = "market-watch"
    MARKETBEAT = "marketbeat"
    MARKETINDEX = "marketindex"
    MIRANDA_PARTNERS = "miranda_partners"
    MODULAR_FINANCE = "modular_finance"
    MONEYCONTROL = "moneycontrol"
    NBD = "nbd"
    NEWSBTC = "newsbtc"
    NEWSFILECORP = "newsfilecorp"
    OBI = "obi"
    POLISH_EMITENT = "polish_emitent"
    POLYMERUPDATE = "polymerupdate"
    PRESSETEXT = "pressetext"
    REUTERS = "reuters"
    RSE = "rse"
    SMALLCAPS = "smallcaps"
    STOCKNEWS = "stocknews"
    STOCKSTORY = "stockstory"
    THE_BLOCK = "the_block"
    THENEWSWIRE = "thenewswire"
    TLSE = "tlse"
    TODAYQ = "todayq"
    TRADING_ECONOMICS = "trading-economics"
    TRADINGVIEW = "tradingview"
    U_TODAY = "u_today"
    VALUEWALK = "valuewalk"
    ZACKS = "zacks"
    ZAWYA = "zawya"
    ZYCRYPTO = "zycrypto"


class Priority(str, Enum):
    FLASH = "flash"
    IMPORTANT = "important"
    KEY_FACTS = "key_facts"
    TOP_STORIES = "top_stories"


class Sentiment(str, Enum):
    NEGATIVE = "negative"
    POSITIVE = "positive"
