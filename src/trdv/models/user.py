from typing import Optional
from pydantic import BaseModel, Field


class UserModel(BaseModel):
    """
    Represents the authenticated user's data model received from the API.
    """

    id: int
    username: str
    email: str | None = None
    date_joined: str
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
    broker_plan: Optional[str] = None
    badges: list
    permissions: dict
    is_staff: bool
    is_superuser: bool
    is_moderator: bool
    social_registration: bool
    userpic: str
    userpic_mid: str
    userpic_big: str
    private_channel: str
    settings: dict
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
    declared_status_timestamp: str | None = None
    force_to_complete_data: bool
    force_to_upgrade: bool
    market_profile_updated_timestamp: str | None = None
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
    notification_count: dict[str, dict]
    reputation: float
    max_user_language_reputation: float
    active_broker: str | None = None
    disallow_adding_to_private_chats: bool
    picture_url: str
    has_active_email: bool
