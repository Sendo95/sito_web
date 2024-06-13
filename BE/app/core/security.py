"""
Questo file contiene le funzioni e le classi necessarie per gestire la sicurezza dell'applicazione,
inclusi la generazione e la verifica dei token JWT, l'hashing delle password e la verifica delle password.
"""

from datetime import datetime, timedelta
from typing import Any, Union

import jwt
from passlib.context import CryptContext

from app.core.config import settings

# Configurazione per l'hashing delle password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Algoritmo utilizzato per i token JWT
ALGORITHM = "HS256"

def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    """
    Crea un token JWT per il soggetto specificato (generalmente l'ID o l'email dell'utente).
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica che la password in chiaro corrisponda alla password hashata.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Hash della password utilizzando l'algoritmo bcrypt.
    """
    return pwd_context.hash(password)

"""
Descrizione delle funzioni:

1. **create_access_token**: Crea un token JWT per un determinato soggetto (utente). Il token include una data di scadenza.
2. **verify_password**: Verifica che una password in chiaro corrisponda al suo hash.
3. **get_password_hash**: Genera l'hash di una password utilizzando bcrypt.
"""

# Esempio di utilizzo delle funzioni di sicurezza:

# Creazione di un token di accesso per l'utente con email 'user@example.com'
token = create_access_token(subject="user@example.com")
print(f"Token di accesso generato: {token}")

# Hashing di una password
hashed_password = get_password_hash("mysecretpassword")
print(f"Password hashata: {hashed_password}")

# Verifica della password
is_valid = verify_password("mysecretpassword", hashed_password)
print(f"La password è valida: {is_valid}")
