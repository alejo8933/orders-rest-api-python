from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    orderId = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    productId = Column(Integer, ForeignKey("products.id"), nullable=False)
    unitPrice = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")
