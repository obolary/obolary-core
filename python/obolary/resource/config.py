from typing import Optional
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    
    resource_host : Optional[ str ] = 'http://127.0.0.1:8080'
    
config = Config()
