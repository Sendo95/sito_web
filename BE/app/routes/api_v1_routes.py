from fastapi import APIRouter

# Importiamo i singoli router definiti nei file di rotta
from app.routes.r_user import router as user_router
from app.routes.r_item import router as item_router
from app.routes.r_auth import router as auth_router
from app.routes.r_prova import router as prova_router

# Creiamo un router principale per la versione 1 dell'API
api_v1_router = APIRouter()

# Includiamo i singoli router nel router principale
api_v1_router.include_router(user_router, prefix="/users", tags=["users"])
api_v1_router.include_router(item_router, prefix="/items", tags=["items"])
api_v1_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_v1_router.include_router(prova_router, tags=["prova"]) 
