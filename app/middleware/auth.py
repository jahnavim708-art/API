from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from jose import JWTError, jwt

from app.config.settings import SECRET_KEY, ALGORITHM


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        # Public routes (no token required)
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

        # Get Authorization header
        auth_header = request.headers.get("Authorization")

        # Header missing
        if not auth_header:
            return JSONResponse(
                status_code=401,
                content={"detail": "Missing Authorization header"}
            )

        # Expected format:
        # Authorization: Bearer <token>
        parts = auth_header.split()

        if len(parts) != 2:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid Authorization header format"}
            )

        scheme, token = parts

        if scheme.lower() != "bearer":
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid auth scheme"}
            )

        try:
            
            print("SECRET_KEY =", SECRET_KEY)
            print("ALGORITHM =", ALGORITHM)

            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=[ALGORITHM]
            )
            print("PAYLOAD =", payload)

            #if not SECRET_KEY or not ALGORITHM:
                #return JSONResponse(
                   # status_code=500,
                    #content={"detail": "Server auth config error"}
               # )
               


            user_id = payload.get("user_id")

            if not user_id:
                return JSONResponse(
                    status_code=401,
                    content={"detail": "Invalid token payload"}
                )

            # Save user info for endpoints
            request.state.user = payload

        except JWTError as e:
            print("JWT ERROR =", repr(e))
            return JSONResponse(
                status_code=401,
                content={str(e)}
            )

        return await call_next(request)