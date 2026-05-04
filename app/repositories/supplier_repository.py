from sqlalchemy.orm import Session
from app.models.supplier import Supplier

class SupplierRepository:
    def get_by_id(self, db: Session, supplier_id: int):
        return db.query(Supplier).filter(Supplier.id == supplier_id).first()

    def create(self, db: Session, supplier: Supplier):
        db.add(supplier)
        db.commit()
        db.refresh(supplier)
        return supplier
