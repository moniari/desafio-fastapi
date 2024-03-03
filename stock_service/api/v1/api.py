from fastapi import APIRouter
from api.v1.endpoints import test, stock

api_router = APIRouter()
api_router.include_router(test.router, prefix="/test", tags=["test"])
api_router.include_router(stock.router, prefix="/stock", tags=["stock"])