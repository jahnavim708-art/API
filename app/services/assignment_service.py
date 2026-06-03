from app.repositories.assignment_repository import AssignmentRepository
from app.models.assignment import Assignment


class AssignmentService:

    @staticmethod
    def get_all(db):
        return AssignmentRepository.get_all(db)

    @staticmethod
    def get_by_id(db, assignment_id: int):
        return AssignmentRepository.get_by_id(db, assignment_id)

    @staticmethod
    def create_assignment(db, data):

        assignment = Assignment(
            course_id=data.course_id,
            title=data.title,
            description=data.description,
            due_date=data.due_date
        )

        return AssignmentRepository.create(db, assignment)