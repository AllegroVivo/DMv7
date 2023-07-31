from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import pygame
from pygame import Surface

from .Graphical import DMGraphicalComponent

if TYPE_CHECKING:
    from Core import DMHero
################################################################################

__all__ = ("DMMonsterGraphics",)

################################################################################
class DMMonsterGraphics(DMGraphicalComponent):

    __slots__ = (
        "_death",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, parent: DMHero):

        self._death: Optional[Surface] = None

        # Call this second so the _load_sprites() call doesn't fail.
        super().__init__(parent)

################################################################################
    def _load_sprites(self) -> None:

        # Abstract method - so it requires a basic implementation.
        super()._load_sprites()

        self._death = pygame.image.load(f"{self.asset_dir}/death.png")

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def subdir(self) -> str:

        return "heroes"

################################################################################
##### METHODS ##################################################################
################################################################################
    def draw(self, surface: Surface) -> None:

        super().draw(surface)

################################################################################
