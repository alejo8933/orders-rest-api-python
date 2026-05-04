from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    companyName = Column(String, index=True, nullable=False)
    contactName = Column(String, nullable=False)
    contactTitle = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    fax = Column(String, nullable=True)

    products = relationship("Product", back_populates="supplier")
