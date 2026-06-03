from pydantic import BaseModel
from datetime import datetime


class EnrollmentCreate(BaseModel):
    user_id: int
    course_id: int


class EnrollmentResponse(BaseModel):
    enrollment_id: int
    user_id: int
    course_id: int
    enrollment_date: datetime | None = None
    status: str | None = None

    class Config:
        from_attributes = True