from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Type, TypeVar

from .Unit import DMUnit

if TYPE_CHECKING:
    from Core import DMGame
################################################################################

__all__ = ("DMHero",)

H = TypeVar("H", bound="DMHero")

################################################################################
class DMHero(DMUnit):

    __slots__ = (

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
    ):

        super().__init__(state, name, description, rank, 1, 1, 1.0)

################################################################################
