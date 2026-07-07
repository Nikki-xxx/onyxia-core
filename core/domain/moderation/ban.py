from datetime import datetime


class BanAction:

    def __init__(self, reason: str):
        self.reason = reason
        self.created_at = datetime.utcnow()