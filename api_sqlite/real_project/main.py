from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Bonjour, bienvenue sur l’API liste de course"}

@app.get("/get_list")
def get_list(db: Session = Depends(get_db)):
    items = crud.get_list(db)
    if not items:
        return {"message": "La liste est vide"}
    return items

@app.post("/add_to_list")
def add_to_list(name: str, quantity: float, unit: str, db: Session = Depends(get_db)):
    return crud.add_to_list(db, name, quantity, unit)

@app.delete("/remove_from_list")
def remove_from_list(name: str, db: Session = Depends(get_db)):
    crud.remove_from_list(db, name)
    return {"message": "Item removed"}

@app.delete("/clean_list")
def clean_list(db: Session = Depends(get_db)):
    crud.clean_list(db)
    return {"message": "List cleaned"}
