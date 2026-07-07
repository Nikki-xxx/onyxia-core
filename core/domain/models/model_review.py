from __future__ import annotations

from datetime import datetime


class ModelReview:
    """
    Representa la revisión administrativa de una solicitud.
    """

    def __init__(
        self,
        reviewer: str,
        approved: bool,
        reason: str | None = None,
    ):
        self.reviewer = reviewer
        self.approved = approved
        self.reason = reason
        self.reviewed_at = datetime.utcnow()