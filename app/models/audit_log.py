from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from app.config.database import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    log_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.user_id")
    )

    action = Column(
        String(200)
    )

    entity_name = Column(
        String(100)
    )

    entity_id = Column(
        Integer
    )

    created_at = Column(
        DateTime
    )