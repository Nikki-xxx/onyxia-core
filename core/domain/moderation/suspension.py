from datetime import datetime


class SuspensionAction:

    def __init__(self, days: int):
        self.days = days
        self.created_at = datetime.utcnow()