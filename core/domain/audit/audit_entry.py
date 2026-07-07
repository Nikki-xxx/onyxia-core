from datetime import datetime


class AuditEntry:

    def __init__(
        self,
        actor: str,
        action,
        target: str,
    ):
        self.actor = actor
        self.action = action
        self.target = target
        self.created_at = datetime.utcnow()