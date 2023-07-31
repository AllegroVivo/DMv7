from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import pygame
from pygame import Surface

from .Graphical import DMGraphicalComponent

if TYPE_CHECKING:
    from Core import DMMonster
################################################################################

__all__ = ("DMMonsterGraphics",)

################################################################################
class DMMonsterGraphics(DMGraphicalComponent):

    __slots__ = (
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def _load_sprites(self) -> None:

        # Abstract method - so it requires a basic implementation.
        super()._load_sprites()

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def subdir(self) -> str:

        return "monsters"

################################################################################
##### METHODS ##################################################################
################################################################################
    def draw(self, surface: Surface) -> None:

        super().draw(surface)

################################################################################
