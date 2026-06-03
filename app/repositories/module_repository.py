from sqlalchemy.orm import Session

from app.models.module import Module


class ModuleRepository:

    @staticmethod
    def get_all(
        db: Session
    ):
        return db.query(Module).all()

    @staticmethod
    def get_by_id(
        db: Session,
        module_id: int
    ):
        return (
            db.query(Module)
            .filter(Module.module_id == module_id)
            .first()
        )

    @staticmethod
    def get_by_course(
        db: Session,
        course_id: int
    ):
        return (
            db.query(Module)
            .filter(Module.course_id == course_id)
            .all()
        )