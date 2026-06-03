from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Text

from app.config.database import Base


class Course(Base):

    __tablename__ = "courses"

    course_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(200),
        nullable=False
    )

    description = Column(
        Text
    )

    instructor_id = Column(
        Integer,
        ForeignKey("users.user_id")
    )

    thumbnail_url = Column(
        String(500)
    )

    is_published = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime
    )