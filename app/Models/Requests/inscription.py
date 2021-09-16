from pydantic.main import BaseModel


class Inscription(BaseModel):
    student_id: str
    subject_code: str