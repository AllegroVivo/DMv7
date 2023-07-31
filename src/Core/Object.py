from __future__ import annotations

from uuid import UUID, uuid4
from typing import TYPE_CHECKING, Optional

from utils import *

if TYPE_CHECKING:
    from Core import DMGame
################################################################################

__all__ = ("DMObject", )

################################################################################
class DMObject:

    __slots__ = (
        "_uuid",
        "_state",
        "_name",
        "_description",
        "_rank",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, state: DMGame, name: str, description: Optional[str] = None, rank: int = 0):

        self._uuid: UUID = uuid4()
        self._state: DMGame = state

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
    def obj_type(self) -> DMObjectType:

        return DMObjectType.Object

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

        return DMObject(self._state, self._name, self._description, self._rank)

################################################################################
