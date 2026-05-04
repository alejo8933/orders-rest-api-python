from sqlalchemy.orm import Session
from app.repositories import order_item_repository, product_repository
from app.services.order_service import order_service
from app.schemas.order_item import OrderItemCreate, OrderItemUpdate
from app.models.order_item import OrderItem
from app.utils.errors import raise_not_found

class OrderItemService:
    def get_items(self, db: Session, order_id: int):
        order_service.get_by_id(db, order_id) # ensure order exists
        return order_item_repository.get_by_order_id(db, order_id)
        
    def create(self, db: Session, order_id: int, data: OrderItemCreate):
        order_service.get_by_id(db, order_id)
        product = product_repository.get_by_id(db, data.productId)
        if not product:
            raise_not_found("Product", data.productId)
            
        order_item = OrderItem(
            orderId=order_id,
            productId=data.productId,
            unitPrice=product.unitPrice,
            quantity=data.quantity
        )
        created_item = order_item_repository.create(db, order_item)
        order_service.recalculate_total(db, order_id)
        return created_item

    def update(self, db: Session, order_id: int, item_id: int, data: OrderItemUpdate):
        order_service.get_by_id(db, order_id)
        item = order_item_repository.get_by_id(db, item_id)
        if not item or item.orderId != order_id:
            raise_not_found("OrderItem", item_id)
            
        if data.quantity is not None:
            item.quantity = data.quantity
        if data.unitPrice is not None:
            item.unitPrice = data.unitPrice
            
        updated_item = order_item_repository.update(db, item)
        order_service.recalculate_total(db, order_id)
        return updated_item
        
    def delete(self, db: Session, order_id: int, item_id: int):
        order_service.get_by_id(db, order_id)
        item = order_item_repository.get_by_id(db, item_id)
        if not item or item.orderId != order_id:
            raise_not_found("OrderItem", item_id)
            
        order_item_repository.delete(db, item)
        order_service.recalculate_total(db, order_id)

order_item_service = OrderItemService()
