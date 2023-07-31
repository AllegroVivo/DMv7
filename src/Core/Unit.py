from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Type, TypeVar

from Components import DMTransform
from Core.Object import DMObject

if TYPE_CHECKING:
    from Core import DMGame
################################################################################

__all__ = ("DMUnit",)

M = TypeVar("M", bound="DMMonster")

################################################################################
class DMUnit(DMObject):

    __slots__ = (
        "_stats",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(
        self,
        state: DMGame,
        name: str,
        description: Optional[str],
        rank: int
    ):

        super().__init__(state, name, description, rank)

        self._stats: DMStats = DMStats()