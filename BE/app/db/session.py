"""
Questo file configura la sessione del database.
Definisce un'istanza di SessionLocal che verrà utilizzata per interagire con il database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings  # Importiamo le impostazioni dell'applicazione

# Creiamo l'engine per connettersi al database utilizzando la stringa di connessione definita nelle impostazioni
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

# Creiamo una configurazione di sessione locale
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
Descrizione delle componenti:

1. **engine**: Crea l'engine per connettersi al database utilizzando la stringa di connessione definita nelle impostazioni.
2. **SessionLocal**: Configura una sessione locale per interagire con il database.
"""
