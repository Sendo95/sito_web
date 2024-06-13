"""
Questo file definisce gli schemi Pydantic per la validazione e la serializzazione dei dati.
Include gli schemi per gli utenti e gli articoli.
"""

from pydantic import BaseModel
from typing import Optional, List

class UserBase(BaseModel):
    """
    Schema base per gli utenti, utilizzato come base per altri schemi utente.
    """
    email: str

class UserCreate(UserBase):
    """
    Schema utilizzato per la creazione di un nuovo utente.
    """
    password: str

class UserUpdate(BaseModel):
    """
    Schema utilizzato per l'aggiornamento di un utente esistente.
    """
    email: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None

class User(UserBase):
    """
    Schema completo per un utente, utilizzato nelle risposte API.
    """
    id: int
    is_active: bool
    items: List["Item"] = []

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    """
    Schema base per gli articoli, utilizzato come base per altri schemi articolo.
    """
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    """
    Schema utilizzato per la creazione di un nuovo articolo.
    """
    pass

class ItemUpdate(BaseModel):
    """
    Schema utilizzato per l'aggiornamento di un articolo esistente.
    """
    title: Optional[str] = None
    description: Optional[str] = None

class Item(ItemBase):
    """
    Schema completo per un articolo, utilizzato nelle risposte API.
    """
    id: int
    owner_id: int

    class Config:
        orm_mode = True

"""
Descrizione delle componenti:

1. **UserBase**: Schema base per gli utenti.
2. **UserCreate**: Schema per la creazione di un nuovo utente.
3. **UserUpdate**: Schema per l'aggiornamento di un utente esistente.
4. **User**: Schema completo per un utente, utilizzato nelle risposte API.
5. **ItemBase**: Schema base per gli articoli.
6. **ItemCreate**: Schema per la creazione di un nuovo articolo.
7. **ItemUpdate**: Schema per l'aggiornamento di un articolo esistente.
8. **Item**: Schema completo per un articolo, utilizzato nelle risposte API.
"""
