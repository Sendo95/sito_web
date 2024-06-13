"""
Questo file definisce i test per le funzionalità degli utenti.
"""

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.tests import test_client

def test_read_users(test_client: TestClient, db: Session):
    """
    Test per l'endpoint di lettura di utenti.
    """
    response = test_client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_current_user(test_client: TestClient, db: Session):
    """
    Test per l'endpoint di lettura dell'utente attualmente autenticato.
    """
    response = test_client.get("/users/me")
    assert response.status_code == 200
    assert "email" in response.json()

def test_update_current_user(test_client: TestClient, db: Session):
    """
    Test per l'endpoint di aggiornamento dell'utente attualmente autenticato.
    """
    response = test_client.put("/users/me", json={"email": "updated@example.com", "password": "newpassword"})
    assert response.status_code == 200
    assert response.json()["email"] == "updated@example.com"

def test_delete_current_user(test_client: TestClient, db: Session):
    """
    Test per l'endpoint di cancellazione dell'utente attualmente autenticato.
    """
    response = test_client.delete("/users/me")
    assert response.status_code == 200
    assert "email" in response.json()

"""
Descrizione dei test:

1. **test_read_users**: Test per l'endpoint di lettura di utenti. Verifica che l'endpoint ritorni una lista di utenti.
2. **test_read_current_user**: Test per l'endpoint di lettura dell'utente attualmente autenticato. Verifica che l'utente autenticato possa ottenere le proprie informazioni.
3. **test_update_current_user**: Test per l'endpoint di aggiornamento dell'utente attualmente autenticato. Verifica che l'utente possa aggiornare le proprie informazioni.
4. **test_delete_current_user**: Test per l'endpoint di cancellazione dell'utente attualmente autenticato. Verifica che l'utente possa cancellare il proprio account.
"""
