from pydantic import BaseModel

class StudentsSchema(BaseModel):
    id: int = None
    name: str = None
    grade: int = None