from sqlalchemy.orm import Session

from app.models.enrollment import Enrollment


class EnrollmentRepository:

    @staticmethod
    def get_all(
        db: Session
    ):
        return db.query(Enrollment).all()

    @staticmethod
    def get_by_user(
        db: Session,
        user_id: int
    ):
        return (
            db.query(Enrollment)
            .filter(
                Enrollment.user_id == user_id
            )
            .all()
        )

    @staticmethod
    def create(
        db: Session,
        enrollment: Enrollment
    ):
        db.add(enrollment)
        db.commit()
        db.refresh(enrollment)

        return enrollment