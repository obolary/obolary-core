from typing import Optional, Self

from obolary.resource.identity import Identity
from obolary.rest.context import Context
from obolary.resource.status import Status

class Target(Identity):
    
    target : str
    on_ok : Optional[ str ] = ''
    on_error : Optional[ str ] = ''
    
    def __init__( self, **kwargs ):
        super().__init__( kind = 'target', **kwargs )
 
    @staticmethod
    def create( context : Context ) -> (Self, Status):
        return Target().create(context)
       