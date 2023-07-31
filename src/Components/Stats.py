from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Type, TypeVar

from

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("DMUnitStats",)

S = TypeVar("S", bound="DMUnitStats")

################################################################################
class DMUnitStats:

    __slots__ = (
        "_life",
        "_atk"
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