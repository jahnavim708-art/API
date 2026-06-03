from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime

from app.config.database import Base


class User(Base):

    __tablename__ = "users"

    user_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(100),
        nullable=False,
        unique=True
    )

    email = Column(
        String(255),
        nullable=False,
        unique=True
    )

    password_hash = Column(
        String(500),
        nullable=False
    )

    first_name = Column(
        String(100)
    )

    last_name = Column(
        String(100)
    )

    phone = Column(
        String(20)
    )

    is_active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime
    )

    updated_at = Column(
        DateTime
    )