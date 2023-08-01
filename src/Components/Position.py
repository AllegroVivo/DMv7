from __future__ import annotations

from pygame import Vector2
from typing import TYPE_CHECKING, List, Optional, Type, TypeVar

if TYPE_CHECKING:
    from Core import DMUnit
################################################################################

__all__ = ("PositionComponent",)

P = TypeVar("P", bound="PositionComponent")

################################################################################
class PositionComponent:

    __slots__ = (
        "_parent",
        "_screen_pos",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, parent: DMUnit):

        self._parent: DMUnit = parent

        self._screen_pos: Vector2 = Vector2()

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def parent(self) -> DMUnit:

        return self._parent

################################################################################
    @property
    def screen_pos(self) -> Vector2:

        return self._screen_pos

################################################################################
##### PUBLIC METHODS ###########################################################
################################################################################
    def set_screen_pos(self, vector: Vector2 = None, *, x: int = None, y: int = None) -> None:

        if vector is not None:
            self._screen_pos = vector
        else:
            if x is None or y is None:
                raise ValueError(
                    "Either vector or (x, y) must be specified for screen_position."
                )
            self._screen_pos = Vector2(x, y)

################################################################################
