from __future__ import annotations

import pygame

from typing import TYPE_CHECKING, List, Optional, Union

from Core.State import DMState
from States import _STATE_MAPPINGS

if TYPE_CHECKING:
    from pygame import Surface
    from pygame.event import Event

    from Core import DMGame
################################################################################

__all__ = ("DMStateMachine",)

################################################################################
class DMStateMachine:

    __slots__ = (
        "_game",
        "_states",
        "_previous_state",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, game: DMGame):

        self._game: DMGame = game

        self._states: List[DMState] = []
        self._previous_state: Optional[DMState] = None

################################################################################
##### INTERNAL METHODS #########################################################
################################################################################
    def __repr__(self) -> str:

        ret = f"<StateStackManager -- Stack breakdown from current to last:"
        count = 1

        for state in reversed(self._states):
            ret += f"\n{count}. {state}"
            count += 1

        return ret + ">"

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def game(self) -> DMGame:

        return self._game

################################################################################
    @property
    def previous_state(self) -> Optional[DMState]:

        return self._previous_state

################################################################################
    @property
    def current_state(self) -> DMState:

        return self._states[-1]

################################################################################
    @property
    def stack(self) -> List[DMState]:

        return self._states

################################################################################
##### STATE MANAGEMENT #########################################################
################################################################################
    def push(self, state: Union[str, DMState]) -> None:

        if isinstance(state, str):
            cls = _STATE_MAPPINGS.get(state)
            if cls:
                self._states.append(cls(self.game))
        elif isinstance(state, DMState):
            self._states.append(state)

################################################################################
    def pop(self) -> bool:

        if not self._states:
            return False

        self._previous_state = self._states.pop()

        return True

################################################################################
    def switch(self, state: Union[str, DMState]) -> None:

        if self._states:
            self._previous_state = self._states.pop()

        self.push(state)

################################################################################
##### GAME LOOP METHODS ########################################################
################################################################################
    def handle_event(self, event: Event) -> None:

        self.current_state.handle_event(event)

################################################################################
    def update(self, dt: float) -> None:

        if self._states:
            state = self.current_state
            state.update(dt)

            if state.quit:
                self._previous_state = self._states.pop()
                if not self._states:
                    self.game.quit()
            elif state.next_state:
                self.push(state.next_state)
                state.next_state = None

################################################################################
    def draw(self, screen: Surface) -> None:

        if self._states:
            # screen.fill(BLACK)
            self.current_state.draw(screen)

            pygame.display.flip()

################################################################################
