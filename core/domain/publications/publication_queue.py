class PublicationQueue:

    def __init__(self):
        self.items = []

    def enqueue(self, publication):
        self.items.append(publication)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)

    def total(self):
        return len(self.items)