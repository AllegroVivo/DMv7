from __future__ import annotations

import logging

from collections import deque
from logging    import Formatter, Handler, Logger, LogRecord
from pygame     import Rect, Surface
from pygame.font import Font
from typing import TYPE_CHECKING, Deque, List, Optional, Tuple

from Core.LogHandler import DMLogHandler
from utils import *

if TYPE_CHECKING:
    from Core import DMGame, DMObject
################################################################################

__all__ = ("EngineLogHandler",)

################################################################################
class EngineLogHandler(DMLogHandler):

    def _get_logger(self) -> None:

        self._logger = logging.getLogger("game.Engine")

################################################################################
    def _format(self) -> None:

        self.setFormatter(
            Formatter(
                "[%(asctime)s] %(name)s% -- (levelname)s |\n"
                "=== %(pathname)s: ln.%(lineno)d ===\n"
                "%(message)s"
            )
        )

################################################################################
##### PROPERTIES ###############################################################
################################################################################


################################################################################
##### HANDLING #################################################################
################################################################################
    def emit(self, record: LogRecord) -> None:

        self._log_lines.append(self.format(record))
        self.surface.fill(LOGGER_BG)

        for i, line in enumerate(self._log_lines):
            text_surf = self.font.render(line, True, self.message_color)
            text_rect = text_surf.get_rect(topleft=(0, i * 24))
            self.surface.blit(text_surf, text_rect)

################################################################################
##### LOG METHODS ##############################################################
################################################################################
    def debug(self, msg: str) -> None:

        self.logger.debug(msg)

################################################################################
    def info(self, msg: str) -> None:

        self.logger.info(msg)

################################################################################
    def warning(self, msg: str) -> None:

        self.logger.warning(msg)

################################################################################
    def error(self, msg: str) -> None:

        self.logger.error(msg)

################################################################################
    def critical(self, msg: str) -> None:

        self.logger.critical(msg)

################################################################################
