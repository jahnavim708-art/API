from app.repositories.user_repository import UserRepository
from app.config.security import hash_password, verify_password, create_access_token

from app.config.security import (
    verify_password,
    create_access_token
)


class AuthService:
    
    @staticmethod
    def login(db, username: str, password: str):

        user = UserRepository.get_by_username(db, username)

        if not user:
            return None

        # ✅ FIX: ENABLE PASSWORD CHECK
        if not verify_password(password, user.password_hash):
            return None

        token = create_access_token({
            "user_id": user.user_id,
            "username": user.username
        })

        return {
            "access_token": token,
            "token_type": "bearer"
        }










    