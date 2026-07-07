from .model_application import ModelApplication
from .model_decision import ModelDecision
from .model_result import ModelResult


class ModelOnboarding:

    def submit(
        self,
        application: ModelApplication,
    ):
        return application

    def approve(self):
        return ModelResult(True)

    def reject(self, reason: str):
        return ModelResult(False, reason)