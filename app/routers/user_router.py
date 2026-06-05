from fastapi import APIRouter,Request
from fastapi import Depends

from sqlalchemy.orm import Session

from app.config.database import get_db
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/me")
def me(request: Request):
    return request.state.user


@router.get("/")
def get_users(
    db: Session = Depends(get_db)
):
    return UserService.get_all_users(db)


@router.get("/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return UserService.get_user_by_id(
        db,
        user_id
    )