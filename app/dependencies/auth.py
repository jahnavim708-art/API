from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.config.database import get_db
from app.config.security import decode_access_token

from app.models.user import User
from app.models.role import Role
from app.models.user_role import UserRole


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """
    Validate JWT token and return current user.
    """

    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    user_id = payload.get("user_id")

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User ID missing from token"
        )

    user = (
        db.query(User)
        .filter(User.user_id == user_id)
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


def get_user_roles(
    user_id: int,
    db: Session
):
    """
    Get all role names assigned to user.
    """

    roles = (
        db.query(Role.role_name)
        .join(
            UserRole,
            Role.role_id == UserRole.role_id
        )
        .filter(
            UserRole.user_id == user_id
        )
        .all()
    )

    return [role.role_name for role in roles]


def admin_required(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Allow only Admin users.
    """

    roles = get_user_roles(
        current_user.user_id,
        db
    )

    if "Admin" not in roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    return current_user


def instructor_required(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Allow only Instructor users.
    """

    roles = get_user_roles(
        current_user.user_id,
        db
    )

    if "Instructor" not in roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Instructor access required"
        )

    return current_user


def student_required(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Allow only Student users.
    """

    roles = get_user_roles(
        current_user.user_id,
        db
    )

    if "Student" not in roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Student access required"
        )

    return current_user


def admin_or_instructor_required(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Allow Admin or Instructor users.
    """

    roles = get_user_roles(
        current_user.user_id,
        db
    )

    if (
        "Admin" not in roles and
        "Instructor" not in roles
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin or Instructor access required"
        )

    return current_user