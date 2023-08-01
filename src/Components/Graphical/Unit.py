from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Type, TypeVar

import pygame
from pygame import Surface

from .Graphical import DMGraphicalComponent
from utils import *

if TYPE_CHECKING:
    from Core import DMUnit
################################################################################

__all__ = ("DMUnitGraphics",)

G = TypeVar("G", bound="DMUnitGraphical")

################################################################################
class DMUnitGraphics(DMGraphicalComponent):

    __slots__ = (
        "_idle_frames",
        "_idle_idx",
        "_spritesheet",
        "_attack",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, parent: DMUnit):

        self._attack: Surface = None  # type: ignore
        self._spritesheet: Surface = None  # type: ignore

        self._idle_frames: List[Surface] = []
        self._idle_idx: int = 0

        # Call this second so the _load_sprites() call doesn't fail.
        super().__init__(parent)

################################################################################
    def _load_sprites(self) -> None:

        super()._load_sprites()

        self._attack = pygame.image.load(f"{self.asset_dir}/attack.png")

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def idle_sprite(self) -> Optional[Surface]:

        return self._idle_frames[self.parent.animator.frame_idx]

################################################################################
    @property
    def attack_sprite(self) -> Optional[Surface]:

        return self._attack

################################################################################
    @property
    def subdir(self) -> str:

        return ""

################################################################################
    @property
    def current_sprite(self) -> Optional[Surface]:

        match self.state:
            case GraphicsState.Attack:
                return self.attack_sprite
            case GraphicsState.Idle:
                return self.idle_sprite
            case _:
                return super().current_sprite

################################################################################
    @property
    def idle_frames(self) -> List[Surface]:

        return self._idle_frames

################################################################################
##### METHODS ##################################################################
################################################################################
    def draw(self, surface: Surface) -> None:

        super().draw(surface)

################################################################################
    def advance_frame(self) -> None:

        self._idle_idx += 1
        if self._idle_idx >= len(self._idle_frames):
            self._idle_idx = 0

################################################################################
    def copy(self, parent: DMUnit) -> DMUnitGraphics:

        new_obj: Type[G] = super().copy(parent)  # type: ignore

        new_obj._attack = self._attack.copy() if self._attack else None
        new_obj._spritesheet = self._spritesheet.copy() if self._spritesheet else None
        new_obj._idle_frames = [frame.copy() for frame in self._idle_frames]

        return new_obj

################################################################################
    def display_idle(self) -> None:

        self._idle_idx = 0
        self._state = GraphicsState.Idle

################################################################################
    def display_attack(self) -> None:

        self._state = GraphicsState.Attack

################################################################################
