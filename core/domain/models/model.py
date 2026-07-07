from __future__ import annotations

from core.domain.users.user import User


class Model(User):
    """
    Representa una modelo dentro del ecosistema.
    """

    def __init__(self):
        super().__init__()