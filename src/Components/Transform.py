from __future__ import annotations

from pygame import Vector2
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    pass
################################################################################

__all__ = (
    "DMTransform",
)

################################################################################
class DMTransform:

    __slots__ = (
        "_parent",
        "_position",
        "_rotation",
        "_scale",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(
        self,
        position: Vector2 = Vector2(0, 0),
        rotation: float = 0.0,
        scale: Vector2 = Vector2(1, 1),
        parent: Optional[DMTransform] = None
    ):

        self._parent: Optional[DMTransform] = parent

        self._position: Vector2 = position
        self._rotation: float = rotation
        self._scale: Vector2 = scale

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def parent(self) -> Optional[DMTransform]:

        return self._parent

################################################################################
    @property
    def position(self) -> Vector2:

        return self._position

################################################################################
    @property
    def rotation(self) -> float:

        return self._rotation

################################################################################
    @property
    def scale(self) -> Vector2:

        return self._scale

################################################################################
##### PUBLIC METHODS ###########################################################
################################################################################
    def translate(self, translation: Vector2) -> None:

        self._position += translation

################################################################################
    def rotate(self, rotation: float) -> None:

        self._rotation += rotation

################################################################################
    def enlarge(self, scale: Vector2) -> None:

        self._scale *= scale

################################################################################
    def shrink(self, scale: Vector2) -> None:

        self._scale /= scale

################################################################################
