from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from app.models.product import Product

class ProductRepository:
    def get_by_id(self, db: Session, product_id: int):
        return db.query(Product).options(joinedload(Product.supplier)).filter(Product.id == product_id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 10, search: str = None, supplier_id: int = None, discontinued: bool = None):
        query = db.query(Product).options(joinedload(Product.supplier))
        if search:
            query = query.filter(Product.productName.ilike(f"%{search}%"))
        if supplier_id is not None:
            query = query.filter(Product.supplierId == supplier_id)
        if discontinued is not None:
            query = query.filter(Product.isDiscontinued == discontinued)
            
        total = query.count()
        items = query.offset(skip).limit(limit).all()
        return items, total

    def create(self, db: Session, product: Product):
        db.add(product)
        db.commit()
        db.refresh(product)
        return product
