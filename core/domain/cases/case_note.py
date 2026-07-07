from datetime import datetime


class CaseNote:

    def __init__(self, author: str, text: str):
        self.author = author
        self.text = text
        self.created_at = datetime.utcnow()