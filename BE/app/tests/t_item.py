"""
Questo file definisce i test per le funzionalità degli articoli (items).
"""

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.tests import test_client

def test_create_item(test_client: TestClient, db: Session):
    """
    Test per l'endpoint di creazione di un nuovo articolo.
    """
    response = test_client.post("/items/", json={"title": "New Item", "description": "Description of new item"})
    assert response.status_code == 200
    assert response.json()["title"] == "New Item"

def test_read_items(test_client: TestClient, db: Session):
    """
    Test per l'endpoint di lettura di articoli.
    """
    response = test_client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_item(test_client: TestClient, db: Session):
    """
    Test per l'endpoint di aggiornamento di un articolo.
    """
    response = test_client.put("/items/1", json={"title": "Updated Item", "description": "Updated description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Item"

def test_delete_item(test_client: TestClient, db: Session):
    """
    Test per l'endpoint di cancellazione di un articolo.
    """
    response = test_client.delete("/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

"""
Descrizione dei test:

1. **test_create_item**: Test per l'endpoint di creazione di un nuovo articolo. Verifica che un nuovo articolo possa essere creato correttamente.
2. **test_read_items**: Test per l'endpoint di lettura di articoli. Verifica che l'endpoint ritorni una lista di articoli.
3. **test_update_item**: Test per l'endpoint di aggiornamento di un articolo. Verifica che un articolo possa essere aggiornato correttamente.
4. **test_delete_item**: Test per l'endpoint di cancellazione di un articolo. Verifica che un articolo possa essere cancellato correttamente.
"""
