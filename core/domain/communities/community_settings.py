class CommunitySettings:
    """
    Configuración general de una comunidad.
    """

    def __init__(
        self,
        allow_new_models: bool = True,
        allow_new_buyers: bool = True,
    ):
        self.allow_new_models = allow_new_models
        self.allow_new_buyers = allow_new_buyers