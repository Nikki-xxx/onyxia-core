from datetime import datetime


class Session:

    def __init__(self):
        self.created_at = datetime.utcnow()