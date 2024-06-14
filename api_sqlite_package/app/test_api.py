# test_api.py
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.models import ShoppingItem, Base
from app.main import app, get_db  # Assume your FastAPI app is in app/main.py

# Configuration de la base de données de test

# Initialiser la base de données de test

# Remplace la dépendance get_db par une version de test
def override_get_db():
    try:
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Remplace la dépendance get_db par une dépendance envers overide get_db
app.dependency_overrides[get_db] = override_get_db


# Créer un client de test
client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bonjour, bienvenue sur l’API liste de course"}

def test_get_empty_list():
    response = client.get("/get_list")
    assert response.status_code == 200
    assert response.json() == {"message": "La liste est vide"}

def test_add_to_list():
    response = client.post("/add_to_list", params={"name": "Apples", "quantity": 5, "unit": "kg"})
    assert response.status_code == 200
    assert response.json()["name"] == "Apples"
    assert response.json()["quantity"] == 5
    assert response.json()["unit"] == "kg"

# def test_get_list():
#     response = client.get("/get_list")
#     assert response.status_code == 200
#     content = response.json()
#     assert content == {'message': 'La liste est vide'}

# def test_remove_from_list():
#     response = client.delete("/remove_from_list", params={"name": "Apples"})
#     assert response.status_code == 200
#     assert response.json() == {"message": "Item removed"}

#     response = client.get("/get_list")
#     assert response.status_code == 200
#     assert response.json() == {"message": "La liste est vide"}

# def test_clean_list():
#     client.post("/add_to_list", params={"name": "Oranges", "quantity": 2, "unit": "kg"})
#     client.post("/add_to_list", params={"name": "Bananas", "quantity": 3, "unit": "kg"})
    
#     response = client.delete("/clean_list")
#     assert response.status_code == 200
#     assert response.json() == {"message": "List cleaned"}

#     response = client.get("/get_list")
#     assert response.status_code == 200
#     assert response.json() == {"message": "La liste est vide"}
