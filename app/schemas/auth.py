from pydantic import BaseModel

# -------------------------
# REGISTER
# -------------------------
class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    role: str = "student"


# -------------------------
# LOGIN
# -------------------------
class LoginRequest(BaseModel):
    username: str
    password: str


# -------------------------
# TOKEN RESPONSE (IMPORTANT)
# -------------------------
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"