from enum import Enum


class VerificationLevel(Enum):
    NONE = 0
    BASIC = 1
    VERIFIED = 2
    PREMIUM = 3
    STAFF = 4