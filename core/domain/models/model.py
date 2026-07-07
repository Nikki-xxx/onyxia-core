from __future__ import annotations

from core.domain.users.user import User


class Model(User):
    """
    Modelo verificada del ecosistema.
    """

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