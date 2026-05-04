from sqlalchemy.orm import Session
from app.models.customer import Customer

class CustomerRepository:
    def get_by_id(self, db: Session, customer_id: int):
        return db.query(Customer).filter(Customer.id == customer_id).first()
    
    def get_all(self, db: Session, skip: int = 0, limit: int = 10, search: str = None, country: str = None, city: str = None):
        query = db.query(Customer)
        if search:
            query = query.filter(
                (Customer.firstName.ilike(f"%{search}%")) |
                (Customer.lastName.ilike(f"%{search}%"))
            )
        if country:
            query = query.filter(Customer.country == country)
        if city:
            query = query.filter(Customer.city == city)
            
        total = query.count()
        items = query.offset(skip).limit(limit).all()
        return items, total

    def create(self, db: Session, customer: Customer):
        db.add(customer)
        db.commit()
        db.refresh(customer)
        return customer

    def update(self, db: Session, customer: Customer):
        db.commit()
        db.refresh(customer)
        return customer
