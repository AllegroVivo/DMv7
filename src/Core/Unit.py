from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Type, TypeVar

from Components import DMUnitStats, DMAnimator
from Core.Object import DMObject

if TYPE_CHECKING:
    from Components import DMUnitGraphics
    from Core import DMGame
################################################################################

__all__ = ("DMUnit",)

M = TypeVar("M", bound="DMMonster")

################################################################################
class DMUnit(DMObject):

    __slots__ = (
        "_stats",
        "_animator",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(
        self,
        state: DMGame,
        name: str,
        description: Optional[str],
        rank: int,
        life: int,
        atk: int,
        defense: float,
    ):

        super().__init__(state, name, description, rank)

        self._stats: DMUnitStats = DMUnitStats(life, atk, defense)
        self._animator: DMAnimator = DMAnimator(self)

################################################################################
##### INTERNAL METHODS #########################################################
################################################################################

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def graphics(self) -> DMUnitGraphics:

        return self._graphical

################################################################################
