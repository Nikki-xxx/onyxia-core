from datetime import datetime


class DomainClock:

    @staticmethod
    def now():
        return datetime.utcnow()