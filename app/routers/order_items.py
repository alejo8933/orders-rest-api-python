from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.order_item import OrderItemCreate, OrderItemUpdate, OrderItemResponse
from app.services.order_item_service import order_item_service

router = APIRouter(prefix="/orders", tags=["Order Items"])

@router.get("/{order_id}/items", response_model=List[OrderItemResponse])
def get_order_items(order_id: int, db: Session = Depends(get_db)):
    return order_item_service.get_items(db, order_id)

@router.post("/{order_id}/items", response_model=OrderItemResponse, status_code=201)
def create_order_item(order_id: int, data: OrderItemCreate, db: Session = Depends(get_db)):
    return order_item_service.create(db, order_id, data)

@router.patch("/{order_id}/items/{item_id}", response_model=OrderItemResponse)
def update_order_item(order_id: int, item_id: int, data: OrderItemUpdate, db: Session = Depends(get_db)):
    return order_item_service.update(db, order_id, item_id, data)

@router.delete("/{order_id}/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order_item(order_id: int, item_id: int, db: Session = Depends(get_db)):
    order_item_service.delete(db, order_id, item_id)
