from pydantic import BaseModel


class ModuleCreate(BaseModel):
    course_id: int
    title: str
    display_order: int


class ModuleResponse(BaseModel):
    module_id: int
    course_id: int
    title: str
    display_order: int

    class Config:
        from_attributes = True