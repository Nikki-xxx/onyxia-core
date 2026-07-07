from enum import Enum


class IdentityStatus(Enum):
    PENDING = "pending"
    VERIFIED = "verified"
    SUSPENDED = "suspended"
    BANNED = "banned"