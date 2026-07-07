from uuid import uuid4
from datetime import datetime

from .publication_status import PublicationStatus
from .publication_priority import PublicationPriority


class Publication:

    def __init__(
        self,
        owner_id,
        message: str,
    ):
        self.id = uuid4()

        self.owner_id = owner_id

        self.message = message

        self.status = PublicationStatus.PENDING

        self.priority = PublicationPriority.NORMAL

        self.created_at = datetime.utcnow()