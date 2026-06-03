from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import home_router

app = FastAPI(
    title="LMS System"
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

app.include_router(home_router.router)