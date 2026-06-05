from app.repositories.user_repository import UserRepository
from app.config.security import (
    verify_password,
    create_access_token,
    hash_password
)
from app.models.user import User


class AuthService:

    @staticmethod
    def register(db, data):

        existing_user = UserRepository.get_by_username(
            db,
            data.username
        )

        if existing_user:
            raise Exception("Username already exists")

        existing_email = UserRepository.get_by_email(
            db,
            data.email
        )

        if existing_email:
            raise Exception("Email already exists")

        user = User(
            username=data.username,
            email=data.email,
            password_hash=hash_password(data.password),
            is_active=True
        )

        return UserRepository.create(db, user)

    @staticmethod
    def login(db, username: str, password: str):

        user = UserRepository.get_by_username(db, username)

        if not user:
            return None

        if not verify_password(
            password,
            user.password_hash
        ):
            return None

        token = create_access_token(
            {
                "user_id": user.user_id,
                "username": user.username
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }