from datetime import datetime


class ReportEvidence:

    def __init__(
        self,
        description: str,
        attachments: list[str] | None = None,
    ):
        self.description = description
        self.attachments = attachments or []
        self.created_at = datetime.utcnow()