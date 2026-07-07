from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from core.domain.reports.report_reason import ReportReason
from core.domain.reports.report_status import ReportStatus
from core.domain.reports.report_evidence import ReportEvidence


class Report:

    def __init__(
        self,
        reporter_id: int,
        reported_id: int,
        reason: ReportReason,
        evidence: ReportEvidence,
    ):
        self.id = uuid4()
        self.reporter_id = reporter_id
        self.reported_id = reported_id
        self.reason = reason
        self.evidence = evidence
        self.status = ReportStatus.OPEN
        self.created_at = datetime.utcnow()

    def start_review(self):
        self.status = ReportStatus.UNDER_REVIEW

    def resolve(self):
        self.status = ReportStatus.RESOLVED

    def reject(self):
        self.status = ReportStatus.REJECTED