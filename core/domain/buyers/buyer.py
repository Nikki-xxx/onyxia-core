from __future__ import annotations

from core.domain.users.user import User


class Buyer(User):
    """
    Representa un comprador dentro del ecosistema.
    """

    def __init__(self):
        super().__init__()