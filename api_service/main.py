from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from config.config import settings
from api.v1.api import api_router as api_router_v1
from middlewares.authentication import decodeBase64
import uvicorn

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

@app.middleware("http")
async def check_user_permissions(request: Request, call_next):  
    auth = request.headers["Authorization"]
    token = auth.split(' ')[1]  
    userData = decodeBase64(token)

    if (userData[0] != settings.AUTH_USERNAME or userData[1] != settings.AUTH_PASSWORD):
        return JSONResponse("Invalid Authentication data!", 401)

    response = await call_next(request)
    
    return response
    

app.include_router(api_router_v1, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7777)

