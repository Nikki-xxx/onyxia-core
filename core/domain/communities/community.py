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

        self.models = []
        self.buyers = []

    def add_model(self, model):
        if model not in self.models:
            self.models.append(model)

    def add_buyer(self, buyer):
        if buyer not in self.buyers:
            self.buyers.append(buyer)

    def total_models(self):
        return len(self.models)

    def total_buyers(self):
        return len(self.buyers)

    def total_members(self):
        return len(self.models) + len(self.buyers)