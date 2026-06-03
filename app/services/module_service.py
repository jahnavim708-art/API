from app.repositories.module_repository import ModuleRepository
from app.models.module import Module


class ModuleService:

    @staticmethod
    def get_all_modules(db):
        return ModuleRepository.get_all(db)

    @staticmethod
    def get_by_course(db, course_id: int):
        return ModuleRepository.get_by_course(db, course_id)

    @staticmethod
    def create_module(db, module_data):

        module = Module(
            course_id=module_data.course_id,
            title=module_data.title,
            display_order=module_data.display_order
        )

        return ModuleRepository.create(db, module)