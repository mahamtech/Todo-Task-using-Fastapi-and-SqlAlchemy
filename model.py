from sqlalchemy import Column,INTEGER,String,Boolean,Enum,DateTime
from database import Base
from datetime import datetime
from enums import TodoStatus
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
class User(Base):
    __tablename__="users"
    id=Column(INTEGER,primary_key=True,index=True)
    username=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=True)
    hashed_password=Column(String,nullable=False)
    role=Column(String,default="user")

    todos=relationship("Todo",back_populates="user",cascade="all,delete")#relationship is object connection b/w two 
    ##back_populates refer object with
class Todo(Base):
    __tablename__="todo_project"
    id=Column(INTEGER,primary_key=True,index=True)
    title=Column(String,nullable=False)
    status=Column(Enum(TodoStatus),nullable=False,default=TodoStatus.pending)
    completed=Column(Boolean,default=False)
    created_at=Column(DateTime,default=datetime.utcnow)
    user_id=Column(INTEGER,ForeignKey("users.id"),nullable=False)
    user=relationship("User",back_populates="todos")