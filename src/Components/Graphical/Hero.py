from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type, TypeVar

import pygame
from pygame import Surface

from .Graphical import DMGraphicalComponent
from utils import *

if TYPE_CHECKING:
    from Core import DMHero
################################################################################

__all__ = ("DMHeroGraphics",)

G = TypeVar("G", bound="DMHeroGraphics")

################################################################################
class DMHeroGraphics(DMGraphicalComponent):

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
    def death_sprite(self) -> Optional[Surface]:

        return self._death

################################################################################
    @property
    def subdir(self) -> str:

        return "heroes"

################################################################################
    @property
    def current_sprite(self) -> Optional[Surface]:

        match self.state:
            case GraphicsState.Death:
                return self.death_sprite
            case _:
                return super().current_sprite

################################################################################
##### METHODS ##################################################################
################################################################################
    def draw(self, surface: Surface) -> None:

        super().draw(surface)

################################################################################
    def copy(self, parent: DMHero) -> DMHeroGraphics:

        new_obj: Type[G] = super().copy(parent)  # type: ignore

        new_obj._death = self._death.copy()

        return new_obj

################################################################################
    def display_death(self) -> None:

        self._state = GraphicsState.Death

################################################################################
