from __future__ import annotations

from core.domain.blacklist.blacklist_entry import BlacklistEntry


class Blacklist:
    """
    Lista Negra del ecosistema Onyxia.
    """

    def __init__(self):
        self.entries: list[BlacklistEntry] = []

    def add(self, entry: BlacklistEntry):
        self.entries.append(entry)

    def total(self) -> int:
        return len(self.entries)