from enum import Enum


class PublicationStatus(Enum):
    PENDING = "pending"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"
    EXPIRED = "expired"
    CANCELLED = "cancelled"