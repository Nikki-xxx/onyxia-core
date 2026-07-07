from .identity_status import IdentityStatus


class Identity:

    def __init__(self):
        self.status = IdentityStatus.PENDING
        self.roles = []
        self.permissions = []
        self.sessions = []

    def add_role(self, role):
        self.roles.append(role)

    def add_permission(self, permission):
        self.permissions.append(permission)

    def add_session(self, session):
        self.sessions.append(session)