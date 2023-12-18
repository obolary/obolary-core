from pydantic_settings import BaseSettings

class Config(BaseSettings):
    log_trace_enabled : bool = True
    log_debug_enabled : bool = False
    pod_name : str = ''
    pod_ip : str = ''
    
config = Config( log_debug_enabled = True )
