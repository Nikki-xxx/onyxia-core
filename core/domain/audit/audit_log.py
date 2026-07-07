class AuditLog:

    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def total(self):
        return len(self.entries)