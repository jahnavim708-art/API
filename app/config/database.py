from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from connection import get_db_connection

Base = declarative_base()

engine = get_db_connection()

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()