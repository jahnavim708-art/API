from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.config.security import decode_access_token


class AuthMiddleware(BaseHTTPMiddleware):
    """
    JWT Authentication Middleware
    """

    async def dispatch(
        self,
        request: Request,
        call_next
    ):
        # Public routes
        public_routes = [
            "/",
            "/docs",
            "/redoc",
            "/openapi.json",
            "/auth/login",
            "/auth/register"
        ]

        if request.url.path in public_routes:
            return await call_next(request)

        auth_header =