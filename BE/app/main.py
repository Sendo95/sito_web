import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.api_v1_routes import api_v1_router
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
"http://localhost:8000",
]

app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=[""],
allow_headers=[""],
)

app.include_router(api_v1_router, prefix="/api/v1")

@app.get("/")
def read_root():
    print("fatta la get root")
    return {"message": "funziona"}
