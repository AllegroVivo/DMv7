from __future__ import annotations

import pygame

from pygame import Surface, Vector2
from pygame.time import Clock
from typing import TYPE_CHECKING

from Core.Events import DMEventManager
from Core.Logger import DMLogManager
from Core.ObjPool import DMObjectPool
from Core.Random import DMGenerator
from Core.StateMachine import DMStateMachine

if TYPE_CHECKING:
    from Core import DMObject
################################################################################

__all__ = ("DMGame",)

################################################################################
class DMGame:

    __slots__ = (
        "_screen",
        "_game_surf",
        "_log_surf",
        "_clock",
        "_running",
        "_state",
        "_rng",
        "_objpool",
        "_events",
        "_logger",
    )

################################################################################
    def __init__(self):

        pygame.init()

        self._screen: Surface = pygame.display.set_mode((1024, 768))
        self._game_surf: Surface = pygame.Surface(
            (self._screen.get_width() * 0.80, 768)
        )
        self._log_surf: Surface = pygame.Surface(
            (self._screen.get_width() * 0.20, 768)
        )

        self._clock: Clock = pygame.time.Clock()
        self._running: bool = True

        self._logger: DMLogManager = DMLogManager(self)
        self._rng: DMGenerator = DMGenerator(self)
        self._objpool: DMObjectPool = DMObjectPool(self)
        self._state: DMStateMachine = DMStateMachine(self)
        self._events: DMEventManager = DMEventManager(self)

################################################################################
    def run(self) -> None:

        pass

################################################################################
    def quit(self) -> None:

        self._running = False
        pygame.quit()

################################################################################
    @property
    def game_surface(self) -> Surface:

        return self._game_surf

################################################################################
    @property
    def log_surface(self) -> Surface:

        return self._log_surf

################################################################################
    @property
    def rng(self) -> DMGenerator:

        return self._rng

################################################################################
    @property
    def objpool(self) -> DMObjectPool:

        return self._objpool

################################################################################
    @property
    def state(self) -> DMStateMachine:

        return self._state

################################################################################
    @property
    def events(self) -> DMEventManager:

        return self._events

################################################################################
    @property
    def running(self) -> bool:

        return self._running

################################################################################
    @property
    def log(self) -> DMLogManager:

        return self._logger

################################################################################
    def log_game(self, _obj: DMObject, msg: str) -> None:

        self._logger.log_game(_obj, msg)

################################################################################
    def log_engine(self, msg: str) -> None:

        self._logger.log_engine(msg)

################################################################################
