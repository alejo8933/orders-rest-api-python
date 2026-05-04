from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    orderDate = Column(Date, nullable=False)
    orderNumber = Column(String, unique=True, index=True, nullable=False)
    customerId = Column(Integer, ForeignKey("customers.id"), nullable=False)
    totalAmount = Column(Float, default=0.0, nullable=False)

    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
