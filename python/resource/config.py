from pydantic_settings import BaseSettings

class Config(BaseSettings):
    
    resource_host : str
    
config = Config()
