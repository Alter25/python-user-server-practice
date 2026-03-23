from fastapi import APIRouter


router = APIRouter(prefix="/productos")

@router
async def router():
  return {"productos":"sobres"}