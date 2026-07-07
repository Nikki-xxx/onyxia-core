from __future__ import annotations

from core.domain.common.base_entity import BaseEntity


class Community(BaseEntity):
    """
    Representa una comunidad administrada por Onyxia.
    """

    def __init__(
        self,
        name: str,
        telegram_chat_id: int,
    ):
        super().__init__()

        self.name = name
        self.telegram_chat_id = telegram_chat_id

        self.models = []
        self.buyers = []

    def add_model(self, model):
        self.models.append(model)

    def add_buyer(self, buyer):
        self.buyers.append(buyer)