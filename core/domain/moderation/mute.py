from datetime import datetime


class MuteAction:

    def __init__(self, hours: int):
        self.hours = hours
        self.created_at = datetime.utcnow()