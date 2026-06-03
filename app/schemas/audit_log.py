from pydantic import BaseModel
from datetime import datetime


class AuditLogResponse(BaseModel):
    log_id: int
    user_id: int
    action: str
    entity_name: str
    entity_id: int
    created_at: datetime | None = None

    class Config:
        from_attributes = True