from pydantic.main import BaseModel


class Message(BaseModel):
    message: str
