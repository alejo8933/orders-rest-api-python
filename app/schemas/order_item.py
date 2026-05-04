from pydantic import BaseModel, ConfigDict
from typing import Optional

class OrderItemBase(BaseModel):
    productId: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemUpdate(BaseModel):
    quantity: Optional[int] = None
    unitPrice: Optional[float] = None

class OrderItemResponse(OrderItemBase):
    id: int
    orderId: int
    unitPrice: float
    
    model_config = ConfigDict(from_attributes=True)
