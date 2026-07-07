from enum import Enum


class ReportReason(Enum):
    SCAM = "scam"
    HARASSMENT = "harassment"
    SPAM = "spam"
    IMPERSONATION = "impersonation"
    OTHER = "other"