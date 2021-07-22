import typing

import attr

from zenora.models.snowflake import Snowflake
from zenora.utils import get__str__

__all__: typing.Final[typing.List[str]] = ["Button"]


@attr.s(slots=True)
class Button:
    __str__ = get__str__

    type = 2

    label: str = attr.ib()

    url: typing.Optional[str] = attr.ib(default=None)

    custom_id: typing.Optional[str] = attr.ib(default=None)

    def to_dict(self):
        data = {"type": self.type, "label": self.label, "style": 1}
        if self.custom_id:
            data["custom_id"] = self.custom_id
        if self.url:
            data["url"] = self.url
        return data
