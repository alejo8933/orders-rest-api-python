from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import date
from .customer import CustomerResponse
from .order_item import OrderItemResponse, OrderItemCreate

class OrderBase(BaseModel):
    orderDate: date
    customerId: int

class OrderCreate(BaseModel):
    customerId: int
    items: List[OrderItemCreate]

class OrderUpdate(BaseModel):
    orderDate: Optional[date] = None
    customerId: Optional[int] = None

class OrderResponse(OrderBase):
    id: int
    orderNumber: str
    totalAmount: float
    customer: Optional[CustomerResponse] = None
    items: List[OrderItemResponse] = []
    
    model_config = ConfigDict(from_attributes=True)
