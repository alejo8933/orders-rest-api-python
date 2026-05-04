from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date
import math

from app.database import get_db
from app.schemas.order import OrderCreate, OrderUpdate, OrderResponse
from app.services.order_service import order_service
from app.utils.pagination import PaginatedResponse

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("", response_model=PaginatedResponse[OrderResponse])
def get_orders(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    customerId: Optional[int] = None,
    dateFrom: Optional[date] = None,
    dateTo: Optional[date] = None,
    sort: Optional[str] = None,
    db: Session = Depends(get_db)
):
    items, total = order_service.get_all(db, page, limit, customerId, dateFrom, dateTo, sort)
    pages = math.ceil(total / limit) if total > 0 else 0
    return PaginatedResponse(items=items, total=total, page=page, limit=limit, pages=pages)

@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return order_service.get_by_id(db, order_id)

@router.post("", response_model=OrderResponse, status_code=201)
def create_order(data: OrderCreate, db: Session = Depends(get_db)):
    return order_service.create(db, data)

@router.put("/{order_id}", response_model=OrderResponse)
def replace_order(order_id: int, data: OrderCreate, db: Session = Depends(get_db)):
    return order_service.replace(db, order_id, data)

@router.patch("/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, data: OrderUpdate, db: Session = Depends(get_db)):
    return order_service.update(db, order_id, data)

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order_service.delete(db, order_id)
