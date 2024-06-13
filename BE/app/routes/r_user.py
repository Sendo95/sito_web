"""
Questo file definisce le rotte per la gestione degli utenti.
Include endpoint per ottenere informazioni sugli utenti, aggiornare i profili e cancellare utenti.
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_active_user
from app.models.m_schemas import User, UserUpdate
from app.models.m_models import User as DBUser
from app.models.m_user import get_user, get_users, update_user, delete_user

router = APIRouter()

@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Endpoint per ottenere una lista di utenti. Supporta la paginazione tramite i parametri skip e limit.
    """
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.get("/me", response_model=User)
def read_current_user(current_user: DBUser = Depends(get_current_active_user)):
    """
    Endpoint per ottenere le informazioni dell'utente attualmente autenticato.
    """
    return current_user

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Endpoint per ottenere un utente specifico tramite il suo ID.
    """
    user = get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.put("/me", response_model=User)
def update_current_user(
    user_in: UserUpdate, 
    db: Session = Depends(get_db), 
    current_user: DBUser = Depends(get_current_active_user)
):
    """
    Endpoint per aggiornare il profilo dell'utente attualmente autenticato.
    """
    updated_user = update_user(db=db, user=current_user, user_in=user_in)
    return updated_user

@router.delete("/me", response_model=User)
def delete_current_user(
    db: Session = Depends(get_db), 
    current_user: DBUser = Depends(get_current_active_user)
):
    """
    Endpoint per cancellare l'utente attualmente autenticato.
    """
    deleted_user = delete_user(db=db, user_id=current_user.id)
    return deleted_user