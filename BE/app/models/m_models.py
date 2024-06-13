"""
Questo file definisce i modelli principali del database utilizzando SQLAlchemy.
Include i modelli per gli utenti e gli articoli.
"""

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    """
    Il modello User rappresenta un utente nel sistema.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

class Item(Base):
    """
    Il modello Item rappresenta un articolo nel sistema.
    """
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="items")

"""
Descrizione delle componenti:

1. **User**: Modello che rappresenta gli utenti. Include id, email, hashed_password, is_active e items (relazione con Item).
2. **Item**: Modello che rappresenta gli articoli. Include id, title, description, owner_id e owner (relazione con User).
"""
