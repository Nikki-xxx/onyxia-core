class PermissionGroup:

    def __init__(self, name: str):
        self.name = name
        self.permissions = []

    def add(self, permission):
        self.permissions.append(permission)