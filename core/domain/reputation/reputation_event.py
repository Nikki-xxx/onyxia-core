from datetime import datetime


class ReputationEvent:

    def __init__(
        self,
        description: str,
    ):
        self.description = description
        self.created_at = datetime.utcnow()