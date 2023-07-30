from typing import TYPE_CHECKING, Dict, Type

if TYPE_CHECKING:
    from Core.State import DMState
################################################################################

__all__ = [
    "_STATE_MAPPINGS",
]

################################################################################
# Modules
from .Debug import DebugState

################################################################################
_STATE_MAPPINGS: Dict[str, Type["DMState"]] = {
    "debug" : DebugState,
}
################################################################################
