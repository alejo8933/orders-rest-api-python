from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
import math

from app.database import get_db
from app.schemas.customer import CustomerCreate, CustomerUpdate, CustomerResponse
from app.services.customer_service import customer_service
from app.utils.pagination import PaginatedResponse

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("", response_model=PaginatedResponse[CustomerResponse])
def get_customers(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = None,
    country: Optional[str] = None,
    city: Optional[str] = None,
    db: Session = Depends(get_db)
):
    items, total = customer_service.get_all(db, page, limit, search, country, city)
    pages = math.ceil(total / limit) if total > 0 else 0
    return PaginatedResponse(items=items, total=total, page=page, limit=limit, pages=pages)

@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    return customer_service.get_by_id(db, customer_id)

@router.post("", response_model=CustomerResponse, status_code=201)
def create_customer(data: CustomerCreate, db: Session = Depends(get_db)):
    return customer_service.create(db, data)

@router.patch("/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int, data: CustomerUpdate, db: Session = Depends(get_db)):
    return customer_service.update(db, customer_id, data)
