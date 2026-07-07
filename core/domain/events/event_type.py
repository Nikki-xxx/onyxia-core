from enum import Enum


class EventType(Enum):
    MODEL_CREATED = "model_created"
    BUYER_CREATED = "buyer_created"
    REPORT_CREATED = "report_created"
    CASE_CREATED = "case_created"
    PUBLICATION_CREATED = "publication_created"
    SANCTION_APPLIED = "sanction_applied"