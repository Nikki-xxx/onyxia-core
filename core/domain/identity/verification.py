from .verification_level import VerificationLevel
from .verification_method import VerificationMethod


class Verification:

    def __init__(
        self,
        method: VerificationMethod,
        level: VerificationLevel,
    ):
        self.method = method
        self.level = level