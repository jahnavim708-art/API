from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from app.config.database import Base


class UserRole(Base):

    __tablename__ = "user_roles"

    user_role_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.user_id")
    )

    role_id = Column(
        Integer,
        ForeignKey("roles.role_id")
    )