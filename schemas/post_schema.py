#post schema
from pydantic import BaseModel

class PostCreate(BaseModel):
    userId: int
    title: str
    content: str
