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

__all__ = ("DMLogHandler",)

################################################################################
class DMLogHandler(Handler):

    __slots__ = (
        "_state",
        "_logger",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, state: DMGame):

        super().__init__()

        self._state: DMGame = state
        self._logger: Logger = None  # type: ignore

        self._get_logger()
        self._format()

################################################################################
    def _get_logger(self) -> None:

        raise NotImplementedError

################################################################################
    def _format(self) -> None:

        raise NotImplementedError

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def game(self) -> DMGame:

        return self._state

################################################################################
    @property
    def logger(self) -> Logger:

        return self._logger

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
