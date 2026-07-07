from __future__ import annotations

from core.domain.models.model_status import ModelStatus
from core.domain.users.user import User
from core.domain.common.exceptions import DomainException


class Model(User):

    def __init__(
        self,
        telegram_id: int,
        username: str | None = None,
        first_name: str |None = None,
    ):
        super().__init__(
            telegram_id,
            username,
            first_name,
        )

        self.status = ModelStatus.PENDING

    def verify(self):
        if self.status != ModelStatus.PENDING:
            raise DomainException(
                "Only pending models can be verified."
            )

        self.status = ModelStatus.VERIFIED

    def activate(self):
        if self.status != ModelStatus.VERIFIED:
            raise DomainException(
                "Only verified models can be activated."
            )

        self.status = ModelStatus.ACTIVE

    def suspend(self):
        if self.status == ModelStatus.BANNED:
            raise DomainException(
                "A banned model cannot be suspended."
            )

        self.status = ModelStatus.SUSPENDED

    def ban(self):
        self.status = ModelStatus.BANNED