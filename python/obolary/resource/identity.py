from typing import Optional, List, Self
from pydantic import BaseModel

import base64
import json
import uuid
from datetime import datetime

from obolary.rest.context import Context

# forward references
if globals().get( 'Status' ) is None:
    class Identity(BaseModel): pass
    from obolary.resource.status import Status

# id format definition
class Id(BaseModel):
    
    K : str
    E : Optional[ str ] = str( uuid.uuid4() )

    def string( self ) -> str:
        ascii = json.dumps( self ).encode( 'ascii' )
        encoded = base64.standard_b64encode( ascii )
        return encoded.decode( 'ascii' )
    
    @staticmethod
    def decode( encoded : str ) -> Self:
        ascii = encoded.encode( 'ascii' )
        decoded = base64.standard_b64decode( ascii )
        standard = decoded.decode( 'ascii' )
        return Id( json.loads( standard ) )

# identity
class Identity(BaseModel):
    
    kind : str
    id : Optional[str] = ''
    owner_id : Optional[str] = ''
    label_ids : Optional[ List[str] ] = []
    created : Optional[ datetime ] = datetime.now()
    updated : Optional[ datetime ] = datetime.now()
    documentation : Optional[ str ] = ''

    @staticmethod
    # POST /[kind]/create
    def create( context : Context ) -> (Self, Status):
        return None, None
    
    # POST /[kind]/delete/[id]
    def delete( self, context : Context ) -> Status:
        return None
    
    # POST /[kind]/get/[id]
    # POST /[kind]/get { [filter] }
    def get( self, context : Context ) -> (Self | list, Status):
        return None, None
    
    # POST /[kind]/set/[id] { [resource] }
    def set( self, context : Context ) -> (Self, Status):
        return None, None
    