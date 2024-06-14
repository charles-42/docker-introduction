from fastapi import FastAPI, HTTPException 
from fastapi.testclient import TestClient 
import pytest
from main import app

client = TestClient(app) 

def test_get_home(): 
    response = client.get("/") 
    assert response.status_code == 200 
    assert response.json() == {"message": "Hello World"} 
    

def test_get_list(): 
    response = client.get("/liste") 
    assert response.status_code == 200 
    assert response.json() == {"content": []} 

def test_add_to_list(): 
    response = client.post("/liste", params={"element":5}) 
    assert response.status_code == 200 
    assert response.json() == {"content": [5]} 
    
    response = client.post("/liste", params={"element":"hello"}) 
    assert response.status_code == 422 


def test_remove_from_list(): 
    # je test que j'arrive à enlever un élément qui est bien dans ma liste
    response = client.delete("/liste", params={"element": 5}) 
    assert response.status_code == 200 
    assert response.json() == {"content": []} 

    # je test que quand je donne autre chose qu'integer j'obtiens une erreur lié au validateur (erreur 422)
    response = client.delete("/liste", params={"element": "world"}) 
    assert response.status_code == 422

    # je teste que si j'enlève un élement qui n'est pas dans ma liste, j'obtiens une erreur 404
    response = client.delete("/liste", params={"element": 8}) 
    assert response.status_code == 404
    assert response.json() == {"detail":"Element not found in the list"}