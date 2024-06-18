from fastapi import APIRouter

router = APIRouter()

@router.get("/prova")
async def get_prova():
    return {"message": "Hello World"}
