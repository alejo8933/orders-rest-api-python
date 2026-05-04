from pydantic import BaseModel, ConfigDict
from typing import Optional
from .supplier import SupplierResponse

class ProductBase(BaseModel):
    productName: str
    supplierId: int
    unitPrice: float
    package: str
    isDiscontinued: bool = False

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    productName: Optional[str] = None
    supplierId: Optional[int] = None
    unitPrice: Optional[float] = None
    package: Optional[str] = None
    isDiscontinued: Optional[bool] = None

class ProductResponse(ProductBase):
    id: int
    supplier: Optional[SupplierResponse] = None
    
    model_config = ConfigDict(from_attributes=True)
