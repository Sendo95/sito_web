"""
Questo file rende la cartella 'db' un modulo Python e può essere utilizzato per centralizzare le configurazioni comuni
e le utility che verranno utilizzate per la gestione del database.
"""

# Importiamo la funzione per inizializzare il database dal file init_db.py
from .init_db import init_db

# Importiamo la base del modello SQLAlchemy dal file base.py
from .base import Base

"""
Descrizione delle importazioni:

- init_db: Funzione per inizializzare il database, ad esempio per creare le tabelle iniziali o popolare dati di test.
- Base: Base per tutti i modelli SQLAlchemy. Tutti i modelli dovrebbero ereditare da questa base.
"""

# Esegui l'inizializzazione del database (opzionale)
# init_db()

# Qui puoi aggiungere altre importazioni o configurazioni comuni che potrebbero essere necessarie in tutto il progetto.
# Ad esempio, potresti configurare loggers specifici per il database, gestire connessioni esterne, ecc.

# Esempio di configurazione di un logger specifico per il database (opzionale)
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Database module initialized")

# Aggiungi altre inizializzazioni o configurazioni che ritieni necessarie
