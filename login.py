from fastapi import Depends,HTTPException,APIRouter,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from security import verify_password, hash_password, create_access_token
from database import get_db
from model import User as UserModel
from schemas import User,UserCreate
import logging
router=APIRouter()
@router.post("/register",response_model=User)
def register(user:UserCreate,db:Session=Depends(get_db)):
    logging.info("Checking if user already exists")
    db_user=db.query(UserModel).filter(UserModel.username == user.username).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="user already registered"
        )
    #hash password
    logging.warning(f"password_value:{user.password}")
    logging.warning(f"password_len:{len(user.password)}")
    hashed_password=hash_password(user.password)
    logging.warning(f"hased password_value:{hashed_password}")
   
    # show byte-length (bcrypt's 72-byte limit applies to bytes, not Python characters)
    logging.info("Creating new user object")
    new_user=UserModel(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role
    )
    logging.info("Saving user to database")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
@router.post("/login")
def login(
    form_data:OAuth2PasswordRequestForm=Depends(),
    db:Session=Depends(get_db)
):
    user=db.query(UserModel).filter(UserModel.username ==  form_data.username).first()
    if not user :
        logging.warning("User not found")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credential"
        )
    logging.info(f"User authenticated: {user.username}")
    if not verify_password(form_data.password , user.hashed_password):
        logging.warning("invalid password")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credential"
        )

    # automatically migrate legacy hashes (e.g. plain bcrypt) to the preferred scheme
    #if pwd_context.needs_update(user.hashed_password):
      

    access_token=create_access_token(
        data={"sub":str(user.id)}
    )
    logging.info(f"token cretaed: {access_token}")
    return{
        "access_token":access_token,
        "token_type":"bearer"
    }
