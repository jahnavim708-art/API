from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.config.database import get_db
from app.services.module_service import ModuleService

router = APIRouter(
    prefix="/modules",
    tags=["Modules"]
)


@router.get("/")
def get_modules(
    db: Session = Depends(get_db)
):
    return ModuleService.get_all_modules(db)


@router.get("/course/{course_id}")
def get_course_modules(
    course_id: int,
    db: Session = Depends(get_db)
):
    return ModuleService.get_by_course(
        db,
        course_id
    )