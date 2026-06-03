from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.config.database import get_db
from app.services.lesson_service import LessonService

router = APIRouter(
    prefix="/lessons",
    tags=["Lessons"]
)


@router.get("/")
def get_lessons(
    db: Session = Depends(get_db)
):
    return LessonService.get_all_lessons(
        db
    )


@router.get("/module/{module_id}")
def get_module_lessons(
    module_id: int,
    db: Session = Depends(get_db)
):
    return LessonService.get_by_module(
        db,
        module_id
    )