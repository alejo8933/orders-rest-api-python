from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from app.models.order import Order
from datetime import date

class OrderRepository:
    def get_by_id(self, db: Session, order_id: int):
        return db.query(Order).options(
            joinedload(Order.customer),
            joinedload(Order.items)
        ).filter(Order.id == order_id).first()
        
    def get_last_order(self, db: Session):
        return db.query(Order).order_by(Order.id.desc()).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 10, customer_id: int = None, date_from: date = None, date_to: date = None, sort: str = None):
        query = db.query(Order).options(
            joinedload(Order.customer),
            joinedload(Order.items)
        )
        if customer_id is not None:
            query = query.filter(Order.customerId == customer_id)
        if date_from:
            query = query.filter(Order.orderDate >= date_from)
        if date_to:
            query = query.filter(Order.orderDate <= date_to)
            
        if sort == "date_desc":
            query = query.order_by(Order.orderDate.desc())
        elif sort == "date_asc":
            query = query.order_by(Order.orderDate.asc())
        else:
            query = query.order_by(Order.id.desc())
            
        total = query.count()
        items = query.offset(skip).limit(limit).all()
        return items, total

    def create(self, db: Session, order: Order):
        db.add(order)
        db.commit()
        db.refresh(order)
        return order

    def update(self, db: Session, order: Order):
        db.commit()
        db.refresh(order)
        return order
        
    def delete(self, db: Session, order: Order):
        db.delete(order)
        db.commit()
