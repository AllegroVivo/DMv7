from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Dict, List, Type

if TYPE_CHECKING:
    from Core import DMGame
################################################################################

__all__ = ("DMEventManager", )

################################################################################
class DMEventManager:

    __slots__ = (
        "_state",
        "_events",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, state: DMGame):

        self._state: DMGame = state
        self._events: Dict[str, List[Callable]] = {}

################################################################################
##### GENERAL METHODS ##########################################################
################################################################################
    def subscribe(self, e: str, callback: Callable) -> None:

        if not callable(callback):
            raise TypeError("Invalid observer callback passed to EventManager.subscribe().")

        if callback in self._events[e]:
            return

        try:
            self._events[e].append(callback)
        except KeyError:
            self._events[e] = [callback]

################################################################################
    def unsubscribe(self, e: str, callback: Callable) -> None:

        if callback not in self._events[e]:
            return

        self._events[e].remove(callback)

################################################################################
    def notify(self, e: str, *ctx) -> None:

        if e not in self._events:
            raise TypeError(f"Invalid event name `{e}` passed to EventManager.dispatch().")

        for callback in self._events[e]:
            callback(*ctx)

################################################################################
