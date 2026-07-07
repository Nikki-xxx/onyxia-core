from datetime import datetime

from .sanction import Sanction


class ModerationAction:

    def __init__(
        self,
        sanction: Sanction,
        reason: str,
    ):
        self.sanction = sanction
        self.reason = reason
        self.created_at = datetime.utcnow()