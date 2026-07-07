from .federation_status import FederationStatus


class Federation:

    def __init__(self):
        self.communities = []
        self.events = []
        self.status = FederationStatus.PENDING

    def add_community(self, community):
        self.communities.append(community)

    def add_event(self, event):
        self.events.append(event)

    def activate(self):
        self.status = FederationStatus.ACTIVE