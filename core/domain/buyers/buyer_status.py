from enum import Enum


class BuyerStatus(Enum):
    ACTIVE = "active"
    WARNED = "warned"
    SUSPENDED = "suspended"
    BANNED = "banned"