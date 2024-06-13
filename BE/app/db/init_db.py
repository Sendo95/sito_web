"""
Questo file inizializza il database, creando le tabelle necessarie e popolandolo con dati iniziali se necessario.
"""

from sqlalchemy.orm import Session
from app.db.base import Base  # Importiamo la base per tutti i modelli
from app.db.session import engine  # Importiamo l'engine per connettersi al database

# Importiamo i modelli in modo che siano registrati con SQLAlchemy
from app.models import m_models

def init_db(db: Session) -> None:
    """
    Inizializza il database, creando tutte le tabelle.
    """
    # Crea tutte le tabelle definite dai modelli che ereditano da Base
    Base.metadata.create_all(bind=engine)

    # Popolamento dei dati iniziali (opzionale)
    # Esempio: Creazione di un utente amministratore
    # from app.models.m_user import User
    # from app.core.security import get_password_hash
    # admin_user = User(email="admin@example.com", hashed_password=get_password_hash("admin"), is_active=True)
    # db.add(admin_user)
    # db.commit()

"""
Descrizione delle componenti:

1. **init_db**: Funzione per inizializzare il database, creando tutte le tabelle e popolandolo con dati iniziali se necessario.
2. **Base.metadata.create_all**: Crea tutte le tabelle definite dai modelli che ereditano da Base.
"""
