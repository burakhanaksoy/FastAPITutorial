from pydantic import BaseModel
from typing import Optional

class CreateBlog(BaseModel):
    title:str
    user:str
    likes: int
    published: bool
