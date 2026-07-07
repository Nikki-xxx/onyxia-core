from __future__ import annotations

from core.domain.common.base_entity import BaseEntity


class User(BaseEntity):
    """
    Usuario base del ecosistema Onyxia.
    """

    def __init__(
        self,
        telegram_id: int,
        username: str | None = None,
        first_name: str | None = None,
    ):
        super().__init__()

        self.telegram_id = telegram_id
        self.username = username
        self.first_name = first_name