from __future__ import annotations

from core.domain.common.base_entity import BaseEntity


class Community(BaseEntity):
    """
    Comunidad administrada por Onyxia.
    """

    def __init__(
        self,
        name: str,
        telegram_chat_id: int,
    ):
        super().__init__()

        self.name = name
        self.telegram_chat_id = telegram_chat_id