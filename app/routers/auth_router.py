from fastapi import APIRouter
from fastapi import Depends
#from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.auth import LoginRequest, TokenResponse
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.config.database import get_db
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login", response_model=TokenResponse)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    result= AuthService.login(
        db,
        request.username,
        request.password
    )
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    return result
