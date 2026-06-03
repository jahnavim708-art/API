from sqlalchemy.orm import Session

from app.models.course import Course


class CourseRepository:

    @staticmethod
    def get_all(db: Session):
        return (
            db.query(Course)
            .order_by(Course.course_id.desc())
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        course_id: int
    ):
        return (
            db.query(Course)
            .filter(Course.course_id == course_id)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        course: Course
    ):
        db.add(course)
        db.commit()
        db.refresh(course)

        return course

    @staticmethod
    def update(
        db: Session,
        course: Course
    ):
        db.commit()
        db.refresh(course)

        return course

    @staticmethod
    def delete(
        db: Session,
        course: Course
    ):
        db.delete(course)
        db.commit()