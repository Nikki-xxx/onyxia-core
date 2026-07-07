class PublicationRules:

    def __init__(
        self,
        max_daily_posts=3,
        minimum_interval=60,
    ):
        self.max_daily_posts = max_daily_posts
        self.minimum_interval = minimum_interval