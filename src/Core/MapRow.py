from __future__ import annotations

from pygame import Surface
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from Core import DMGame, DMRoom
################################################################################

__all__ = ("DMMapRow",)

################################################################################
class DMMapRow:

    __slots__ = (
        "_state",
        "_row_idx",
        "_rooms",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, game: DMGame, index: int):

        self._state: DMGame = game

        self._row_idx: int = index
        self._rooms: List[DMRoom] = []

################################################################################
##### INTERNAL METHODS #########################################################
################################################################################
    def __getitem__(self, item: int) -> Optional[DMRoom]:

        try:
            return self._rooms[item]
        except IndexError:
            return

################################################################################
    def __len__(self) -> int:

        return len(self._rooms)

################################################################################
##### PROPERTIES ################################################################
################################################################################
    @property
    def game(self) -> DMGame:

        return self._state

################################################################################
##### GAME LOOP METHODS ########################################################
################################################################################
    def draw(self, surface: Surface) -> None:

        for room in self._rooms:
            if room is not None:
                room.draw(surface)

################################################################################
