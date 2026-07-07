from datetime import datetime


class ModelReview:

    def __init__(
        self,
        approved: bool,
        reviewer: str,
        reason: str = "",
    ):
        self.approved = approved
        self.reviewer = reviewer
        self.reason = reason
        self.reviewed_at = datetime.utcnow()