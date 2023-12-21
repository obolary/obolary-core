from typing import Optional, List, Self
from pydantic import BaseModel

import requests
import base64
import json
import uuid
from datetime import datetime

from obolary.rest.context import Context
# NOTE, we're not use base_path from rest.config
# from obolary.rest.config import config as rest

from obolary.resource.filter import Filter
from obolary.resource.status import StatusBadGateway, StatusBadRequest
from obolary.resource.config import config

# forward references
if globals().get( 'Status' ) is None:
    class Identity(BaseModel): pass
    from obolary.resource.status import Status

# id format definition
class Id(BaseModel):
    
    K : str
    E : str

    @staticmethod
    def new( kind : str ):
        return Id( K = kind, E = str( uuid.uuid4() ) )
        
    def string( self ) -> str:
        ascii = json.dumps( self.model_dump() ).encode( 'ascii' )
        encoded = base64.standard_b64encode( ascii )
        return encoded.decode( 'ascii' )
    
    @staticmethod
    def decode( encoded : str ) -> Self:
        ascii = encoded.encode( 'ascii' )
        decoded = base64.standard_b64decode( ascii )
        standard = decoded.decode( 'ascii' )
        dictionary = json.loads( standard )
        return Id( **dictionary )

# identity
class Identity(BaseModel):
    
    kind : str
    id : str
    owner_id : Optional[str] = ''
    label_ids : Optional[ List[str] ] = []
    created : Optional[ datetime ] = datetime.now()
    updated : Optional[ datetime ] = datetime.now()
    documentation : Optional[ str ] = ''
    
    def __init__( self, kind : str, **kwargs ):
        id = Id.new( kind )
        super().__init__( kind = kind, id = id, **kwargs )

    # POST /[kind]/create
    def create( self, context : Context ) -> (Self, Status):
        if context is None:
            return None, StatusBadRequest.clone( 'missing required context' )
        response = requests.post(
            f'{config.data_service_url_and_path}/{self.kind}/create',
            headers={
                'Authorization': f'Bearer {context.access_token}',
                'Content-Type': 'application/json',
            },
            json=self,
            verify=False,
        )
        if response.status_code == 200:
            return response.json(), None
        else:
            error = response.json()
            return error, StatusBadGateway.clone( f'set failed' )
                 
    # POST /[kind]/delete/[id]
    def delete( self, context : Context, filter : Filter = None ) -> Status:
        if context is None:
            return None, StatusBadRequest.clone( 'missing required context' )
        response = requests.post(
            f'{config.data_service_url_and_path}/{self.kind}/delete/{self.id}',
            headers={
                'Authorization': f'Bearer {context.access_token}',
                'Content-Type': 'application/json',
            },
            json=filter,
            verify=False,
        )
        if response.status_code == 200:
            return response.json(), None
        else:
            return StatusBadGateway.clone( f'delete failed' )
    
    # POST /[kind]/get/[id]
    # POST /[kind]/get { [filter] }
    def get( self, context : Context, filter : Filter = None ) -> (Self | list, Status):
        if context is None:
            return None, StatusBadRequest.clone( 'missing required context' )
        if filter is not None:
            response = requests.post(
                f'{config.data_service_url_and_path}/{self.kind}/query',
                headers={
                    'Authorization': f'Bearer {context.access_token}',
                    'Content-Type': 'application/json',
                },
                json=filter,
                verify=False,
            )
            if response.status_code == 200:
                return response.json(), None
            else:
                error = response.json()
                return error, StatusBadGateway.clone( f'get failed' )
        else:
            response = requests.post(
                f'{config.data_service_url_and_path}/{self.kind}/set/{self.id}',
                headers={
                    'Authorization': f'Bearer {context.access_token}',
                    'Content-Type': 'application/json',
                },
                json=self,
                verify=False,
            )
            if response.status_code == 200:
                return response.json(), None
            else:
                error = response.json()
                return error, StatusBadGateway.clone( f'get failed' )
    
    # POST /[kind]/set/[id] { [resource] }
    def set( self, context : Context ) -> (Self, Status):
        if context is None:
            return None, StatusBadRequest.clone( 'missing required context' )
        response = requests.post(
            f'{config.data_service_url_and_path}/{self.kind}/set/{self.id}',
            headers={
                'Authorization': f'Bearer {context.access_token}',
                'Content-Type': 'application/json',
            },
            json=self,
            verify=False,
        )
        if response.status_code == 200:
            return response.json(), None
        else:
            error = response.json()
            return error, StatusBadGateway.clone( f'set failed' )
