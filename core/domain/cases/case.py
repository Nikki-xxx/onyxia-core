from uuid import uuid4

from .case_priority import CasePriority
from .case_status import CaseStatus


class Case:

    def __init__(
        self,
        title: str,
        priority: CasePriority = CasePriority.NORMAL,
    ):
        self.id = uuid4()

        self.title = title

        self.priority = priority

        self.status = CaseStatus.OPEN

        self.events = []

        self.notes = []

        self.resolution = None

    def add_event(self, event):
        self.events.append(event)

    def add_note(self, note):
        self.notes.append(note)

    def resolve(self, resolution):
        self.resolution = resolution
        self.status = CaseStatus.RESOLVED

    def close(self):
        self.status = CaseStatus.CLOSED