from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password_hash: Mapped[str] = mapped_column(String)
    #role: Mapped[str] = mapped_column(String)