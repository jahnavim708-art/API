
from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.config.database import get_db
from app.services.course_service import CourseService

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.post("/get_courses")
def get_courses(
    db: Session = Depends(get_db)
):
    return CourseService.get_all_courses(db)


@router.post("/{course_id}")
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    return CourseService.get_course_by_id(
        db,
        course_id
    )