from datetime import datetime
from uuid import uuid4

from .event_type import EventType


class DomainEvent:

    def __init__(
        self,
        event_type: EventType,
        payload: dict,
    ):
        self.id = uuid4()
        self.type = event_type
        self.payload = payload
        self.created_at = datetime.utcnow()