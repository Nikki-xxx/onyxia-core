from __future__ import annotations

from abc import ABC
from uuid import UUID, uuid4


class BaseEntity(ABC):
    """
    Clase base para todas las entidades del dominio.
    """

    def __init__(self, entity_id: UUID | None = None):
        self._id = entity_id or uuid4()

    @property
    def id(self) -> UUID:
        return self._id

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.id == other.id

    def __hash__(self):
        return hash(self.id)