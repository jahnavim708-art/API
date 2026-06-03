from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog


class AuditLogRepository:

    @staticmethod
    def get_all(
        db: Session
    ):
        return (
            db.query(AuditLog)
            .order_by(
                AuditLog.log_id.desc()
            )
            .all()
        )

    @staticmethod
    def create(
        db: Session,
        audit_log: AuditLog
    ):
        db.add(audit_log)
        db.commit()
        db.refresh(audit_log)

        return audit_log