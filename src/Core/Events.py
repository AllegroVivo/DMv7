from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Dict, List

from src.Events import _EVENT_REFERENCE

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("DMEventManager", )

################################################################################
class DMEventManager:

    __slots__ = (
        "_state",
        "_events",
    )

################################################################################
    def __init__(self, state: DMGame):

        self._state: DMGame = state

        self._events: Dict[str, List[Callable]] = {}
        self._init_event_dict()

################################################################################
    def _init_event_dict(self) -> None:

        for event in _EVENT_REFERENCE:
            self._events[event] = []

################################################################################
