from enum import Enum


class Interval(Enum):
    """Represents time intervals for historical data."""

    # Minute intervals
    MIN_1 = "1"
    MIN_2 = "2"
    MIN_3 = "3"
    MIN_5 = "5"
    MIN_10 = "10"
    MIN_15 = "15"
    MIN_30 = "30"
    MIN_45 = "45"

    # Hourly intervals
    HOUR_1 = "60"
    HOUR_2 = "120"
    HOUR_3 = "180"
    HOUR_4 = "240"

    # Daily, Weekly, Monthly intervals
    DAY = "1D"
    WEEK = "1W"
    MONTH = "1M"
    MONTH_3 = "3M"
    MONTH_6 = "6M"
    MONTH_12 = "12M"

    def __str__(self) -> str:
        """Return the string value when converted to string."""
        return self.value


class MessageType(Enum):
    """WebSocket message types for TradingView communication."""

    # Connection management
    SET_AUTH_TOKEN = "set_auth_token"
    CHART_CREATE_SESSION = "chart_create_session"
    QUOTE_CREATE_SESSION = "quote_create_session"

    # Symbol operations
    RESOLVE_SYMBOL = "resolve_symbol"
    CREATE_SERIES = "create_series"
    MODIFY_SERIES = "modify_series"
    REMOVE_SERIES = "remove_series"
    SERIES_COMPLETED = "series_completed"
    SERIES_LOADING = "series_loading"
    SYMBOL_RESOLVED = "symbol_resolved"
    TIMESCALE_UPDATE = "timescale_update"

    # Data requests
    REQUEST_MORE_DATA = "request_more_data"
    QUOTE_ADD_SYMBOLS = "quote_add_symbols"
    QUOTE_REMOVE_SYMBOLS = "quote_remove_symbols"
    QUOTE_FAST_SYMBOLS = "quote_fast_symbols"

    # Study/indicator operations
    CREATE_STUDY = "create_study"
    MODIFY_STUDY = "modify_study"
    REMOVE_STUDY = "remove_study"

    # Session management
    SWITCH_TIMEZONE = "switch_timezone"
    SET_FIELDS = "set_fields"

    # Error handling
    PROTOCOL_ERROR = "protocol_error"

    def __str__(self) -> str:
        """Return the string value when converted to string."""
        return self.value


class SessionType(Enum):
    """Session types for different data streams."""

    CHART = "chart"
    QUOTE = "quote"
    STUDY = "study"
