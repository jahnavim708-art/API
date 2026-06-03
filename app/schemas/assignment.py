from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AssignmentCreate(BaseModel):
    course_id: int
    title: str
    description: Optional[str] = None
    due_date: datetime


class AssignmentUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None


class AssignmentResponse(BaseModel):
    assignment_id: int
    course_id: int
    title: str
    description: Optional[str] = None
    due_date: datetime

    class Config:
        from_attributes = True