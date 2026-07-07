from enum import Enum


class ModelStatus(Enum):
    PENDING = "pending"
    VERIFIED = "verified"
    ACTIVE = "active"
    SUSPENDED = "suspended"
    BANNED = "banned"