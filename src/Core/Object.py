from __future__ import annotations

from uuid import UUID, uuid4
from typing import TYPE_CHECKING, Optional, Type, TypeVar

from Components import DMTransform
from utils import *

if TYPE_CHECKING:
    from Core import DMGame
    from Components import DMGraphical
################################################################################

__all__ = ("DMObject", )

O = TypeVar("O", bound="DMObject")

################################################################################
class DMObject:

    __slots__ = (
        "_uuid",
        "_state",
        "_name",
        "_description",
        "_rank",
        "_transform",
        "_graphical",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, state: DMGame, name: str, description: Optional[str], rank: int):

        self._uuid: UUID = uuid4()
        self._state: DMGame = state

        self._transform: DMTransform = DMTransform()
        self._graphical: Optional[DMGraphical] = None

        self._name: str = name
        self._description: Optional[str] = description
        self._rank: int = rank

################################################################################
##### INTERNAL METHODS #########################################################
################################################################################
    def __eq__(self, other: DMObject) -> bool:

        if not isinstance(other, DMObject):
            return False

        return self._uuid == other._uuid

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def game(self) -> DMGame:

        return self._state

################################################################################
    @property
    def id(self) -> str:

        return self._uuid.hex

################################################################################
    @property
    def name(self) -> str:

        return self._name

################################################################################
    @property
    def description(self) -> Optional[str]:

        return self._description

################################################################################
    @property
    def rank(self) -> int:

        return self._rank

################################################################################
    @property
    def transform(self) -> DMTransform:

        return self._transform

################################################################################
    @property
    def obj_type(self) -> DMObjectType:

        return DMObjectType.Object

################################################################################
    @property
    def graphics(self) -> DMGraphical:

        return self._graphical

################################################################################
##### IDENTIFICATION ###########################################################
################################################################################
    @staticmethod
    def is_monster() -> bool:

        return False

################################################################################
    @staticmethod
    def is_hero() -> bool:

        return False

################################################################################
    @staticmethod
    def is_room() -> bool:

        return False

################################################################################
    @staticmethod
    def is_skill() -> bool:

        return False

################################################################################
    @staticmethod
    def is_status() -> bool:

        return False

################################################################################
    @staticmethod
    def is_relic() -> bool:

        return False

################################################################################
##### PUBLIC METHODS ###########################################################
################################################################################
    def copy(self, **kwargs) -> DMObject:

        cls: Type[O] = type(self)
        new_obj = cls.__new__(cls)

        new_obj._uuid = uuid4()
        new_obj._state = self._state

        new_obj._transform = DMTransform()

        new_obj._name = self._name
        new_obj._description = self._description
        new_obj._rank = self._rank

        return new_obj

################################################################################
