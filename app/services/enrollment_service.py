from datetime import datetime

from app.repositories.enrollment_repository import EnrollmentRepository
from app.models.enrollment import Enrollment


class EnrollmentService:

    @staticmethod
    def get_all(db):
        return EnrollmentRepository.get_all(db)

    @staticmethod
    def get_by_user(db, user_id: int):
        return EnrollmentRepository.get_by_user(db, user_id)

    @staticmethod
    def enroll_user(db, data):

        enrollment = Enrollment(
            user_id=data.user_id,
            course_id=data.course_id,
            enrollment_date=datetime.utcnow(),
            status="Active"
        )

        return EnrollmentRepository.create(db, enrollment)