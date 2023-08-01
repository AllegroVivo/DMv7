from __future__ import annotations

import pygame

from abc import ABC, abstractmethod
from pygame     import Surface, Vector2
from typing     import TYPE_CHECKING, Optional, Type, TypeVar, Union

from utils import *

if TYPE_CHECKING:
    from Core import DMObject, DMGame, DMHero, DMMonster, DMRoom, DMUnit
################################################################################

__all__ = ("DMGraphicalComponent",)

GC = TypeVar("GC", bound="DMGraphicalComponent")

################################################################################
class DMGraphicalComponent:

    __slots__ = (
        "_parent",
        "_static",
        "_zoom",
        "_state",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, parent: DMObject):

        self._parent: DMObject = parent

        self._static: Surface = None  # type: ignore
        self._zoom: Surface = None  # type: ignore

        self._state: GraphicsState = GraphicsState.Idle

        self._load_sprites()

################################################################################
    @abstractmethod
    def _load_sprites(self) -> None:

        self._static = pygame.image.load(f"{self.asset_dir}/static.png")
        self._zoom = pygame.image.load(f"{self.asset_dir}/zoom.png")

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def game(self) -> DMGame:

        return self._parent.game

################################################################################
    @property
    def parent(self) -> Union[DMObject, DMHero, DMMonster, DMRoom, DMUnit]:

        return self._parent

################################################################################
    @property
    def static_sprite(self) -> Optional[Surface]:

        return self._static

################################################################################
    @property
    def zoom_sprite(self) -> Optional[Surface]:

        return self._zoom

################################################################################
    @property
    def asset_dir(self) -> str:

        return f"assets/sprites/{self.subdir}/{class_to_file_name(self._parent)}"

################################################################################
    @property
    @abstractmethod
    def subdir(self) -> str:

        raise NotImplementedError

################################################################################
    @property
    def state(self) -> GraphicsState:

        return self._state

################################################################################
    @property
    def screen_pos(self) -> Vector2:

        return self._parent.transform.position

################################################################################
    @property
    def current_sprite(self) -> Optional[Surface]:

        match self._state:
            case GraphicsState.Static:
                return self.static_sprite
            case GraphicsState.Zoom:
                return self.zoom_sprite
            case _:
                raise TypeError("Invalid enum value passed to Graphical.current_sprite")

################################################################################
##### GENERAL METHODS ##########################################################
################################################################################
    @abstractmethod
    def draw(self, screen: Surface) -> None:

        raise NotImplementedError

################################################################################
    @abstractmethod
    def copy(self, parent: DMObject) -> DMGraphicalComponent:

        cls: Type[GC] = type(self)
        new_obj = cls.__new__(cls)

        new_obj._parent = parent

        new_obj._static = self._static.copy() if self._static is not None else None
        new_obj._zoom = self._zoom.copy() if self._zoom is not None else None

        return new_obj

################################################################################
    def display_static(self) -> None:

        self._state = GraphicsState.Static

################################################################################
    def display_zoom(self) -> None:

        self._state = GraphicsState.Zoom

################################################################################
