from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.config.database import Base


class Module(Base):

    __tablename__ = "modules"

    module_id = Column(
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

    display_order = Column(
        Integer
    )