from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

# Routers
from app.routers import (
    auth_router,
    user_router,
    course_router,
    module_router,
    lesson_router,
    enrollment_router,
    assignment_router,
    audit_log_router,
    dashboard_router
)

# Middleware
from app.middleware.request_logger import RequestLoggerMiddleware
from app.middleware.auth import AuthMiddleware

# Exceptions
from app.exceptions.custom_exceptions import LMSException
from app.exceptions.handlers import lms_exception_handler


# =========================
# APP INIT
# =========================

app = FastAPI(
    title="LMS System",
    description="Learning Management System using FastAPI + MSSQL",
    version="1.0.0"
)

# =========================
# MIDDLEWARE (ORDER FIXED)
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(RequestLoggerMiddleware)
app.add_middleware(AuthMiddleware)

# =========================
# STATIC FILES
# =========================

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# =========================
# TEMPLATES
# =========================

templates = Jinja2Templates(
    directory="app/templates"
)

# =========================
# EXCEPTION HANDLER
# =========================

app.add_exception_handler(
    LMSException,
    lms_exception_handler
)

# =========================
# ROUTERS
# =========================

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(course_router)
app.include_router(module_router)
app.include_router(lesson_router)
app.include_router(enrollment_router)
app.include_router(assignment_router)
app.include_router(audit_log_router)
app.include_router(dashboard_router)

# =========================
# ROOT
# =========================

@app.get("/")
def home():
    return {"message": "LMS API is running"}

# =========================
# HEALTH CHECK
# =========================

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "LMS Backend"
    }