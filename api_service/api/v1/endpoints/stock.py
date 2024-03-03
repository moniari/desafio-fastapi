from fastapi import APIRouter
from utils.logs import generate_log
from config.config import settings
import httpx

router = APIRouter()

@router.get("/")
async def getStock(q: str):
  stockName = q.lower()
                                  # f"api/v1/stock?stock={q}"
  url = settings.STOCK_API_URL + f"/api/v1/stock?stock={q}"

  try:
    async with httpx.AsyncClient() as client:
      response = await client.get(url)

      generate_log(
        False,
        "POST",
        q,
        f"Stock infos for {q} retrieved with success"
      )

      json_response = response.json()

      return json_response
    
  except:
    generate_log(
      True,
      "POST",
      q,
      f"Failed to access Stock service and fetch infos for {q}"
    )

    return {
      "message": f"Failed to access Stock service and fetch infos for {q}"
    }