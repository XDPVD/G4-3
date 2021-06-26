from learnabc.database import Base
from typing import List, Optional
from pydantic import BaseModel
from ..user.models import User

class Course(BaseModel):
    id: int
    name: str

    class Config():
        orm_mode = True
        
        
class RequestCourse(BaseModel):
    name: str

    class Config():
        orm_mode = True
        
        
class ShowCourse(BaseModel):
    id: int
    name: str
    creator: User
    users_enrolled: List[User] = []

    class Config():
        orm_mode = True