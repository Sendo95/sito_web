"""
Questo file definisce le funzioni specifiche per la gestione degli utenti,
inclusi operazioni CRUD (Create, Read, Update, Delete).
"""

from sqlalchemy.orm import Session
from app.models.m_models import User
from app.models.m_schemas import UserCreate, UserUpdate
from app.core.security import get_password_hash

def get_user(db: Session, user_id: int) -> User:
    """
    Ritorna un utente specifico tramite il suo ID.
    """
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User:
    """
    Ritorna un utente specifico tramite il suo email.
    """
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 10) -> list[User]:
    """
    Ritorna una lista di utenti, con supporto per la paginazione.
    """
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate) -> User:
    """
    Crea un nuovo utente nel database.
    """
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: User, user_in: UserUpdate) -> User:
    """
    Aggiorna un utente esistente nel database.
    """
    update_data = user_in.dict(skip_defaults=True)
    for field in update_data:
        if field in update_data:
            setattr(user, field, update_data[field])
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int) -> User:
    """
    Cancella un utente esistente nel database.
    """
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return user

"""
Descrizione delle funzioni CRUD:

1. **get_user**: Ritorna un utente specifico tramite il suo ID.
2. **get_user_by_email**: Ritorna un utente specifico tramite il suo email.
3. **get_users**: Ritorna una lista di utenti, con supporto per la paginazione.
4. **create_user**: Crea un nuovo utente nel database.
5. **update_user**: Aggiorna un utente esistente nel database.
6. **delete_user**: Cancella un utente esistente nel database.
"""
