from pydantic import BaseModel, ConfigDict
from typing import Optional

class SupplierBase(BaseModel):
    companyName: str
    contactName: str
    contactTitle: str
    city: str
    country: str
    phone: str
    fax: Optional[str] = None

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(BaseModel):
    companyName: Optional[str] = None
    contactName: Optional[str] = None
    contactTitle: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None

class SupplierResponse(SupplierBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)
