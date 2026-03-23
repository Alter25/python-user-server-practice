from fastapi import APIRouter, HTTPException, status
from app.models.user import UserLogin, Token
from app.utils import verify_password, create_access_token
from app.routers.users import fake_db


router = APIRouter(prefix="/auth",tags=["auth"])


@router.post("/login",response_model=Token)
def login(credential: UserLogin):
  user=next((u for u in fake_db if u["username"] == credential.username),None)
  
  if not user or not verify_password(credential.password, user["password"]):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Credenciales incorrectas"
    )
  
  token = create_access_token(data={"sub":user["username"]})
  return {"access_token":token, "token_type": "bearer"}