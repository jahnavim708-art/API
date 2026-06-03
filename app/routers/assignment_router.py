from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.services.assignment_service import (
    AssignmentService
)

router = APIRouter(
    prefix="/assignments",
    tags=["Assignments"]
)


@router.get("/")
def get_assignments(
    db: Session = Depends(get_db)
):
    return AssignmentService.get_all(
        db
    )


@router.get("/{assignment_id}")
def get_assignment(
    assignment_id: int,
    db: Session = Depends(get_db)
):
    return AssignmentService.get_by_id(
        db,
        assignment_id
    )