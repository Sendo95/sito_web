from fastapi import APIRouter

router = APIRouter()

@router.get("/prova")
async def get_prova():
    print("chiamato prova")
    return {"message": "Hello World"}
