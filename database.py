from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
#session maker is a  class to talk to database
#declarative_base-> is the base class for orm model
from dotenv import load_dotenv
import os
load_dotenv()## used to get all values from .env 
DATABASE_URL=os.getenv("DATABASE_URL")# get all values as variable
engine=create_engine(DATABASE_URL)#connector
SessionLocal=sessionmaker(bind=engine,autoflush=False)
Base=declarative_base() ##it is a class to define ORM related database 
#depend function
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


