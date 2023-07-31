from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Type, TypeVar

from .Stat import DMStatComponent
from utils import *

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("DMUnitStats",)

S = TypeVar("S", bound="DMUnitStats")

################################################################################
class DMUnitStats:

    __slots__ = (
        "_life",
        "_atk",
        "_def",
        "_dex",
        "_combat",
        "_attacks",
        "_speed",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, life: int = 1, attack: int = 1, defense: float = 1.0):

        self._life: DMStatComponent = DMStatComponent(life, StatComponentType.Life)
        self._atk: DMStatComponent = DMStatComponent(attack, StatComponentType.Attack)
        self._def: DMStatComponent = DMStatComponent(defense, StatComponentType.Defense)
        self._dex: DMStatComponent = DMStatComponent(1.0, StatComponentType.Dex)
        self._combat: DMStatComponent = DMStatComponent(1.0, StatComponentType.Combat)
        self._attacks: DMStatComponent = DMStatComponent(1, StatComponentType.NumAttacks)
        self._speed: DMStatComponent = DMStatComponent(1.0, StatComponentType.Speed)

################################################################################
##### INTERNAL METHODS #########################################################
################################################################################
    def __repr__(self) -> str:

        return (
            f"<DMUnitStats(life={self._life.value},\n"
            f"attack={self._atk.value},\n"
            f"defense={self._def.value},\n"
            f"dex={self._dex.value},\n"
            f"combat={self._combat.value},\n"
            f"attacks={self._attacks.value},\n"
            f"speed={self._speed.value})>"
        )

################################################################################
