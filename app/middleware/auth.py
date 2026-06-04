from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session


from jose import JWTError, jwt
from app.config.settings import SECRET_KEY, ALGORITHM


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        public_paths = {
            "/",
            "/auth/login",
            "/auth/register",
            "/docs",
            "/openapi.json",
            "/redoc",
            "/favicon.ico"
        }

        path = request.url.path

        print("REQUEST PATH =", path)

        if path in public_paths or path.startswith("/static"):
            return await call_next(request)

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return JSONResponse(
                status_code=401,
                content={"detail": "Missing Authorization header"}
            )

        try:
            scheme, token = auth_header.split()

            if scheme.lower() != "bearer":
                return JSONResponse(
                    status_code=401,
                    content={"detail": "Invalid auth scheme"}
                )
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

            user_id = payload.get("user_id")

            if not user_id:
                return JSONResponse(status_code=401, content={"detail": "Invalid token"})

# NOTE: middleware has no DB session → so we keep payload only safely
            request.state.user = payload

            
        except ValueError:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid Authorization header format"}
            )

        except JWTError:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid or expired token"}
            )

        return await call_next(request)