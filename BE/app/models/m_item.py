"""
Questo file definisce il modello SQLAlchemy per gli articoli (items).
Include la definizione della tabella, le colonne e le relazioni con altri modelli,
così come le funzioni per creare, leggere, aggiornare e cancellare articoli.
"""

from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from typing import List

from app.db.base import Base
from app.models.m_schemas import ItemCreate, ItemUpdate

class Item(Base):
    """
    Il modello Item rappresenta un articolo nel sistema.
    """
    __tablename__ = 'items'  # Nome della tabella nel database

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=True)
    owner_id = Column(Integer, ForeignKey('users.id'))  # Foreign key per la relazione con il modello User

    owner = relationship("User", back_populates="items")


def create_item(db: Session, item: ItemCreate, user_id: int) -> Item:
    """
    Crea un nuovo articolo.
    """
    db_item = Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 10) -> List[Item]:
    """
    Ottiene una lista di articoli con supporto per la paginazione.
    """
    return db.query(Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int) -> Item:
    """
    Ottiene un articolo specifico tramite il suo ID.
    """
    return db.query(Item).filter(Item.id == item_id).first()

def update_item(db: Session, item: Item, item_in: ItemUpdate) -> Item:
    """
    Aggiorna un articolo esistente.
    """
    for var, value in vars(item_in).items():
        setattr(item, var, value) if value else None
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def delete_item(db: Session, item_id: int) -> Item:
    """
    Cancella un articolo esistente.
    """
    item = db.query(Item).filter(Item.id == item_id).first()
    db.delete(item)
    db.commit()
    return item
