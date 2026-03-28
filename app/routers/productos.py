from fastapi import APIRouter, HTTPException, status
from app.models.producto import ProductResponse, CreateProduct
from app.database import products_collection


router = APIRouter(prefix="/productos", tags=["productos"])


@router.post("/",response_model=ProductResponse)
async def create_product(producto:CreateProduct):
  existing = await products_collection.find_one({"name":producto.name})
  if existing:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, detail="El producto ya existe"
    )
  
  new_product = {
    "name":producto.name,
    "precio":producto.precio,
    "descripcion":producto.descripcion,
    "cantidad":producto.cantidad,
  }
  result = await products_collection.insert_one(new_product)
  return {"id":str(result.inserted_id),"name":producto.name,"precio":producto.precio,"cantidad":producto.cantidad, "description":producto.description}

@router.get("/",response_model=list[ProductResponse])
async def get_products():
  productos=[]
  async for producto in products_collection.find():
    productos.append({
      "id":str(producto["_id"]),
      "name":producto["name"],
      "precio":producto["precio"],
      "cantidad":producto["cantidad"],
      "descripcion":producto["descripcion"]
    })
  return productos