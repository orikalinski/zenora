import typing

import attr

from zenora.models.snowflake import Snowflake
from zenora.utils import get__str__

__all__: typing.Final[typing.List[str]] = ["Guild"]


@attr.s(slots=True)
class Guild:
    __str__ = get__str__

    id: Snowflake = attr.ib(converter=Snowflake)

    name: str = attr.ib()

    nsfw: typing.Optional[bool] = attr.ib(default=None)

    topic: typing.Optional[str] = attr.ib(default=None)

    approximate_member_count: typing.Optional[int] = attr.ib(default=None)

    approximate_presence_count: typing.Optional[int] = attr.ib(default=None)

    rate_limit_per_user: typing.Optional[int] = attr.ib(default=None)

    afk_channel_id: typing.Optional[int] = attr.ib(default=None)

    afk_timeout: typing.Optional[int] = attr.ib(default=None)

    application_id: typing.Optional[int] = attr.ib(default=None)

    banner: typing.Optional[int] = attr.ib(default=None)

    default_message_notifications: typing.Optional[int] = attr.ib(default=None)

    description: typing.Optional[str] = attr.ib(default=None)

    discovery_splash: typing.Optional[int] = attr.ib(default=None)

    emojis: typing.Optional[list] = attr.ib(default=None)

    explicit_content_filter: typing.Optional[int] = attr.ib(default=None)

    features: typing.Optional[list] = attr.ib(default=None)

    icon: typing.Optional[str] = attr.ib(default=None)

    max_members: typing.Optional[int] = attr.ib(default=None)

    max_presences: typing.Optional[int] = attr.ib(default=None)

    max_video_channel_users: typing.Optional[int] = attr.ib(default=None)

    mfa_level: typing.Optional[int] = attr.ib(default=None)

    nsfw_level: typing.Optional[int] = attr.ib(default=None)

    owner_id: typing.Optional[str] = attr.ib(default=None)

    preferred_locale: typing.Optional[str] = attr.ib(default=None)

    premium_subscription_count: typing.Optional[int] = attr.ib(default=None)

    premium_tier: typing.Optional[int] = attr.ib(default=None)

    public_updates_channel_id: typing.Optional[int] = attr.ib(default=None)

    region: typing.Optional[str] = attr.ib(default=None)

    roles: typing.Optional[list] = attr.ib(default=None)

    rules_channel_id: typing.Optional[int] = attr.ib(default=None)

    splash: typing.Optional[int] = attr.ib(default=None)

    stickers: typing.Optional[list] = attr.ib(default=None)

    system_channel_flags: typing.Optional[int] = attr.ib(default=None)

    system_channel_id: typing.Optional[str] = attr.ib(default=None)

    vanity_url_code: typing.Optional[int] = attr.ib(default=None)

    verification_level: typing.Optional[int] = attr.ib(default=None)

    widget_channel_id: typing.Optional[int] = attr.ib(default=None)

    widget_enabled: typing.Optional[bool] = attr.ib(default=None)
