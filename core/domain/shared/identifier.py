from uuid import uuid4


class Identifier:

    @staticmethod
    def new():
        return uuid4()