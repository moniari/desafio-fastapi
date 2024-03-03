from fastapi import APIRouter, Request
import pandas as pd
from utils.logs import generate_log

router = APIRouter()

baseUrl = "https://stooq.com/"

@router.get("")
async def getStock(stock: str):
  try:
    url =  baseUrl + f"q/l/?s={stock}&f=sd2t2ohlcvn&h&e=csv"

    data = pd.read_csv(
        url, 
        sep=',', 
        encoding='utf-8',
        usecols=['Symbol', 'Name', 'Close'])

    generate_log(
        False,
        "POST",
        stock,
        f"Stock infos for {stock} retrieved with success"
    )

    return {
        "simbolo": data.loc[0, 'Symbol'],
        "nome_da_empresa": data.loc[0, 'Name'],
        "cotacao": data.loc[0, 'Close']
    }
  except:
    generate_log(
        True,
        "POST",
        stock,
        f"Failed to fetch stock infos for {stock}"
    )
    return {
      "message": "Error fetching stock"
    }