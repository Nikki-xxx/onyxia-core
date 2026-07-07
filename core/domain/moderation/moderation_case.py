from uuid import uuid4

from .moderation_status import ModerationStatus


class ModerationCase:

    def __init__(
        self,
        report_id,
    ):
        self.id = uuid4()

        self.report_id = report_id

        self.status = ModerationStatus.PENDING

        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def finish(self):
        self.status = ModerationStatus.FINISHED