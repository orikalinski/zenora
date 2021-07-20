import typing

import attr

from zenora.models.snowflake import Snowflake
from zenora.models.user import User
from zenora.utils import get__str__

__all__: typing.Final[typing.List[str]] = ["Message"]


@attr.s(slots=True)
class Message:
    __str__ = get__str__

    id: Snowflake = attr.ib(converter=Snowflake)

    channel_id: Snowflake = attr.ib(converter=Snowflake)

    author: User = attr.ib()

    content: str = attr.ib()

    type: int = attr.ib()

    embeds: list = attr.ib()

    attachments: list = attr.ib()

    components: list = attr.ib()

    flags: int = attr.ib()

    mention_everyone: bool = attr.ib()

    mention_roles: list = attr.ib()

    mentions: list = attr.ib()

    timestamp: str = attr.ib()

    pinned: bool = attr.ib()

    tts: bool = attr.ib()

    edited_timestamp: typing.Optional[str] = attr.ib(default=None)
