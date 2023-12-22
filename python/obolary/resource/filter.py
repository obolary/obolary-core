from typing import Optional, List, Self
from pydantic import BaseModel, Field

from datetime import datetime

class Filter(BaseModel):
    
    condition : Optional[ str ] = ''
    limit_number : Optional[ int ] = 100
    limit_on : Optional[ str ] = 'created'
    limit_after_inclusive : Optional[ datetime ] = None
    limit_before : Optional[ datetime ] = None
    page : Optional[ int ] = 0
    