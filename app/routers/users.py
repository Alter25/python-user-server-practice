from fastapi import APIRouter, HTTPException, status
from app.models.user import UserCreate, UserResponse
from app.utils import hash_password
from app.database import user_collection

router = APIRouter(prefix="/users",tags=["users"])


@router.post("/",response_model=UserResponse)
async def create_user(user:UserCreate):
  existing = await user_collection.find_one({"username":user.username})
  if existing:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario ya existe"
    )
    
  new_user={
    "username":user.username,
    "email":user.email,
    "password":hash_password(user.password)
  }
  result = await user_collection.insert_one(new_user)
  return {"id":str(result.inserted_id),"username":user.username,"email":user.email}



@router.get("/",response_model=list[UserResponse])
async def get_users():
  users=[]
  async for user in user_collection.find():
    users.append({
      "id":str(user["_id"]),
      "username":user["username"],
      "email":user["email"]
    })
    return users