from pygame.locals  import *
################################################################################
# System

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 768

GAME_AREA_WIDTH = SCREEN_WIDTH * 0.75
LOG_AREA_WIDTH = SCREEN_WIDTH * 0.25

FPS = 15

EPSILON = 3.0

################################################################################
# Colors

AQUAMARINE  = (127, 255, 212, 255)
BLACK       = (  0,   0,   0, 255)
BLUE        = (  0,   0, 255, 255)
BROWN       = (165,  42,  42, 255)
CREAM       = (255, 253, 208, 255)
CYAN        = (  0, 255, 255, 255)
GOLD        = (255, 215,   0, 255)
GREEN       = (  0, 255,   0, 255)
LAVENDER    = (230, 230, 250, 255)
LIME        = (  0, 128,   0, 255)
MAGENTA     = (255,   0, 255, 255)
MAROON      = (128,   0,   0, 255)
NAVY        = (  0,   0, 128, 255)
OLIVE       = (128, 128,   0, 255)
ORANGE      = (255, 165,   0, 255)
PINK        = (255, 105, 180, 255)
PURPLE      = (128,   0, 128, 255)
RED         = (200,   0,   0, 255)
SILVER      = (192, 192, 192, 255)
TEAL        = (  0, 128, 128, 255)
WHITE       = (255, 255, 255, 255)
YELLOW      = (255, 255,   0, 255)

INVISIBLE   = (  0,   0,   0,   0)
TINTED      = (  0,   0,   0, 128)

EXP_BG      = ( 60,  51,  42, 128)
ROOM_BG     = (254, 239, 198, 255)
CANCEL_BG   = ( 76,  45,   0, 255)
CONFIRM_BG  = ( 30,  71,   1, 255)
ZOOM_BORDER = ( 72,  60,  55, 255)

TEXT_ACCENT = (126,  83,  17, 255)

################################################################################
# Log Colors

LOGGER_BG = (255, 255, 102, 255)

LOG_MONSTER     = MAROON
LOG_HERO        = CYAN
LOG_RELIC       = PURPLE
LOG_SKILL       = ORANGE
LOG_STATUS      = LIME
LOG_ROOM        = LAVENDER
# etc...

################################################################################
# Game

DUNGEON_WIDTH = 3
DUNGEON_HEIGHT = 3
ROOM_SIZE = 150

HERO_SPEED = 75
SCROLL_SPEED = 10

################################################################################
# Visual

EDGE_PADDING = 75
GRID_PADDING = 25
SPRITE_PADDING = 0.15
BORDER_THICKNESS = 5

FATE_BOARD_WIDTH = 11
FATE_BOARD_HEIGHT = 20
FATE_ROWS = 5

FATE_CARD_WIDTH = 70
FATE_CARD_WIDTH_SCALED = 170
FATE_CARD_HEIGHT = 100
FATE_PADDING = 10
FATE_CARD_WIDTH_SMALL = 40
FATE_CARD_HEIGHT_SMALL = 50

FATE_FADE_TIME = 0.5

################################################################################
