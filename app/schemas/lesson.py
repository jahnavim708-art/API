from pydantic import BaseModel
from typing import Optional


class LessonCreate(BaseModel):
    module_id: int
    title: str
    content: Optional[str] = None
    video_url: Optional[str] = None
    duration_minutes: int
    display_order: int


class LessonResponse(BaseModel):
    lesson_id: int
    module_id: int
    title: str
    content: Optional[str] = None
    video_url: Optional[str] = None
    duration_minutes: int
    display_order: int

    class Config:
        from_attributes = True