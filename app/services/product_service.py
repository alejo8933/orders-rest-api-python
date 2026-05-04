from sqlalchemy.orm import Session
from app.repositories import product_repository
from app.utils.errors import raise_not_found

class ProductService:
    def get_by_id(self, db: Session, product_id: int):
        product = product_repository.get_by_id(db, product_id)
        if not product:
            raise_not_found("Product", product_id)
        return product

    def get_all(self, db: Session, page: int, limit: int, search: str, supplier_id: int, discontinued: bool):
        skip = (page - 1) * limit
        return product_repository.get_all(db, skip=skip, limit=limit, search=search, supplier_id=supplier_id, discontinued=discontinued)

product_service = ProductService()
