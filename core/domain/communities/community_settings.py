class CommunitySettings:
    """
    Configuración de la comunidad.
    """

    def __init__(
        self,
        allow_new_models=True,
        allow_new_buyers=True,
        auto_accept_buyers=False,
    ):
        self.allow_new_models = allow_new_models
        self.allow_new_buyers = allow_new_buyers
        self.auto_accept_buyers = auto_accept_buyers