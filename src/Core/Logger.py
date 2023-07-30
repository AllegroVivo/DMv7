from __future__ import annotations

import logging
from collections import deque
from logging    import Formatter, Handler, Logger, LogRecord
from pygame     import Rect, Surface
from pygame.font import Font
from typing import TYPE_CHECKING, Deque, List, Optional, Tuple

from utils import *

if TYPE_CHECKING:
    from Core.Game import DMGame
    from Core.Object import DMObject
################################################################################

__all__ = ("DMLogManager",)

################################################################################
class DMLogManager(Handler):

    __slots__ = (
        "_state",
        "_surface",
        "_engine_log",
        "_game_log",
        "_log_lines",
        "_max_lines",
        "_obj_handle",
    )

    MAX_LINES = 150

################################################################################
    def __init__(self, state: DMGame):

        super().__init__()

        self._state: DMGame = state
        self._surface: Surface = Surface(state._log_surf.get_size())

        self._engine_log: Logger = logging.getLogger("game.engine")
        self._game_log: Logger = logging.getLogger("game.game")

        self._log_lines: Deque = deque(maxlen=self.MAX_LINES)
        self._obj_handle: Optional[DMObject] = None

        self._init_loggers()

################################################################################
    def _init_loggers(self) -> None:

        self._format_engine_log()

        self._engine_log.setLevel(logging.DEBUG)
        self._engine_log.addHandler(self)

        self._game_log.setLevel(logging.INFO)
        self._game_log.addHandler(self)

################################################################################
    def _format_engine_log(self) -> None:

        self.setFormatter(
            Formatter(
                "[%(asctime)s] %(name)s% -- (levelname)s |\n"
                "=== %(pathname)s: ln.%(lineno)d ===\n"
                "%(message)s"
            )
        )

################################################################################
    def _format_game_object(self) -> None:

        if self._obj_handle is None:
            raise ValueError("No object handle set for game log message.")

        self.setFormatter(
            Formatter(
                f"[%(asctime)s] {self._obj_handle.log_name}: %(message)s"
            )
        )

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
    def logs(self) -> List[str]:

        return list(self._log_lines)

################################################################################
    def emit(self, record: LogRecord) -> None:

        self._log_lines.append(self.format(record))

        self.surface.fill(LOGGER_BG)

        for i, line in enumerate(self._log_lines):
            text_surf = self.font.render(line, True, WHITE)
            text_rect = text_surf.get_rect(topleft=(0, i * 24))
            self.surface.blit(text_surf, text_rect)

################################################################################
    def draw(self, surface: Surface) -> None:

        surface.blit(self.surface, self.rect)

################################################################################
    def message_color(self) -> Tuple[int, int, int, int]:

        if self._obj_handle is None:
            return WHITE

        if self._obj_handle.is_monster():
            return LOG_MONSTER
        elif self._obj_handle.is_hero():
            return LOG_HERO
        else:
            raise ValueError(
                f"Invalid object handle: {self._obj_handle.__class__.__name__} "
                "present for game log message."
            )

################################################################################
    def debug(self, msg: str) -> None:

        self._engine_log.debug(msg)

################################################################################
    def info(self, msg: str) -> None:

        self._engine_log.info(msg)

################################################################################
    def warning(self, msg: str) -> None:

        self._engine_log.warning(msg)

################################################################################
    def error(self, msg: str) -> None:

        self._engine_log.error(msg)

################################################################################
    def critical(self, msg: str) -> None:

        self._engine_log.critical(msg)

################################################################################
    def game(self, _obj: DMObject, msg: str) -> None:

        self._obj_handle = _obj
        self._format_game_object()

        self._game_log.info(msg)

        self._obj_handle = None

################################################################################
