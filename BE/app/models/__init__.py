"""
Questo file rende la cartella 'models' un modulo Python e centralizza l'importazione di tutti i modelli
definiti nel progetto. Questo è utile per assicurare che SQLAlchemy conosca tutti i modelli quando si crea il database.
"""

# Importiamo i modelli definiti nei singoli file
from app.models.m_user import User
from app.models.m_item import Item

"""
Descrizione delle importazioni:

1. **User**: Modello che rappresenta gli utenti nel sistema.
2. **Item**: Modello che rappresenta gli articoli (items) nel sistema.
"""