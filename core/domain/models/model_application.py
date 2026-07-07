from __future__ import annotations

from datetime import datetime


class ModelApplication:

    def __init__(
        self,
        telegram_id: int,
        username: str,
        display_name: str,
        country: str,
    ):
        self.telegram_id = telegram_id
        self.username = username
        self.display_name = display_name
        self.country = country

        self.created_at = datetime.utcnow()

        self.reviewed = False
        self.accepted = False