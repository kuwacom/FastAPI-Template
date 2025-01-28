from pydantic import BaseModel
from typing import List

class Hello(BaseModel):
    name: str
    hellos: List[str]
