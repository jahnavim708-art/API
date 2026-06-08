from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from passlib.context import CryptContext

#from starsessions import SessionMiddleware, SessionAutoloadMiddleware
from starlette.middleware.sessions import SessionMiddleware
from testing.database import SessionLocal
from testing.models import User
from testing.schema import RegisterRequest

app = FastAPI()
app.add_middleware(
    SessionMiddleware,
    secret_key="my-secret-key"
)
# Session middleware
#app.add_middleware(SessionMiddleware, secret_key="my-secret-key")
#app.add_middleware(SessionMiddleware)

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)


# ---------------- DB ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- LOGIN ----------------
@app.post("/login")
def login(
    data: RegisterRequest,
    request: Request,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == data.username).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not pwd_context.verify(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Store user in session
    request.session["username"] = user.username

    return {"message": "Login successful"}


# ---------------- PROTECTED ROUTE ----------------
@app.get("/")
def home(request: Request):
    username = request.session.get("username")

    if not username:
        raise HTTPException(status_code=401, detail="Not authenticated")

    return {"message": f"Welcome {username}"}


# ---------------- LOGOUT ----------------
@app.post("/logout")
def logout(request: Request):
    request.session.clear()
    return {"message": "Logged out successfully"}