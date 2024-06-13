"""
Questo file definisce e organizza tutte le rotte per la versione 1 dell'API.
Include i router specifici per le diverse risorse e gestisce il prefisso delle rotte e i tag.
"""

from fastapi import APIRouter

# Importiamo i singoli router definiti nei file di rotte
from app.routes.r_user import router as user_router
from app.routes.r_item import router as item_router
from app.routes.r_auth import router as auth_router

# Creiamo un router principale per la versione 1 dell'API
api_v1_router = APIRouter()

# Includiamo i singoli router nel router principale
api_v1_router.include_router(user_router, prefix="/users", tags=["users"])
api_v1_router.include_router(item_router, prefix="/items", tags=["items"])
api_v1_router.include_router(auth_router, prefix="/auth", tags=["auth"])

"""
Descrizione delle componenti:

1. **APIRouter**: Creiamo un router principale utilizzando FastAPI's APIRouter.
2. **Inclusione dei router**: Importiamo e includiamo i singoli router (user, item, auth) nel router principale.
3. **Prefix e tags**: Utilizziamo prefissi e tag per organizzare meglio le rotte API.
"""
