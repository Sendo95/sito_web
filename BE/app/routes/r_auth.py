"""
Questo file definisce le rotte per l'autenticazione, inclusi login e registrazione.
Utilizza OAuth2 e JWT per gestire l'autenticazione.
"""

from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.core.security import create_access_token, verify_password, get_password_hash
from app.models.m_schemas import Token, UserCreate, User
from app.models.m_models import User as DBUser
from app.models.m_user import get_user_by_email, create_user

router = APIRouter()

@router.post("/login", response_model=Token)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint per il login dell'utente. Verifica le credenziali e ritorna un token di accesso JWT.
    """
    user = get_user_by_email(db, email=form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=60)  # Definisce la durata del token di accesso
    access_token = create_access_token(subject=user.email, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=User)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint per la registrazione di un nuovo utente. Crea un nuovo utente nel database.
    """
    user = get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    new_user = create_user(db=db, user=user_in)
    return new_user