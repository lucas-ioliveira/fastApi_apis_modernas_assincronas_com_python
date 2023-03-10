# Configurações gerais.
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    '''
    Configurações gerais usadas na aplicação.
    '''
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:senha_do_banco_de_dados@localhost:5432/nome_banco_de_dados"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
