from app.repositories.lesson_repository import LessonRepository
from app.models.lesson import Lesson


class LessonService:

    @staticmethod
    def get_all_lessons(db):
        return LessonRepository.get_all(db)

    @staticmethod
    def get_by_module(db, module_id: int):
        return LessonRepository.get_by_module(db, module_id)

    @staticmethod
    def create_lesson(db, lesson_data):

        lesson = Lesson(
            module_id=lesson_data.module_id,
            title=lesson_data.title,
            content=lesson_data.content,
            video_url=lesson_data.video_url,
            duration_minutes=lesson_data.duration_minutes,
            display_order=lesson_data.display_order
        )

        return LessonRepository.create(db, lesson)