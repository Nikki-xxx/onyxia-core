from enum import Enum


class ModerationReason(Enum):
    SCAM = "scam"
    SPAM = "spam"
    HARASSMENT = "harassment"
    IMPERSONATION = "impersonation"
    OTHER = "other"