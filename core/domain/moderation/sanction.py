from enum import Enum


class Sanction(Enum):
    WARNING = "warning"
    MUTE = "mute"
    SUSPENSION = "suspension"
    BAN = "ban"