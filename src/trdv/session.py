import logging

import aiohttp
from pydantic import ValidationError
from yarl import URL

from .const import TRADINGVIEW_LOGIN_URL, USER_AGENTS
from .exceptions import AuthenticationError, CaptchaRequired
from .models import User, UserModel

logger = logging.getLogger(__name__)


class Session:
    """Manages user authentication state and the login workflow."""

    def __init__(self, username: str | None = None, password: str | None = None):
        """
        Initializes the session with user credentials.

        Args:
            username: The TradingView username.
            password: The TradingView password.
        """
        self.username = username
        self.__password = password
        self._cookie_jar = aiohttp.CookieJar()
        self._authenticated = False
        self._headers = {
            "User-Agent": USER_AGENTS["chrome"][0],
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.tradingview.com/",
            "Origin": "https://www.tradingview.com",
        }
        self._user: User | None = None

    @property
    def is_authenticated(self) -> bool:
        """Returns True if the session has successfully authenticated."""
        return self._authenticated

    @property
    def user(self) -> User | None:
        """Returns the user information if available."""
        return self._user

    async def login(self):
        """
        Attempts to programmatically log in to TradingView.

        If successful, the session will be marked as authenticated, and the necessary
        cookies will be stored for subsequent requests.

        Raises:
            AuthenticationError: If login fails due to invalid credentials or other errors.
            CaptchaRequired: If the login attempt is blocked by a CAPTCHA challenge.
        """
        if not self.username or not self.__password:
            raise AuthenticationError(
                "username and password must be provided for login."
            )

        payload = {
            "username": self.username,
            "password": self.__password,
            "remember": True,
        }

        async with aiohttp.ClientSession(cookie_jar=self._cookie_jar) as session:
            async with session.post(
                TRADINGVIEW_LOGIN_URL, data=payload, headers=self._headers
            ) as resp:
                if resp.content_type != "application/json":
                    if 400 <= resp.status < 600:
                        raise AuthenticationError(
                            f"Login failed with HTTP status {resp.status}."
                        )
                    raise AuthenticationError(
                        f"Unexpected content type: {resp.content_type}"
                    )
                data = await resp.json()
                logger.debug(f"Login response data: {data}")

                try:
                    response_data = UserModel(**data)
                except ValidationError as e:
                    logger.error(f"Failed to parse API response: {e}")
                    raise AuthenticationError(
                        "Login failed: Invalid data received from API."
                    ) from e

                if response_data.error:
                    if response_data.code == "recaptcha_required":
                        logger.warning(
                            "CAPTCHA challenge detected. Directing user to manual login."
                        )
                        raise CaptchaRequired(
                            "CAPTCHA challenge detected. Login currently not supported."
                            " In future versions, you may be directed to a browser login.",
                            url=TRADINGVIEW_LOGIN_URL,
                        )
                    raise AuthenticationError(response_data.error)

                self._user = response_data.user
                self._authenticated = True
                logger.info("Login successful")
                return

    def set_auth_cookies(self, cookies: str):
        """Manually sets the necessary authentication cookies after a browser login."""
        cookies_to_set = {}
        for cookie in cookies.split("; "):
            key, value = cookie.split("=", 1)
            cookies_to_set[key] = value

        self._cookie_jar.update_cookies(
            cookies_to_set, response_url=URL("https://www.tradingview.com/")
        )
        logger.info(
            "Authentication cookies set manually. The session is authenticated."
        )
