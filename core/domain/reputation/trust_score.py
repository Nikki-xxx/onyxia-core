class TrustScore:

    def __init__(self, score: int = 0):
        self.score = score

    def increase(self, points: int):
        self.score += points

    def decrease(self, points: int):
        self.score -= points