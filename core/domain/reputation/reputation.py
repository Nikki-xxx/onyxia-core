from .disciplinary_record import DisciplinaryRecord
from .reputation_level import ReputationLevel
from .trust_score import TrustScore


class Reputation:

    def __init__(self):
        self.level = ReputationLevel.UNKNOWN
        self.score = TrustScore()
        self.history = []
        self.record = DisciplinaryRecord()

    def add_event(self, event):
        self.history.append(event)