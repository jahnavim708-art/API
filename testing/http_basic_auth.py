from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from testing.database import SessionLocal
from testing.models import User
app = FastAPI()
security = HTTPBasic()

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)
#print("ACTIVE SCHEMES:", pwd_context.schemes())


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/register")
def register(
    username: str,
    email: str,
    password: str,
    db: Session = Depends(get_db)
):
    existing_user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    hashed_password = pwd_context.hash(password)

    user = User(
        username=username,
        email=email,
        password_hash=hashed_password
    )

    db.add(user)
    db.commit()

    return {"message": "User registered successfully"}


@app.get("/")
def home(
    credentials: HTTPBasicCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.username == credentials.username)
        .first()
    )

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    

    if not pwd_context.verify(
        credentials.password,
        user.password_hash
    ):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": f"Welcome {user.username}"}