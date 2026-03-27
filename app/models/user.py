from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
  username:str
  email:str
  password:str
  
class UserLogin(BaseModel):
  username:str
  password:str
  
class UserResponse(BaseModel):
  id:str
  username:str
  email:str
  
class Token(BaseModel):
  access_token:str
  token_type:str
  

