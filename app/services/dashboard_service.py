from app.repositories.user_repository import UserRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.assignment_repository import AssignmentRepository


class DashboardService:

    @staticmethod
    def get_stats(db):

        return {
            "total_users": db.query(UserRepository.get_all(db).__class__).count(),
            "total_courses": db.query(CourseRepository.get_all(db).__class__).count(),
            "total_enrollments": db.query(EnrollmentRepository.get_all(db).__class__).count(),
            "total_assignments": db.query(AssignmentRepository.get_all(db).__class__).count()
        }