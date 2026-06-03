from sqlalchemy.orm import Session

from app.models.assignment import Assignment


class AssignmentRepository:

    @staticmethod
    def get_all(
        db: Session
    ):
        return db.query(Assignment).all()

    @staticmethod
    def get_by_id(
        db: Session,
        assignment_id: int
    ):
        return (
            db.query(Assignment)
            .filter(
                Assignment.assignment_id
                == assignment_id
            )
            .first()
        )

    @staticmethod
    def get_by_course(
        db: Session,
        course_id: int
    ):
        return (
            db.query(Assignment)
            .filter(
                Assignment.course_id
                == course_id
            )
            .all()
        )