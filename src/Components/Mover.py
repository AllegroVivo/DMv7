from __future__ import annotations

from pygame import Vector2
from typing import TYPE_CHECKING, List, Optional, Type, TypeVar

if TYPE_CHECKING:
    from Core import DMUnit
################################################################################

__all__ = ("Mover",)

M = TypeVar("M", bound="Mover")

################################################################################
class Mover:

    __slots__ = (
        "_parent",
        "_direction",
        "_target_pos",
        "_moving",
    )

    DIRECTIONS = [Vector2(-1, 0), Vector2(1, 0), Vector2(0, -1), Vector2(0, 1)]

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, parent: DMUnit):

        self._parent: DMUnit = parent

        self._direction: Optional[Vector2] = None
        self._target_pos: Optional[Vector2] = None

        self._moving: bool = False

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def parent(self) -> DMUnit:

        return self._parent

################################################################################
    @property
    def direction(self) -> Optional[Vector2]:

        return self._direction

################################################################################
    @property
    def target_pos(self) -> Optional[Vector2]:

        return self._target_pos

################################################################################
    @property
    def moving(self) -> bool:

        return self._moving

################################################################################
    @property
    def screen_pos(self) -> Vector2:

        return self.parent.transform.position

################################################################################
    @screen_pos.setter
    def screen_pos(self, pos: Vector2) -> None:

        self.parent.transform.position = pos

################################################################################
##### PUBLIC METHODS ###########################################################
################################################################################
    def update(self, dt: float) -> None:

        if self._moving:
            self._move(dt)

################################################################################
    def move(self, direction: Vector2) -> None:

        if self._direction.x != 0:
            self.screen_pos.x += self._direction.x * HERO_SPEED * dt
        elif self._direction.y != 0:
            self.screen_pos.y += self._direction.y * HERO_SPEED * dt

################################################################################
    def set_target(self, pos: Vector2) -> None:

        self._target_pos = pos
        self._direction = (pos - self.parent.transform.position).normalize()
        self._moving = True

################################################################################
