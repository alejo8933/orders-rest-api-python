from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    productName = Column(String, index=True, nullable=False)
    supplierId = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    unitPrice = Column(Float, nullable=False)
    package = Column(String, nullable=False)
    isDiscontinued = Column(Boolean, default=False, nullable=False)

    supplier = relationship("Supplier", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")
