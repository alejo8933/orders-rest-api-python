from sqlalchemy.orm import Session
from app.models.order_item import OrderItem

class OrderItemRepository:
    def get_by_id(self, db: Session, item_id: int):
        return db.query(OrderItem).filter(OrderItem.id == item_id).first()
        
    def get_by_order_id(self, db: Session, order_id: int):
        return db.query(OrderItem).filter(OrderItem.orderId == order_id).all()

    def create(self, db: Session, order_item: OrderItem):
        db.add(order_item)
        db.commit()
        db.refresh(order_item)
        return order_item

    def update(self, db: Session, order_item: OrderItem):
        db.commit()
        db.refresh(order_item)
        return order_item
        
    def delete(self, db: Session, order_item: OrderItem):
        db.delete(order_item)
        db.commit()
