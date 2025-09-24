class TrdvException(Exception):
    """Base exception for the trdv library."""


class SymbolNotFound(TrdvException):
    """Raised when a symbol cannot be found."""


class AuthenticationError(TrdvException):
    """Raised for login failures."""


class RateLimitError(TrdvException):
    """Raised when the API rate limit is exceeded."""
