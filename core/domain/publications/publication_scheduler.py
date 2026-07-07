class PublicationScheduler:

    def __init__(self):
        self.queue = []

    def schedule(self, publication):
        self.queue.append(publication)