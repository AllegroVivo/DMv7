from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID, uuid4

if TYPE_CHECKING:
    from Core import DMGame
################################################################################

__all__ = ("DMContext", )

################################################################################
class DMContext:

    __slots__ = (
        "_state",
        "_id",
    )

################################################################################
    def __init__(self, state: DMGame):

        self._state: DMGame = state
        self._id: UUID = uuid4()

################################################################################
