from typing import Optional

from obolary.resource.identity import Identity

class Target(Identity):
    
    target : str
    on_ok : Optional[ str ] = ''
    on_error : Optional[ str ] = ''
    
    def __init__( self, **kwargs ):
        super().__init__( kind = 'target', **kwargs )
        