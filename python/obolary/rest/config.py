from pydantic_settings import BaseSettings

class Config(BaseSettings):
    
    rest_host_and_port : str = ':8080'
    rest_base_path : str = '/obolary/1.0'
    
    rest_transport_max_idle_conns : int = 256
    rest_transport_max_tries : int = 3
    rest_transport_request_timeout : int = 60
    
config = Config()
