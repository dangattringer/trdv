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
