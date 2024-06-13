from fastapi import FastAPI
from app.routes.api_v1_routes import api_v1_router
from app.db.session import engine
from app.db.base import Base

# Inizializzazione del database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclusione dei router
app.include_router(api_v1_router, prefix="/api/v1")

@app.get("/")
def read_root():
    print("fatta la get root")
    return {"message": "funziona"}
