from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, model_validator


class NotificationCount(BaseModel):
    """
    Represents the count of notifications for the user.
    """

    following: dict[str, Any]
    user: dict[str, Any]


class UserModel(BaseModel):
    """
    Represents the authenticated user's data model.
    """

    id: int
    username: str
    date_joined: datetime
    status: str
    ignore_list: list[int]
    has_phone: bool
    do_not_track: bool
    is_non_pro_confirmed: bool
    profile_data_filled: bool
    is_corporation_user: bool
    is_symphony: bool
    is_active_partner: bool
    is_broker: bool
    broker_plan: str | None = None
    badges: list[Any]
    permissions: dict[str, Any]
    is_staff: bool
    is_superuser: bool
    is_moderator: bool
    social_registration: bool
    userpic: str
    userpic_mid: str
    userpic_big: str
    private_channel: str
    settings: dict[str, Any]
    last_locale: str
    auth_token: str = Field(..., repr=False)
    sms_email: str | None = None
    pro_plan: str
    is_pro: bool
    is_expert: bool
    is_trial: bool
    is_lite_plan: bool
    had_pro: bool
    declared_status: str
    declared_status_timestamp: datetime | None = None
    force_to_complete_data: bool
    force_to_upgrade: bool
    market_profile_updated_timestamp: datetime | None = None
    pro_plan_days_left: int
    pro_plan_original_name: bool
    pro_being_cancelled: bool | None = None
    pro_plan_billing_cycle: bool
    trial_days_left: int | None = None
    trial_days_left_text: str
    is_support_available: bool
    must_change_password: bool
    must_change_tfa: bool
    session_hash: str
    notification_count: NotificationCount
    reputation: float
    max_user_language_reputation: float
    active_broker: str | None = None
    disallow_adding_to_private_chats: bool
    picture_url: str
    has_active_email: bool


class User(BaseModel):
    """
    Represents the top-level API response for a user request.
    """

    error: str
    code: str | None = None
    user: UserModel | None = None

    @model_validator(mode="after")
    def check_user_on_success(self):
        """Ensure the user object exists if there is no error."""
        # if error is a non-empty string
        # user can be None
        if self.error:
            return self

        # If error is empty string
        # user must not be None
        if not self.user:
            raise ValueError("User object must be present when there is no error.")

        return self
