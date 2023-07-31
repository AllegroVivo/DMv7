from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import pygame
from pygame import Surface

from .Graphical import DMGraphicalComponent

if TYPE_CHECKING:
    from Core import DMMonster
################################################################################

__all__ = ("DMUnitGraphics",)

################################################################################
class DMUnitGraphics(DMGraphicalComponent):

    __slots__ = (
        "_attack",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, parent: DMMonster):

        self._attack: Optional[Surface] = None

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
    def attack_sprite(self) -> Optional[Surface]:

        return self._attack

################################################################################
    @property
    def subdir(self) -> str:

        return ""

################################################################################
##### METHODS ##################################################################
################################################################################
    def draw(self, surface: Surface) -> None:

        super().draw(surface)

################################################################################
