import typing

import attr

from zenora.models.snowflake import Snowflake
from zenora.utils import get__str__

__all__: typing.Final[typing.List[str]] = ["Channel"]


@attr.s(slots=True)
class Channel:
    __str__ = get__str__

    id: Snowflake = attr.ib(converter=Snowflake)

    guild_id: Snowflake = attr.ib(converter=Snowflake)

    name: str = attr.ib()

    last_message_id: str = attr.ib()

    nsfw: bool = attr.ib()

    parent_id: str = attr.ib()

    type: int = attr.ib()

    position: int = attr.ib()

    permission_overwrites: list = attr.ib()

    topic: typing.Optional[str] = attr.ib(default=None)

    rate_limit_per_user: typing.Optional[int] = attr.ib(default=None)
