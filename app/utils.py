from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str)->str:
  return pwd_context.hash(password)


def verify_password(plain:str, hashed:str)->bool:
  return pwd_context.verify(plain,hashed)

def create_access_token(data:dict)-> str:
  to_encode = data.copy()
  expire = datetime.now() + timedelta(minutes=settings.access_token_expire_minutes)
  to_encode.update("exp",expire)
  return jwt.enconde(to_encode, settings.secret_key, algorithm=settings.algorithm)


def verify_token(token:str)->dict:
  try:
    payload = jwt.decode(token, settings.secret_key,algorithms=[settings.algorithm])
    return payload
  except JWTError:
    return None