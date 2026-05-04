from pydantic import BaseModel, ConfigDict
from typing import Optional

class CustomerBase(BaseModel):
    firstName: str
    lastName: str
    city: str
    country: str
    phone: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    phone: Optional[str] = None

class CustomerResponse(CustomerBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)
