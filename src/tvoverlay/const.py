"""Constants for the TvOverlay library."""

from enum import Enum
from typing import Final

DEFAULT_TITLE: Final = "Notification"
DEFAULT_APP_NAME: Final = "Home Assistant"
DEFAULT_SMALL_ICON: Final = "mdi:bell"
DEFAULT_APP_ICON: Final = "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"  # noqa: E501
COLOR_GREEN: Final = "#41E09A"
COLOR_WHITE: Final = "#FFFFFF"
COLOR_BLACK: Final = "#000000"
DEFAULT_SOURCE_NAME: Final = "Notify"
DEFAULT_DURATION: Final = "5"

UNITS = {
    "s": "seconds",
    "m": "minutes",
    "h": "hours",
    "d": "days",
    "w": "weeks",
}


class Positions(Enum):
    """Supported positions for the notification overlay."""

    BOTTOM_RIGHT = "bottom_right"
    BOTTOM_LEFT = "bottom_left"
    TOP_RIGHT = "top_right"
    TOP_LEFT = "top_left"


class Shapes(Enum):
    """Supported positions for the notification overlay."""

    CIRCLE = "circle"
    ROUNDED = "rounded"
    RECTANGULAR = "rectangular"
