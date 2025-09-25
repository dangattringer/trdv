class TrdvException(Exception):
    """Base exception for the trdv library."""


class AuthenticationError(TrdvException):
    """Raised for login failures."""


class CaptchaRequired(TrdvException):
    """
    Raised when a CAPTCHA is required to proceed with login.

    The user must manually solve the CAPTCHA in a browser and then use
    the Session.set_auth_cookies() method to proceed.

    Attributes:
        url (str): The URL to visit to solve the CAPTCHA.
    """

    def __init__(self, message: str, url: str):
        super().__init__(message)
        self.url = url


class RateLimitError(TrdvException):
    """Raised when the API rate limit is exceeded."""


class SymbolNotFound(TrdvException):
    """Raised when a symbol cannot be found."""
