"""
Questo file rende la cartella 'tests' un modulo Python e può essere utilizzato
per importare configurazioni di test comuni o setup.
"""

# Importiamo le configurazioni di test comuni, se necessarie
# Esempio: Configurazione di pytest
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def test_client():
    """
    Fixture per creare un client di test utilizzato nei test.
    """
    yield client

"""
Descrizione delle componenti:

1. **pytest.fixture**: Crea una fixture che può essere utilizzata nei test.
2. **TestClient**: Utilizzato per creare un client di test per l'applicazione FastAPI.
"""
