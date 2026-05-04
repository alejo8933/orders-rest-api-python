from sqlalchemy.orm import Session
from app.repositories import customer_repository
from app.schemas.customer import CustomerCreate, CustomerUpdate
from app.models.customer import Customer
from app.utils.errors import raise_not_found

class CustomerService:
    def get_by_id(self, db: Session, customer_id: int):
        customer = customer_repository.get_by_id(db, customer_id)
        if not customer:
            raise_not_found("Customer", customer_id)
        return customer

    def get_all(self, db: Session, page: int, limit: int, search: str, country: str, city: str):
        skip = (page - 1) * limit
        return customer_repository.get_all(db, skip=skip, limit=limit, search=search, country=country, city=city)

    def create(self, db: Session, data: CustomerCreate):
        customer = Customer(**data.model_dump())
        return customer_repository.create(db, customer)

    def update(self, db: Session, customer_id: int, data: CustomerUpdate):
        customer = self.get_by_id(db, customer_id)
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(customer, key, value)
        return customer_repository.update(db, customer)

customer_service = CustomerService()
