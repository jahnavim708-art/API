from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy import DateTime

from app.config.database import Base


class Assignment(Base):

    __tablename__ = "assignments"

    assignment_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.course_id")
    )

    title = Column(
        String(200),
        nullable=False
    )

    description = Column(
        Text
    )

    due_date = Column(
        DateTime
    )