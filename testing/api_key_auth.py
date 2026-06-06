from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import secrets
from testing.database import SessionLocal
from testing.models import User
from testing.schema import RegisterRequest

app = FastAPI()

api_key_header = APIKeyHeader(name="X-API-Key")

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.username == data.username).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    api_key = secrets.token_hex(16)

    user = User(
        username=data.username,
        email=data.email,
        password_hash=pwd_context.hash(data.password),
        api_key=api_key
    )

    db.add(user)
    db.commit()

    return {
        "message": "User registered successfully",
        "api_key": api_key
    }

@app.get("/login")
def login(
    api_key: str = Depends(api_key_header),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.api_key == api_key).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {"message": f"Welcome {user.username}"}