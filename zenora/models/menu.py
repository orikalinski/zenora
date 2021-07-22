import typing

import attr

from zenora.models.button import Button
from zenora.utils import get__str__

__all__: typing.Final[typing.List[str]] = ["Menu"]


@attr.s(slots=True)
class Menu:
    __str__ = get__str__

    type = 1

    components: typing.List[typing.List[Button]] = attr.ib()

    def to_components(self):
        return [{"type": 1, "components": [button.to_dict() for button in row]}
                for row in self.components]
