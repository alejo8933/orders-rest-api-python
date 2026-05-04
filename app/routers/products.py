from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
import math

from app.database import get_db
from app.schemas.product import ProductResponse
from app.services.product_service import product_service
from app.utils.pagination import PaginatedResponse

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("", response_model=PaginatedResponse[ProductResponse])
def get_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = None,
    supplierId: Optional[int] = None,
    discontinued: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    items, total = product_service.get_all(db, page, limit, search, supplierId, discontinued)
    pages = math.ceil(total / limit) if total > 0 else 0
    return PaginatedResponse(items=items, total=total, page=page, limit=limit, pages=pages)

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.get_by_id(db, product_id)
