
from pydantic import BaseModel
from typing import Optional
class Transcript(BaseModel):
    text: str
    user: str
    timestamp: Optional[str]

class AudioFile(BaseModel):
    file: bytes


class User(BaseModel):
    username: str

    class Config:
        orm_mode = True