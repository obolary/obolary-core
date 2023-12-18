from typing import Optional, Self

from rest.context import Context
from resource.identity import Identity
from resource.identity import Status

class Object(Identity):
    
    state : Optional[ str ] = ''
    status : Optional[ Status ] = None

    def __init__( self, **kwargs ):
        super().__init__( kind = 'object', **kwargs )

    # POST /[kind]/delete/[id]
    # POST /[kind]/delete/[id]/[path]
    def delete( self, context : Context, path : str = '' ) -> Status:
        if not path:
            return super().delete( context )
        # delete path directory, if directory, or
        # delete path file, if file
        return None
    
    # POST /[kind]/get/[id]
    # POST /[kind]/get { [filter] }
    # POST /[kind]/get/[id]/[path]
    def get( self, context : Context, path : str = '' ) -> (Self | [Self], Status):
        if not path:
            return super().get( context )
        # get path list, if directory, or 
        # get path bytes, if file
        return None, None
    
    # POST /[kind]/set/[id] { [resource] }
    # POST /[kind]/set/[id]/[path] [file]
    def set( self, context : Context, path : str = '' ) -> (Self, Status):
        if not path:
            return super().set( context )
        # set path bytes
        return None, None
