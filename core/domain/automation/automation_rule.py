class AutomationRule:

    def __init__(
        self,
        name: str,
        enabled: bool = True,
    ):
        self.name = name
        self.enabled = enabled