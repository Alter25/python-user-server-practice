from pydantic import BaseModel
from typing import Optional


class ProductOther(BaseModel):
  imgUrl:str

class CreateProduct(BaseModel):
  name:str
  precio:int
  cantidad:int
  descripcion:str
  other:Optional[ProductOther]=None
  
class ProductResponse(BaseModel):
  id:str
  name:str
  precio:int
  cantidad:int
  descripcion:str
  
