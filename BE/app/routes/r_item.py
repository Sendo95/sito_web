"""
Questo file definisce le rotte per la gestione degli articoli (items).
Include endpoint per creare, leggere, aggiornare e cancellare articoli.
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_active_user
from app.models.m_schemas import Item, ItemCreate, ItemUpdate
from app.models.m_models import Item as DBItem
from app.models.m_item import create_item, get_items, get_item, update_item, delete_item

router = APIRouter()

@router.post("/", response_model=Item)
def create_new_item(
    item_in: ItemCreate, 
    db: Session = Depends(get_db), 
    current_user: DBItem = Depends(get_current_active_user)
):
    """
    Endpoint per creare un nuovo articolo. Richiede autenticazione.
    """
    return create_item(db=db, item=item_in, user_id=current_user.id)

@router.get("/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Endpoint per ottenere una lista di articoli. Supporta la paginazione tramite i parametri skip e limit.
    """
    items = get_items(db, skip=skip, limit=limit)
    return items

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    Endpoint per ottenere un articolo specifico tramite il suo ID.
    """
    item = get_item(db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=Item)
def update_existing_item(
    item_id: int, 
    item_in: ItemUpdate, 
    db: Session = Depends(get_db), 
    current_user: DBItem = Depends(get_current_active_user)
):
    """
    Endpoint per aggiornare un articolo esistente. Richiede autenticazione.
    """
    item = get_item(db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    if item.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return update_item(db=db, item=item, item_in=item_in)

@router.delete("/{item_id}", response_model=Item)
def delete_existing_item(
    item_id: int, 
    db: Session = Depends(get_db), 
    current_user: DBItem = Depends(get_current_active_user)
):
    """
    Endpoint per cancellare un articolo esistente. Richiede autenticazione.
    """
    item = get_item(db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    if item.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return delete_item(db=db, item_id=item_id)