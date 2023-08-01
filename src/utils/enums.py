from enum import Enum
####################################################################################################

__all__ = (
    "DMObjectType",
    "SpawnType",
    "LogLevel",
    "StatComponentType",
    "GraphicsState",
)

####################################################################################################
class DMObjectType(Enum):

    Object = 0
    Monster = 1
    Hero = 2
    Room = 3
    Skill = 4
    Status = 5
    Relic = 6
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
class LogLevel(Enum):

    Debug = 0
    Info = 1
    Warning = 2
    Error = 3
    Critical = 4

################################################################################
class StatComponentType(Enum):

    Life = 0
    Attack = 1
    Defense = 2
    Dex = 3
    Combat = 4
    NumAttacks = 5
    Speed = 6

################################################################################
class GraphicsState(Enum):

    Idle = 1
    Zoom = 2
    Attack = 3
    Death = 4
    Static = 5

################################################################################
