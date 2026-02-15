from pydantic import BaseModel
from datetime import datetime
from enums import TodoStatus
class TodoBase(BaseModel):
    title:str
    status:TodoStatus=TodoStatus.pending
    completed:bool|None=None
    created_at:datetime
class TodoCreate(TodoBase):
      pass
class Todo(TodoBase):
     id:int
     class Config:
          from_attributes=True## to get orm todo base getting as python object to convert them as json format 
##object creation for user
class UserCreate(BaseModel):
     username:str
     email:str
     password:str
     role:str="user"

class User( BaseModel):
    id: int
    username:str
    email:str
    role:str
    class Config:
        from_attributes = True 