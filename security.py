
from pwdlib import PasswordHash
from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from jose import JWTError,jwt
from database import get_db
from model import User
import logging
#oruse
# from pwdlib import PasswordHash
# prefer bcrypt_sha256 to avoid bcrypt's 72-byte input limit; keep plain bcrypt for
# backward-compatibility so existing hashes still verify
#
#oruse
password_hash = PasswordHash.recommended()
def hash_password(password: str):
    return password_hash.hash(password)

def verify_password(password: str, hashed: str):
    return password_hash.verify(password, hashed)
#3jwt token

SECRET_KEY="SUPERSCRECTKEY"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=10
def create_access_token(data:dict):
    to_encode=data.copy()
    #dont modify original data
    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    #timedleta->duration or differecne in time
    #utc-> coordinated universal time 
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
##check with curent_user
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/login")
def get_current_user(
        token:str=Depends(oauth2_scheme),
        db:Session=Depends(get_db)
):
    credential_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unauthorized User",
         headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        user_id = payload.get("sub")
        logging.info(f"payload {payload}")
        logging.info(f"user id gained {user_id}")
        if user_id is None:
            raise credential_exception
        try:
            user_id = int(user_id)
        except (TypeError, ValueError):
            raise credential_exception
    except JWTError:
        raise credential_exception
    user=db.query(User).filter(User.id ==  user_id).first()
    logging.info(f"user id gained {user}")
    if user is None:
        raise credential_exception
    return user 

def get_current_admin(current_user:User=Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403,detail="Not Authorized")
    return current_user

