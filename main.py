from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import Base,engine,get_db
from schemas import Todo as TodoSchema,TodoCreate
from model import Todo
from login import router as auth_router
from todo import router as todo_router
import logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s ",
   )

#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)##Create all database tables defined by my ORM models, if they don’t already exist.
logging.info("Tables created successfully")
#Base-> parent class for SqlAlchemy models
#metadata-> informationabout all table
#create_all->create table
#engine-> connection
app=FastAPI()
app.include_router(auth_router)
app.include_router(todo_router)

