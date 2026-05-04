from sqlalchemy.orm import Session
from datetime import date
from app.repositories import order_repository, customer_repository, product_repository, order_item_repository
from app.schemas.order import OrderCreate, OrderUpdate
from app.models.order import Order
from app.models.order_item import OrderItem
from app.utils.errors import raise_not_found

class OrderService:
    def get_by_id(self, db: Session, order_id: int):
        order = order_repository.get_by_id(db, order_id)
        if not order:
            raise_not_found("Order", order_id)
        return order

    def get_all(self, db: Session, page: int, limit: int, customer_id: int, date_from: date, date_to: date, sort: str):
        skip = (page - 1) * limit
        return order_repository.get_all(db, skip=skip, limit=limit, customer_id=customer_id, date_from=date_from, date_to=date_to, sort=sort)

    def create(self, db: Session, data: OrderCreate):
        customer = customer_repository.get_by_id(db, data.customerId)
        if not customer:
            raise_not_found("Customer", data.customerId)

        last_order = order_repository.get_last_order(db)
        next_id = (last_order.id + 1) if last_order else 1
        order_number = f"ORD-{next_id:04d}"

        new_order = Order(
            orderDate=date.today(),
            orderNumber=order_number,
            customerId=data.customerId,
            totalAmount=0.0
        )
        created_order = order_repository.create(db, new_order)
        
        total = 0.0
        for item in data.items:
            product = product_repository.get_by_id(db, item.productId)
            if not product:
                raise_not_found("Product", item.productId)
            
            unit_price = product.unitPrice
            order_item = OrderItem(
                orderId=created_order.id,
                productId=item.productId,
                unitPrice=unit_price,
                quantity=item.quantity
            )
            order_item_repository.create(db, order_item)
            total += unit_price * item.quantity
            
        created_order.totalAmount = total
        return order_repository.update(db, created_order)

    def update(self, db: Session, order_id: int, data: OrderUpdate):
        order = self.get_by_id(db, order_id)
        if data.customerId is not None:
            customer = customer_repository.get_by_id(db, data.customerId)
            if not customer:
                raise_not_found("Customer", data.customerId)
            order.customerId = data.customerId
            
        if data.orderDate is not None:
            order.orderDate = data.orderDate
            
        return order_repository.update(db, order)
        
    def replace(self, db: Session, order_id: int, data: OrderCreate):
        order = self.get_by_id(db, order_id)
        
        customer = customer_repository.get_by_id(db, data.customerId)
        if not customer:
            raise_not_found("Customer", data.customerId)
            
        order.customerId = data.customerId
        
        # Using db object reference to delete existing items via repository
        for item in list(order.items):
            order_item_repository.delete(db, item)
            
        total = 0.0
        for item_data in data.items:
            product = product_repository.get_by_id(db, item_data.productId)
            if not product:
                raise_not_found("Product", item_data.productId)
                
            unit_price = product.unitPrice
            new_item = OrderItem(
                orderId=order.id,
                productId=item_data.productId,
                unitPrice=unit_price,
                quantity=item_data.quantity
            )
            order_item_repository.create(db, new_item)
            total += unit_price * item_data.quantity
            
        order.totalAmount = total
        return order_repository.update(db, order)

    def delete(self, db: Session, order_id: int):
        order = self.get_by_id(db, order_id)
        order_repository.delete(db, order)
        
    def recalculate_total(self, db: Session, order_id: int):
        order = self.get_by_id(db, order_id)
        items = order_item_repository.get_by_order_id(db, order_id)
        total = sum(item.unitPrice * item.quantity for item in items)
        order.totalAmount = total
        return order_repository.update(db, order)

order_service = OrderService()
