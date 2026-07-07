from .buyer_application import BuyerApplication
from .buyer_result import BuyerResult


class BuyerOnboarding:

    def submit(self, application: BuyerApplication):
        return application

    def approve(self):
        return BuyerResult(True)

    def reject(self, reason: str):
        return BuyerResult(False, reason)