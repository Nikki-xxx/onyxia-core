from datetime import datetime


class ModerationResult:

    def __init__(
        self,
        accepted: bool,
    ):
        self.accepted = accepted
        self.created_at = datetime.utcnow()