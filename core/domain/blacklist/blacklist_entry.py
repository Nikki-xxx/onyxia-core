from __future__ import annotations

from datetime import datetime

from core.domain.blacklist.blacklist_reason import BlacklistReason


class BlacklistEntry:
    """
    Registro individual de la Lista Negra.
    """

    def __init__(
        self,
        telegram_id: int,
        reason: BlacklistReason,
        evidence: str,
    ):
        self.telegram_id = telegram_id
        self.reason = reason
        self.evidence = evidence
        self.created_at = datetime.utcnow()