from __future__ import annotations

from core.domain.common.base_entity import BaseEntity


class Community(BaseEntity):
    """
    Representa una comunidad administrada por Onyxia.
    """

    def __init__(self):
        super().__init__()