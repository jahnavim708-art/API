from sqlalchemy.orm import Session

from app.models.lesson import Lesson


class LessonRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(Lesson).all()

    @staticmethod
    def get_by_id(
        db: Session,
        lesson_id: int
    ):
        return (
            db.query(Lesson)
            .filter(Lesson.lesson_id == lesson_id)
            .first()
        )

    @staticmethod
    def get_by_module(
        db: Session,
        module_id: int
    ):
        return (
            db.query(Lesson)
            .filter(Lesson.module_id == module_id)
            .all()
        )