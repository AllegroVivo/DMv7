from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union

from utils import *
from .Stat import DMStatComponent

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("DMLifeComponent",)

L = TypeVar("L", bound="DMLifeComponent")

################################################################################
class DMLifeComponent(DMStatComponent):

    __slots__ = (
        "_max",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, base: Union[int, float], _type: StatComponentType):

        super().__init__(base, _type)

        self._max: int = int(base)

################################################################################
##### INTERNAL METHODS #########################################################
################################################################################
    def __repr__(self) -> str:

        return f"<DMLifeComponent(value={self._value}/{self._max})>"

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def max(self) -> int:

        return self._max

################################################################################
##### STAT MODIFICATION ########################################################
################################################################################
    def restore(self) -> None:

        self._value = self._max

################################################################################
    def reset(self) -> None:

        self._value = self.__base
        self._max = int(self.__base)

################################################################################
