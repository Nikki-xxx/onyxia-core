from datetime import datetime


class FederationEvent:

    def __init__(self, description: str):
        self.description = description
        self.created_at = datetime.utcnow()