from datetime import datetime


class BuyerResult:

    def __init__(
        self,
        approved: bool,
        reason: str | None = None,
    ):
        self.approved = approved
        self.reason = reason
        self.created_at = datetime.utcnow()