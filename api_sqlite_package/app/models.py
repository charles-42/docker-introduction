from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class ShoppingItem(Base):
    __tablename__ = "shopping_items"

    name = Column(String, primary_key=True,index=True)
    quantity = Column(Float)
    unit = Column(String)