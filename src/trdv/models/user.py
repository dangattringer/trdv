from pydantic import BaseModel, Field


class UserModel(BaseModel):
    """
    Represents the authenticated user's data model received from the API.
    """

    id: int
    username: str
    email: str | None = None
    date_joined: str | None = None
    status: str | None = None
    ignore_list: list[int] | None = None
    has_phone: bool | None = None
    do_not_track: bool | None = None
    is_non_pro_confirmed: bool | None = None
    profile_data_filled: bool | None = None
    is_corporation_user: bool | None = None
    is_symphony: bool | None = None
    is_active_partner: bool | None = None
    is_broker: bool | None = None
    broker_plan: str | None = None
    badges: list | None = None
    permissions: dict | None = None
    is_staff: bool | None = None
    is_superuser: bool | None = None
    is_moderator: bool | None = None
    social_registration: bool | None = None
    userpic: str | None = None
    userpic_mid: str | None = None
    userpic_big: str | None = None
    private_channel: str | None = None
    settings: dict | None = None
    last_locale: str | None = None
    auth_token: str = Field(..., repr=False)
    sms_email: str | None = None
    pro_plan: str | None = None
    is_pro: bool | None = None
    is_expert: bool | None = None
    is_trial: bool | None = None
    is_lite_plan: bool | None = None
    had_pro: bool | None = None
    declared_status: str | None = None
    declared_status_timestamp: str | None = None
    force_to_complete_data: bool | None = None
    force_to_upgrade: bool | None = None
    market_profile_updated_timestamp: str | None = None
    pro_plan_days_left: int | None = None
    pro_plan_original_name: bool | None = None
    pro_being_cancelled: bool | None = None
    pro_plan_billing_cycle: bool | None = None
    trial_days_left: int | None = None
    trial_days_left_text: str | None = None
    is_support_available: bool | None = None
    must_change_password: bool | None = None
    must_change_tfa: bool | None = None
    session_hash: str | None = None
    notification_count: dict[str, dict] | None = None
    reputation: float | None = None
    max_user_language_reputation: float | None = None
    active_broker: str | None = None
    disallow_adding_to_private_chats: bool | None = None
    picture_url: str | None = None
    has_active_email: bool | None = None
