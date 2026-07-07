class DisciplinaryRecord:

    def __init__(self):
        self.warnings = 0
        self.mutes = 0
        self.suspensions = 0
        self.bans = 0

    def add_warning(self):
        self.warnings += 1

    def add_mute(self):
        self.mutes += 1

    def add_suspension(self):
        self.suspensions += 1

    def add_ban(self):
        self.bans += 1