from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Type, TypeVar, Union

from utils import *

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("DMStatComponent",)

S = TypeVar("S", bound="DMStatComponent")

################################################################################
class DMStatComponent:

    __slots__ = (
        "_type",
        "__base",
        "_value",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, base: Union[int, float], _type: StatComponentType):

        self._type: StatComponentType = _type
        self.__base: Union[int, float] = base

        self._value: Union[int, float] = base

################################################################################
##### INTERNAL METHODS #########################################################
################################################################################
    def __repr__(self) -> str:

        return (
            f"<DMStatComponent(current_value={self._value}, "
            f"component_type={self._type.name})>"
        )

################################################################################
    def __iadd__(self, other: Union[int, float]) -> S:

        self.increase(other)
        return self

################################################################################
    def __isub__(self, other: Union[int, float]) -> S:

        self.reduce(other)
        return self

################################################################################
    def __imul__(self, other: Union[int, float]) -> S:

        self.scale_up(other)
        return self

################################################################################
    def __idiv__(self, other: Union[int, float]) -> S:

        self.scale_down(other)
        return self

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def type(self) -> StatComponentType:

        return self._type

################################################################################
    @property
    def base(self) -> Union[int, float]:

        return self.__base

################################################################################
    @property
    def value(self) -> Union[int, float]:

        return self._value

################################################################################
##### STAT MODIFICATION ########################################################
################################################################################
    def increase(self, value: Union[int, float]) -> None:

        if not isinstance(value, (int, float)):
            raise TypeError("Invalid type passed to StatComponent.increase()")

        if self._type in (
                StatComponentType.Life, StatComponentType.Attack,
                StatComponentType.NumAttacks
        ):
            value = int(value)

        self._value += value

################################################################################
    def reduce(self, value: Union[int, float]) -> None:

        if not isinstance(value, (int, float)):
            raise TypeError("Invalid type passed to StatComponent.reduce()")

        if self._type in (
                StatComponentType.Life, StatComponentType.Attack,
                StatComponentType.NumAttacks
        ):
            value = int(value)

        self._value -= value

        if self._value < 0:
            self._value = 0

################################################################################
    def scale_up(self, value: float) -> None:

        if not isinstance(value, (int, float)):
            raise TypeError("Invalid type passed to StatComponent.scaleup()")

        self._value *= value

        if self._value < 0:
            self._value = 0

################################################################################
    def scale_down(self, value: float) -> None:

        if not isinstance(value, (int, float)):
            raise TypeError("Invalid type passed to StatComponent.scaledown()")

        self._value *= (1.0 - value)

        if self._value < 0:
            self._value = 0

################################################################################
    def copy(self) -> S:

        return type(self)(self.__base, self._type)

################################################################################
    def reset(self) -> None:

        self._value = self.__base

################################################################################
