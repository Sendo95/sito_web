"""
Questo file rende la cartella 'routes' un modulo Python e aggrega tutti i router definiti in altri file di rotte.
In questo modo, possiamo facilmente includere tutti i router nel file principale dell'applicazione.
"""

from fastapi import APIRouter

# Importiamo i singoli router definiti nei file di rotte
from app.routes.r_user import router as user_router
from app.routes.r_item import router as item_router
from app.routes.r_auth import router as auth_router

# Creiamo un router principale che aggrega tutti i router importati
api_router = APIRouter()
api_router.include_router(user_router, prefix="/users", tags=["users"])
api_router.include_router(item_router, prefix="/items", tags=["items"])
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])

"""
Descrizione delle componenti:

1. **APIRouter**: Creiamo un router principale utilizzando FastAPI's APIRouter.
2. **Inclusione dei router**: Importiamo e includiamo i singoli router (user, item, auth) nel router principale.
3. **Prefix e tags**: Utilizziamo prefissi e tag per organizzare meglio le rotte API.
"""

# Il router principale può essere incluso nel file principale dell'applicazione (main.py) come segue:
"""
from fastapi import FastAPI
from app.routes import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
"""
