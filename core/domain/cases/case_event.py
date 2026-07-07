from datetime import datetime


class CaseEvent:

    def __init__(self, event: str):
        self.event = event
        self.created_at = datetime.utcnow()