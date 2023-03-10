# Configurações gerais.
from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = '/ap1/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:testepostegres@localhost:5432/faculdade"

    class Config:
        case_sensitive = True


settings: Settings = Settings()
