from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.services.enrollment_service import (
    EnrollmentService
)

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)


@router.get("/")
def get_enrollments(
    db: Session = Depends(get_db)
):
    return EnrollmentService.get_all(
        db
    )


@router.get("/user/{user_id}")
def get_user_enrollments(
    user_id: int,
    db: Session = Depends(get_db)
):
    return EnrollmentService.get_by_user(
        db,
        user_id
    )