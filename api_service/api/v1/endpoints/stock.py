from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def getStock(q: str):
  return {
    "message": f"This is your stock {q}"
  }