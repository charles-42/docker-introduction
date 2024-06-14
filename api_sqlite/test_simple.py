
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from simple import app  # Assurez-vous que votre application et la fonction get_db soient importées correctement

# Créez une base de données en mémoire pour les tests
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dépendance de la base de données de test
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def setup_module(module):
    # Créez toutes les tables dans la base de données de test
    from models import Base  # Assurez-vous que vos modèles sont correctement importés
    Base.metadata.create_all(bind=engine)

def teardown_module(module):
    # Supprimez toutes les tables de la base de données de test
    from models import Base  # Assurez-vous que vos modèles sont correctement importés
    Base.metadata.drop_all(bind=engine)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bonjour, bienvenue sur l’API liste de course"}

def test_home():
    response = client.get("/home")
    assert response.status_code == 200
    assert response.json() == {"message": "Bonjour, bienvenue à la maison"}

def test_get_list_empty():
    response = client.get("/get_list")
    assert response.status_code == 200
    assert response.json() == {"message": "La liste est vide"}

def test_add_to_list():
    response = client.post("/add_to_list", json={"name": "Tomate", "quantity": 2.0, "unit": "kg"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Tomate"
    assert data["quantity"] == 2.0
    assert data["unit"] == "kg"

def test_add_to_list_existing_item():
    client.post("/add_to_list", json={"name": "Tomate", "quantity": 2.0, "unit": "kg"})
    response = client.post("/add_to_list", json={"name": "Tomate", "quantity": 1.0, "unit": "kg"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Tomate"
    assert data["quantity"] == 3.0
    assert data["unit"] == "kg"

def test_remove_from_list():
    client.post("/add_to_list", json={"name": "Tomate", "quantity": 2.0, "unit": "kg"})
    response = client.delete("/remove_from_list", json={"name": "Tomate"})
    assert response.status_code == 200
    assert response.json() == {"message": "Item removed"}

def test_remove_from_list_not_found():
    response = client.delete("/remove_from_list", json={"name": "NonExistentItem"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_clean_list():
    client.post("/add_to_list", json={"name": "Tomate", "quantity": 2.0, "unit": "kg"})
    response = client.delete("/clean_list")
    assert response.status_code == 200
    assert response.json() == {"message": "List cleaned"}
    response = client.get("/get_list")
    assert response.status_code == 200
    assert response.json() == {"message": "La liste est vide"}