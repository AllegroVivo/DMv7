from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    pass
################################################################################

__all__ = (
    "class_to_file_name",
)

################################################################################
def class_to_file_name(obj: Any):

    return ''.join(
        ['_' + i.lower() if i.isupper() else i for i in obj.__class__.__name__]
    ).lstrip('_')

################################################################################
