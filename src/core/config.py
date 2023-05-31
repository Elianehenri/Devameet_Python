from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    log_level: str = 'info'
    db_url: str
    jwt_secret: str
    jwt_algorithm: str
    jwt_expirations: int

    class Config:
        env_file = '.env'
    
@lru_cache( )
def get_settings( ):
    
    return Settings( )
