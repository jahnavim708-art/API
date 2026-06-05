from app.repositories.user_repository import UserRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.assignment_repository import AssignmentRepository


class DashboardService:

    @staticmethod
    def get_stats(db):

        return {
            "total_users": len(UserRepository.get_all(db)),
            "total_courses": len(CourseRepository.get_all(db)),
            "total_enrollments": len(EnrollmentRepository.get_all(db)),
            "total_assignments": len(AssignmentRepository.get_all(db))
        }