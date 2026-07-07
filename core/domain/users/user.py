from __future__ import annotations

from core.domain.common.base_entity import BaseEntity


class User(BaseEntity):
    """
    Entidad base para cualquier usuario del ecosistema Onyxia.
    """

    def __init__(self):
        super().__init__()