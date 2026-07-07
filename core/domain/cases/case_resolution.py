from datetime import datetime


class CaseResolution:

    def __init__(self, summary: str):
        self.summary = summary
        self.created_at = datetime.utcnow()