from datetime import datetime


class Timestamp:

    @staticmethod
    def now():
        return datetime.utcnow()