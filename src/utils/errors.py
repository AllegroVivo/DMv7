import traceback

from typing     import List, Optional
################################################################################

__all__ = (
    "DMException",
    "SpawnNotFound",
)

################################################################################
class DMException(Exception):

    def __init__(
        self,
        ctx: str,
        message: Optional[str],
        additional_info: Optional[str]
    ):

        super().__init__(message or "Please check the custom breakdown provided.")

        self._ctx: str = ctx
        self._addl_info: Optional[str] = additional_info

################################################################################
    @property
    def additional_info(self) -> str:

        return (
            "\n==================================================\n"
            f"{self._addl_info}"
        ) if self._addl_info is not None else ""

################################################################################
    @property
    def tb(self) -> str:

        return traceback.format_exc()

################################################################################
class SpawnNotFound(Exception):

    def __init__(
            self,
            invalid_value: str,
            spawn_type: str,
            alternates: Optional[List[str]] = None,
            additional_info: Optional[str] = None
    ):
        self._invalid_value: str = invalid_value
        self._spawn_type: str = spawn_type

        self._alternates: Optional[List[str]] = alternates
        self._addl_info: Optional[str] = additional_info

################################################################################
    def __repr__(self) -> str:

        return (
            "Traceback:\n"
            # f"{self.tb}\n"
            "==================================================\n"
            "<SpawnNotFound Raised!>\n"
            f"'{self._invalid_value}' is not a valid {self._spawn_type}'\n\n"

            f"Did you mean one of these: {self._alternates}\n"
            "==================================================\n"
            f"{self._addl_info}"
        )

################################################################################
