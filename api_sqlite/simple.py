from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException
import os



SQLALCHEMY_DATABASE_URL = "sqlite:////data/shopping_list.db"


Base = declarative_base()


class ShoppingItem(Base):
    __tablename__ = "shopping_items"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Float)
    unit = Column(String)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Configuration de l'engine SQLAlchemy
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bonjour, bienvenue sur l’API liste de course"}

@app.get("/get_list")
def get_list():
    items = session.query(ShoppingItem).all()
    if not items:
        return {"message": "La liste est vide"}
    return items

@app.post("/add_to_list")
def add_to_list(name: str, quantity: float, unit: str):
    item = session.query(ShoppingItem).filter(ShoppingItem.name == name).first()
    if item:
        if item.unit != unit:
            raise HTTPException(status_code=400, detail="Unité incorrecte")
        else:
            item.quantity += quantity
    else:
        item = ShoppingItem(name=name, quantity=quantity, unit=unit)
        session.add(item)
    session.commit()
    session.refresh(item)
    return item


@app.delete("/remove_from_list")
def remove_from_list(name: str):
    items = session.query(ShoppingItem).filter(ShoppingItem.name == name).all()
    if items:
        for item in items:
            session.delete(item)
            session.commit()
        return {"message": "Item removed"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/clean_list")
def clean_list():
    session.query(ShoppingItem).delete()
    session.commit()
    return {"message": "List cleaned"}

#  uvicorn simple:app --reload