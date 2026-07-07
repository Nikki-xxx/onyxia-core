from enum import Enum


class BlacklistReason(Enum):
    SCAM = "scam"
    FRAUD = "fraud"
    HARASSMENT = "harassment"
    SPAM = "spam"
    OTHER = "other"