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

from utils import *

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
##### INITIALIZATION ###########################################################
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
###### GAME LOOP ###############################################################
################################################################################
    def run(self) -> None:

        # We have to call this down here so it doesn't run into conflicts with
        # the object pool up above.
        # self._dungeon._map._init_map()

        # Start the game in the main menu state.
        self._state.push("main_menu")

        # Main game loop.
        while self._running:
            # Check for events in the event queue.
            self.handle_events()

            # Update the current state.
            dt = self._clock.tick(FPS) / 1000
            self.update(dt)

            # Draw the current state.
            self.draw()

        # If we've exited the game loop, quit the game.
        self.quit()

################################################################################
    def handle_events(self) -> None:

        for event in pygame.event.get():
            # Handle quit events.
            if event.type == pygame.QUIT:
                self.quit()
            # And we'll make ESC quit the game as well.
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.quit()
            else:
                self._state.handle_event(event)

################################################################################
    def draw(self) -> None:

        self._state.draw(self._game_surf)
        self._logger.draw(self._log_surf)

        # Flip the display.
        pygame.display.flip()

################################################################################
    def update(self, dt: float) -> None:

        self._state.update(dt)

################################################################################
    def quit(self) -> None:

        self._running = False
        pygame.quit()

################################################################################
##### PROPERTIES ###############################################################
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
    def logger(self) -> DMLogManager:

        return self._logger

################################################################################
##### LOGGING ##################################################################
################################################################################
    def log(self, _obj: DMObject, msg: str) -> None:

        self._logger.game(_obj, msg)

################################################################################
