from enum import Enum


class ReputationLevel(Enum):
    UNKNOWN = "unknown"
    TRUSTED = "trusted"
    VERIFIED = "verified"
    RISK = "risk"
    BANNED = "banned"