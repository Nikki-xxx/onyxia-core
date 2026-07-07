from __future__ import annotations

from core.domain.models.model_status import ModelStatus
from core.domain.users.user import User


class Model(User):

    def __init__(
        self,
        telegram_id: int,
        username: str | None = None,
        first_name: str | None = None,
    ):
        super().__init__(
            telegram_id,
            username,
            first_name,
        )

        self.status = ModelStatus.PENDING