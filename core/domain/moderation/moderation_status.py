from enum import Enum


class ModerationStatus(Enum):
    PENDING = "pending"
    REVIEWING = "reviewing"
    FINISHED = "finished"