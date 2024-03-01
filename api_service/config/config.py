import os
from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), "env")


class Settings(BaseSettings):
    API_VERSION: str = "v1"
    API_V1_STR: str = f"/api/{API_VERSION}"
    PROJECT_NAME: str
    AUTH_USERNAME: str
    AUTH_PASSWORD: str

    # model_config = SettingsConfigDict(env_file='../.env', env_file_encoding="utf-8")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
