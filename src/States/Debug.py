from __future__ import annotations

from typing import TYPE_CHECKING

from pygame import Surface
from pygame.event import Event

from Core.State import DMState

if TYPE_CHECKING:
    from Core.Game import DMGame
################################################################################

__all__ = ("DebugState",)

################################################################################
class DebugState(DMState):

    def __init__(self, game: DMGame):

        super().__init__(game)

################################################################################
    def handle_event(self, event: Event) -> None:

        pass

################################################################################
    def update(self, dt: float) -> None:

        pass

################################################################################
    def draw(self, screen: Surface) -> None:

        pass

################################################################################
