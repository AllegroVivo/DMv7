from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Type, TypeVar

from .Unit import DMUnit

if TYPE_CHECKING:
    from Core import DMGame
################################################################################

__all__ = ("DMMonster",)

M = TypeVar("M", bound="DMMonster")

################################################################################
class DMMonster(DMUnit):

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
        life: int,
        atk: int,
        defense: float,
    ):

        super().__init__(state, name, description, rank, life, atk, defense)

################################################################################
