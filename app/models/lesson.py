from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Text

from app.config.database import Base


class Lesson(Base):

    __tablename__ = "lessons"

    lesson_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    module_id = Column(
        Integer,
        ForeignKey("modules.module_id")
    )

    title = Column(
        String(200),
        nullable=False
    )

    content = Column(
        Text
    )

    video_url = Column(
        String(500)
    )

    duration_minutes = Column(
        Integer
    )

    display_order = Column(
        Integer
    )