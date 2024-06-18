"""
Questo file rende la cartella 'core' un modulo Python e può essere utilizzato per centralizzare le configurazioni comuni
e le utility che verranno utilizzate in altre parti del progetto.
"""
'''
# Importiamo le configurazioni dal file config.py
from app.core.config import settings

# Importiamo le utility di sicurezza dal file security.py
from app.core.security import create_access_token, verify_password, get_password_hash

# Importiamo le dipendenze comuni dal file dependencies.py
from app.core.dependencies import get_db, get_current_user

"""
Descrizione delle importazioni:

- settings: Oggetto delle configurazioni globali dell'applicazione, generalmente gestito da Pydantic.
- create_access_token, verify_password, get_password_hash: Funzioni di utilità per la gestione della sicurezza,
  come la creazione e verifica di token JWT, e hashing delle password.
- get_db, get_current_user: Dipendenze comuni per l'injection nei vari endpoint, come ottenere la sessione del database
  o l'utente attualmente autenticato.
"""

# Qui puoi aggiungere altre importazioni o configurazioni comuni che potrebbero essere necessarie in tutto il progetto.
# Ad esempio, potresti configurare loggers, gestire connessioni esterne, ecc.

# Esempio di configurazione di un logger (opzionale)
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Core module initialized")

# Aggiungi altre inizializzazioni o configurazioni che ritieni necessarie
'''