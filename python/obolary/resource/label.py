from typing import Self

from obolary.resource.identity import Identity
from obolary.rest.context import Context
from obolary.resource.status import Status

class Label(Identity):
    
    name : str
    value : str

    def __init__( self, **kwargs ):
        super().__init__( kind = 'label', **kwargs )

    @staticmethod
    def create( context : Context, name : str, value : str ) -> (Self, Status):
        return Label( name, value ).create(context)

    # POST /label/attach/[id]/[member]    
    def attach( context : Context, member : str ):
        pass
    
    # POST /label/attach/[id]/[member]    
    def detach( context : Context, member : str ):
        pass
