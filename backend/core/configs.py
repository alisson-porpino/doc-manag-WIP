from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta
from fastapi.templating import Jinja2Templates
from typing import ClassVar
from pathlib import Path


class Settings(BaseSettings):

    API_V1_STR: str = '/api/v1'

    DB_URL: str = 'postgresql+asyncpg://postgres:1212@localhost:5432/doc-manag'
    #DB_URL: str = 'sqlite+aiosqlite:///./teste.db/'
    DBBaseModel: DeclarativeMeta = declarative_base()

    TEMPLATES: ClassVar[Jinja2Templates]  = Jinja2Templates(directory='templates')
    MEDIA: ClassVar[Path] = Path('media')

    class Config:
        case_sensitive = True


settings: Settings = Settings()