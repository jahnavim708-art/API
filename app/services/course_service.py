from app.repositories.course_repository import CourseRepository
from app.models.course import Course


class CourseService:

    @staticmethod
    def get_all_courses(db):
        return CourseRepository.get_all(db)

    @staticmethod
    def get_course_by_id(db, course_id: int):
        return CourseRepository.get_by_id(db, course_id)

    @staticmethod
    def create_course(db, course_data):

        course = Course(
            title=course_data.title,
            description=course_data.description,
            instructor_id=course_data.instructor_id,
            thumbnail_url=course_data.thumbnail_url,
            is_published=course_data.is_published
        )

        return CourseRepository.create(db, course)