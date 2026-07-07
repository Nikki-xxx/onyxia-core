from enum import Enum


class FederationStatus(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    SUSPENDED = "suspended"