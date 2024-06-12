from sqlalchemy import Column, Integer, String, Float
from .database import Base

class ShoppingItem(Base):
    __tablename__ = "shopping_items"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Float)
    unit = Column(String)