from typing import Optional
from pydantic import BaseModel

class Context(BaseModel):
    
    owner_id : str
    url : Optional[ str ] = ''
    access_token : Optional[ str ] = ''
    content_type : Optional[ str ] = 'application/json'
    
    