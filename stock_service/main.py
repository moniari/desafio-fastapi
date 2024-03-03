from fastapi import FastAPI
from config.config import settings
from api.v1.api import api_router as api_router_v1
import uvicorn

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.include_router(api_router_v1, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)