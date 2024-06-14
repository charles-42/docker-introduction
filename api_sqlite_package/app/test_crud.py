# conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import models
from app.models import Base
from sqlalchemy.exc import IntegrityError

@pytest.fixture(scope="module")
def nombre():
    return 42


@pytest.fixture(scope="module")
def test_db():
    # Crée une base de données SQLite en mémoire
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    db = TestingSessionLocal()
    
    yield db

    db.close()

    # try:
    #     yield db
    # finally:
    #     db.close()
    #     Base.metadata.drop_all(bind=engine)

# test_crud.py
from app import models, crud  # Assurez-vous que les fonctions CRUD sont importées correctement

def test_add_to_list(test_db):
    # Ajouter un élément à la liste
    item_return = crud.add_to_list(test_db, name="Apples", quantity=5, unit="kg")
    assert item_return.name == "Apples"
    assert item_return.quantity == 5
    assert item_return.unit == "kg"

    item_in_db = test_db.query(models.ShoppingItem).filter(models.ShoppingItem.name == "Apples").first()
    assert item_in_db is not None
    assert item_in_db.name == "Apples"
    assert item_in_db.quantity == 5
    assert item_in_db.unit == "kg"

    item_return = crud.add_to_list(test_db, name="Apples", quantity=5, unit="kg")
    assert item_return.name == "Apples"
    assert item_return.quantity == 10
    assert item_return.unit == "kg"

    item_in_db = test_db.query(models.ShoppingItem).filter(models.ShoppingItem.name == "Apples").first()
    assert item_in_db is not None
    assert item_in_db.name == "Apples"
    assert item_in_db.quantity == 10
    assert item_in_db.unit == "kg"

    with pytest.raises(IntegrityError):
        crud.add_to_list(test_db, name="Apples", quantity=5, unit="grams")
    test_db.rollback() 

# def test_get_list(test_db):
#     # Récupérer les éléments de la liste
#     items = crud.get_list(test_db)
#     assert len(items) == 1
#     assert items[0].name == "Apples"

# def test_update_quantity(test_db):
#     # Ajouter une quantité à un élément existant
#     item = crud.add_to_list(test_db, name="Apples", quantity=3, unit="kg")
#     assert item.quantity == 13  # 5 (précédent) + 3 (ajouté)

# def test_remove_from_list(test_db):
#     # Supprimer un élément de la liste
#     crud.remove_from_list(test_db, name="Apples")
#     items = crud.get_list(test_db)
#     assert len(items) == 0

# def test_clean_list(test_db):
#     # Ajouter des éléments et nettoyer la liste
#     crud.add_to_list(test_db, name="Oranges", quantity=2, unit="kg")
#     crud.add_to_list(test_db, name="Bananas", quantity=3, unit="kg")
#     crud.clean_list(test_db)
#     items = crud.get_list(test_db)
#     assert len(items) == 0
