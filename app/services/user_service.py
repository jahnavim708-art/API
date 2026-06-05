from app.repositories.user_repository import UserRepository
from app.config.security import hash_password
from app.models.user import User

from app.exceptions.custom_exceptions import UserAlreadyExistsException


class UserService:

    @staticmethod
    def get_all_users(db):
        return UserRepository.get_all(db)

    @staticmethod
    def get_user_by_id(db, user_id: int):
        return UserRepository.get_by_id(db, user_id)

    @staticmethod
    def create_user(db, user_data):

        existing = UserRepository.get_by_email(
            db,
            user_data.email
        )

        if existing:
            raise UserAlreadyExistsException()


        user = User(
            username=user_data.username,
            email=user_data.email,
            password_hash=hash_password(user_data.password),
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            phone=user_data.phone,
            is_active=True
        )

        return UserRepository.create(db, user)