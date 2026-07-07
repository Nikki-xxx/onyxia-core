class VerificationResult:

    def __init__(
        self,
        approved: bool,
        reason: str | None = None,
    ):
        self.approved = approved
        self.reason = reason