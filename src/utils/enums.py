from enum import Enum
####################################################################################################

__all__ = (
    "DMObjectType",
    "SpawnType"
)

####################################################################################################
class DMObjectType(Enum):

    Object = 0
    Monster = 1
    Hero = 2
    Room = 3
    Skill = 4
    Status = 5
    # etc...

####################################################################################################
    @property
    def log_name(self) -> str:

        return self.name.upper()

####################################################################################################
class SpawnType(Enum):

    Monster = 1
    Hero = 2
    Room = 3
    Status = 4
    Relic = 5
    Fate = 6
    Skill = 7

################################################################################
