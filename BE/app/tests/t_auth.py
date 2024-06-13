"""
Questo file definisce i test per le funzionalità di autenticazione.
"""

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.tests import test_client

def test_login(test_client: TestClient, db: Session):
    """
    Test per l'endpoint di login.
    """
    response = test_client.post("/auth/login", data={"username": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_register(test_client: TestClient, db: Session):
    """
    Test per l'endpoint di registrazione.
    """
    response = test_client.post("/auth/register", json={"email": "newuser@example.com", "password": "newpassword"})
    assert response.status_code == 200
    assert response.json()["email"] == "newuser@example.com"

"""
Descrizione dei test:

1. **test_login**: Test per l'endpoint di login. Verifica che la risposta contenga un token di accesso.
2. **test_register**: Test per l'endpoint di registrazione. Verifica che un nuovo utente possa registrarsi correttamente.
"""
