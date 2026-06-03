from datetime import datetime

from app.repositories.audit_log_repository import AuditLogRepository
from app.models.audit_log import AuditLog


class AuditLogService:

    @staticmethod
    def get_all(db):
        return AuditLogRepository.get_all(db)

    @staticmethod
    def log_action(
        db,
        user_id: int,
        action: str,
        entity_name: str,
        entity_id: int
    ):

        log = AuditLog(
            user_id=user_id,
            action=action,
            entity_name=entity_name,
            entity_id=entity_id,
            created_at=datetime.utcnow()
        )

        return AuditLogRepository.create(db, log)