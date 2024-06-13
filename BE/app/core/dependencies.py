"""
Questo file contiene le dipendenze comuni per l'applicazione FastAPI. Le dipendenze vengono utilizzate per estrarre
e condividere la logica comune tra diversi endpoint.
"""

from typing import Generator, Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.m_models import User
from app.models.m_user import get_user_by_email
from app.db.session import SessionLocal

# Dependency per ottenere la sessione del database
def get_db() -> Generator:
    """
    Ritorna una sessione del database. Questa dipendenza viene utilizzata in molti endpoint
    per interagire con il database tramite SQLAlchemy.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Dependency per l'autenticazione basata su token JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
    """
    Ritorna l'utente attualmente autenticato, basandosi sul token JWT fornito.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """
    Ritorna l'utente attualmente attivo, verificando che l'utente non sia disabilitato.
    """
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

"""
Descrizione delle dipendenze:

1. **get_db**: Questa funzione fornisce una sessione del database SQLAlchemy. Viene utilizzata come dipendenza in molti
   endpoint per interagire con il database.
2. **oauth2_scheme**: Istanza di OAuth2PasswordBearer, utilizzata per estrarre e verificare i token JWT dagli header
   delle richieste.
3. **get_current_user**: Questa funzione estrae l'utente attualmente autenticato dal token JWT. Decodifica il token,
   verifica la validità e recupera l'utente dal database.
4. **get_current_active_user**: Questa funzione verifica che l'utente autenticato sia attivo. Viene utilizzata come
   dipendenza per endpoint che richiedono che l'utente sia attivo.
"""
