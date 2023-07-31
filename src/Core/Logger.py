from __future__ import annotations

import logging

from collections import deque
from logging    import Formatter, Handler, Logger, LogRecord
from pygame     import Rect, Surface
from pygame.font import Font
from typing import TYPE_CHECKING, Deque, List, Optional, Tuple

from utils import *

if TYPE_CHECKING:
    from Core import DMGame, DMObject
################################################################################

__all__ = ("DMLogManager",)

################################################################################
class DMLogManager(Handler):

    __slots__ = (
        "_state",
        "_surface",
        "_log_lines",
        "_obj_handle",
        "_engine_log",
        "_game_log",
        "_monster_log",
        "_hero_log",
        "_room_log",
        "_status_log",
        "_relic_log",
        "_skill_log",
        # etc...
    )

    MAX_LINES = 150

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, state: DMGame):

        super().__init__()

        self._state: DMGame = state

        self._surface: Surface = Surface(state._log_surf.get_size())
        self._log_lines: Deque = deque(maxlen=self.MAX_LINES)
        self._obj_handle: Optional[DMObject] = None

        self._engine_log: Logger = None  # type: ignore
        self._game_log: Logger = None  # type: ignore
        self._monster_log: Logger = None  # type: ignore
        self._hero_log: Logger = None  # type: ignore
        self._room_log: Logger = None  # type: ignore
        self._status_log: Logger = None  # type: ignore
        self._relic_log: Logger = None  # type: ignore
        self._skill_log: Logger = None  # type: ignore

        self._init_loggers()

################################################################################
    def _init_loggers(self) -> None:

        self._engine_log = logging.getLogger("Engine")
        self._engine_log.addHandler(self)

        self._game_log = logging.getLogger("Game")
        self._game_log.addHandler(self)

        self._monster_log = logging.getLogger("Monster")
        self._monster_log.addHandler(self)

        self._hero_log = logging.getLogger("Hero")
        self._hero_log.addHandler(self)

        self._room_log = logging.getLogger("Room")
        self._room_log.addHandler(self)

        self._status_log = logging.getLogger("Status")
        self._status_log.addHandler(self)

        self._relic_log = logging.getLogger("Relic")
        self._relic_log.addHandler(self)

        self._skill_log = logging.getLogger("Skill")
        self._skill_log.addHandler(self)

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def surface(self) -> Surface:

        return self._surface

################################################################################
    @property
    def rect(self) -> Rect:

        return self.surface.get_rect()

################################################################################
    @property
    def font(self) -> Font:

        return Font(None, 24)

################################################################################
    @property
    def lines(self) -> List[str]:

        return list(self._log_lines)

################################################################################
    @property
    def message_color(self) -> Tuple[int, int, int, int]:

        if self._obj_handle is None:
            return WHITE

        match self._obj_handle.obj_type:
            case DMObjectType.Monster:
                return LOG_MONSTER
            case DMObjectType.Hero:
                return LOG_HERO
            case DMObjectType.Room:
                return LOG_ROOM
            case DMObjectType.Status:
                return LOG_STATUS
            case DMObjectType.Relic:
                return LOG_RELIC
            case DMObjectType.Skill:
                return LOG_SKILL
            case _:
                raise ValueError(
                    f"Invalid object handle: {self._obj_handle.__class__.__name__} "
                    "present for game log message."
                )

################################################################################
##### LOG DISPLAY ##############################################################
################################################################################
    def draw(self, surface: Surface) -> None:

        self._surface.fill(LOGGER_BG)
        surface.blit(self.surface, self.rect)

################################################################################
    def emit(self, record: LogRecord) -> None:

        self._log_lines.append(self.format(record))
        self._surface.fill(LOGGER_BG)

        for i, line in enumerate(self.lines):
            text_surf = self.font.render(line, True, self.message_color)
            text_rect = text_surf.get_rect(topleft=(0, i * self.font.get_height()))
            self._surface.blit(text_surf, text_rect)

################################################################################
    def _format_engine(self) -> None:

        self.setFormatter(
            Formatter(
                fmt=(
                    "[%(asctime)s]: %(message)s\n"
                    "(%(levelname)s -- %(filename)s:%(lineno)d)\n"
                ),
                datefmt="%H:%M:%S"
            )
        )

################################################################################
    def _format_game(self) -> None:

        self.setFormatter(
            Formatter(
                fmt="[%(asctime)s] %(name)s: %(message)s",
                datefmt="%H:%M:%S"
            )
        )

################################################################################
##### LOGGING METHODS ##########################################################
################################################################################
    def log(
        self,
        msg: str,
        _obj: Optional[DMObject] = None,
        *,
        level: LogLevel = LogLevel.Info
    ) -> None:

        self._format_engine()

        if _obj is None:
            match level:
                case LogLevel.Info:
                    self._engine_log.info(msg)
                case LogLevel.Debug:
                    self._engine_log.debug(msg)
                case LogLevel.Warning:
                    self._engine_log.warning(msg)
                case LogLevel.Error:
                    self._engine_log.error(msg)
                case LogLevel.Critical:
                    self._engine_log.critical(msg)
                case _:
                    raise ValueError(f"Invalid log level: {level}")
            return

        self._obj_handle = _obj
        self._log_game(msg, level)

################################################################################
    def _log_game(self, msg: str, level: LogLevel) -> None:

        self._format_game()

        match self._obj_handle.obj_type:
            case DMObjectType.Monster:
                logger = self._monster_log
            case DMObjectType.Hero:
                logger = self._hero_log
            case DMObjectType.Room:
                logger = self._room_log
            case DMObjectType.Status:
                logger = self._status_log
            case DMObjectType.Relic:
                logger = self._relic_log
            case DMObjectType.Skill:
                logger = self._skill_log
            case _:
                raise ValueError(
                    f"Invalid object type: {self._obj_handle.obj_type}"
                )

        match level:
            case LogLevel.Info:
                logger.info(msg)
            case LogLevel.Debug:
                logger.debug(msg)
            case LogLevel.Warning:
                logger.warning(msg)
            case LogLevel.Error:
                logger.error(msg)
            case LogLevel.Critical:
                logger.critical(msg)
            case _:
                raise ValueError(f"Invalid log level: {level}")

        self._obj_handle = None

################################################################################
