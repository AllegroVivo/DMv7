from __future__ import annotations

import pygame

from pygame import Surface, Vector2
from pygame.time import Clock
from typing import TYPE_CHECKING

from Core import DMGenerator, DMObjectPool, DMEventManager, DMStateMachine

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("DMGame",)

################################################################################
class DMGame:

    __slots__ = (
        "_screen",
        "_clock",
        "_running",
        "_state",
        "_rng",
        "_objpool",
        "_events",
    )

################################################################################
    def __init__(self):

        pygame.init()

        self._screen: Surface = pygame.display.set_mode((1024, 768))
        self._clock: Clock = pygame.time.Clock()
        self._running: bool = True

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
