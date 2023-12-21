from typing import Optional, List, Self
from pydantic import BaseModel, Field

from datetime import datetime

class Filter(BaseModel):
    
    condition : Optional[ str ] = Field( default='', alias='$condition' )
    limit_number : Optional[ int ] = Field( default=100, alias='$limit_number' )
    limit_on : Optional[ str ] = Field( default='created', alias='$limit_on' )
    limit_after_inclusive : Optional[ datetime ] = Field( default=None, alias='$limit_after_inclusive' )
    limit_before : Optional[ datetime ] = Field( default=None, alias='$limit_before' )
    page : Optional[ int ] = Field( default=0, alias='$page' )
    