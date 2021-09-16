from typing import List

from pydantic.main import BaseModel

from app.Models.Requests.inscription import Inscription


class Inscriptions(BaseModel):
    inscriptions: List[Inscription]
