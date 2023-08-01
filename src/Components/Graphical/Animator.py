from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from utils import *

if TYPE_CHECKING:
    from Core import DMUnit
################################################################################

__all__ = (
    "DMAnimator",
)

################################################################################
class DMAnimator:

    __slots__ = (
        "_parent",
        "_frame_idx",
        "_cooldown",
    )

    IDLE_COOLDOWN: float = 0.10  # 10 FPS

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, parent: DMUnit):

        self._parent: DMUnit = parent

        self._frame_idx: int = 0
        self._cooldown: float = 0.0

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def parent(self) -> DMUnit:

        return self._parent

################################################################################
    @property
    def frame_idx(self) -> int:

        return self._frame_idx

################################################################################
    @property
    def graphics_state(self) -> GraphicsState:

        return self.parent.graphics.state

################################################################################
##### GAME LOOP METHODS ########################################################
################################################################################
    def update(self, dt: float) -> None:

        self._cooldown += dt

        if self._cooldown >= self.IDLE_COOLDOWN:
            self.next_frame()
            self._cooldown = 0.0

################################################################################
##### PUBLIC METHODS ###########################################################
################################################################################
    def next_frame(self) -> None:

        self._frame_idx += 1

        if self._frame_idx >= len(self.parent.graphics.idle_frames):
            self._frame_idx = 0

################################################################################
    @staticmethod
    def copy(parent: DMUnit) -> DMAnimator:

        return DMAnimator(parent)

################################################################################
