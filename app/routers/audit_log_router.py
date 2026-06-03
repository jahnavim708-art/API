from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.services.audit_log_service import (
    AuditLogService
)

router = APIRouter(
    prefix="/audit-logs",
    tags=["Audit Logs"]
)


@router.get("/")
def get_logs(
    db: Session = Depends(get_db)
):
    return AuditLogService.get_all(
        db
    )