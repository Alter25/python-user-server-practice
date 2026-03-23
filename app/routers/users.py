from fastapi import APIRouter
from app.models.user import UserCreate, UserResponse
from app.utils import hash_password

router = APIRouter(prefix="/users",tags=["users"])


fake_db=[]

@router.post("/",response_model=UserResponse)
async def create_user(user:UserCreate):
  new_user={
    "id":len(fake_db)+1,
    "username":user.username,
    "email":user.email,
    "password":hash_password(user.password)
  }
  fake_db.append(new_user)
  return new_user


@router.get("/",response_model=list[UserResponse])
def get_users():
  return fake_db