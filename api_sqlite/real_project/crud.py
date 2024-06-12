from sqlalchemy.orm import Session
from . import models

def get_list(db: Session):
    return db.query(models.ShoppingItem).all()

def add_to_list(db: Session, name: str, quantity: float, unit: str):
    item = db.query(models.ShoppingItem).filter(models.ShoppingItem.name == name, models.ShoppingItem.unit == unit).first()
    if item:
        item.quantity += quantity
    else:
        item = models.ShoppingItem(name=name, quantity=quantity, unit=unit)
        db.add(item)
    db.commit()
    db.refresh(item)
    return item

def remove_from_list(db: Session, name: str):
    item = db.query(models.ShoppingItem).filter(models.ShoppingItem.name == name).first()
    if item:
        db.delete(item)
        db.commit()

def clean_list(db: Session):
    db.query(models.ShoppingItem).delete()
    db.commit()
