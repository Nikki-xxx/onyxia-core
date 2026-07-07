from datetime import datetime


class BuyerApplication:

    def __init__(
        self,
        telegram_id: int,
        username: str,
    ):
        self.telegram_id = telegram_id
        self.username = username
        self.created_at = datetime.utcnow()