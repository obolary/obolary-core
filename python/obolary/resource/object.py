from typing import Optional, Self
import io
import os
from botocore.exceptions import ClientError

from obolary.rest.context import Context
from obolary.resource.identity import Identity
from obolary.resource.filter import Filter
from obolary.resource.status import Status, StatusBadRequest
from obolary.resource.config import config

import obolary.log as log

class Object(Identity):
    
    state : Optional[ str ] = ''
    status : Optional[ Status ] = None

    def __init__( self, **kwargs ):
        super().__init__( kind = 'object', **kwargs )

    @staticmethod
    def create( context : Context ) -> (Self, Status):
        if context is None:
            return None, StatusBadRequest.clone( 'missing required context' )        
        return Object().create(context)

    # TODO - POST /[kind]/delete/[id], this should delete the lake object
    # POST /object/delete/[id]/[path]
    # TODO - POST /[kind]/delete { [filter] }, this should delete the lake object
    def delete( self, context : Context, path : str = '' ) -> Status:
        if context is None:
            return None, StatusBadRequest.clone( 'missing required context' )        
        if not path:
            return super().delete( context )
        # TODO, this belongs in the resource manager, placed here for prototype
        if not config.s3_enabled:
            return StatusBadRequest.clone('lake not enabled').alarm()
        # delete path directory, if directory, or
        # delete path file, if file
        try:
            full = f'{self.id}/{path}'
            response = config.s3.delete_object( Bucket=config.s3_bucket, Key=full )
            log.debug( response )
        except ClientError as e:
            log.alarm( f'delete failed due to error, {e}' )
        return None
    
    # POST /[kind]/get/[id]
    # POST /object/get/[id]/[path]
    # TODO - POST /[kind]/get { [filter] }
    def get( self, context : Context, path : str = '' ) -> (Self | list, Status):
        if context is None:
            return None, StatusBadRequest.clone( 'missing required context' )        
        if not path:
            return super().get( context, filter )
        # TODO, this belongs in the resource manager, placed here for prototype
        if not config.s3_enabled:
            return StatusBadRequest.clone('lake not enabled').alarm()
        # get path list, if directory, or 
        # get path bytes, if file
        output = io.BytesIO()
        try:
            full = f'{self.id}/{path}'
            response = config.s3.download_fileobj( Bucket=config.s3_bucket, Key=full, Fileobj = output  )
            log.debug( response )
            #log.debug( str(output.getvalue()) )
        except ClientError as e:
            log.alarm( f'get failed due to error, {e}' )
        return output, None
    
    # POST /[kind]/set/[id] { [resource] }
    # POST /[kind]/set/[id]/[path] [file]
    def set( self, context : Context, path : str = '', content : io.BytesIO = None ) -> (Self, Status):
        if context is None:
            return None, StatusBadRequest.clone( 'missing required context' )        
        if not path:
            return super().set( context )
        # TODO, this belongs in the resource manager, placed here for prototype
        if not config.s3_enabled:
            return StatusBadRequest.clone('lake not enabled').alarm()
        # set path bytes
        try:
            full = f'{self.id}/{path}'
            response = config.s3.upload_fileobj( content, Bucket=config.s3_bucket, Key=full )
            log.debug( response )
        except ClientError as e:
            log.alarm( f'set failed due to error, {e}' )
        return None, None

    # POST /[kind]/list/[id]
    # {'ResponseMetadata': 
    #   {
    #       'HTTPStatusCode': 200, 
    #       'HTTPHeaders': {
    #           'date': 'Tue, 26 Dec 2023 17: 16: 15 GMT', 
    #           'content-type': 'application/xml', 
    #           'content-length': '873', 
    #           'connection': 'keep-alive', 
    #           'vary': 'Accept-Encoding', 
    #           'server': 'cloudflare', 
    #           'cf-ray': '83baf8752fe07279-EWR'
    #       }, 
    #       'RetryAttempts': 0
    #   }, 
    #   'IsTruncated': False, 
    #   'Marker': '', 
    #   'Contents': [
    #       {
    #           'Key': 'eyJLIjogIm9iamVjdCIsICJFIjogIjZhZWZlYjQ1LTBhNTgtNDExOS04NzA5LWZhMWU1NTEwMDQwZiJ9/boo.txt', 
    #           'LastModified': datetime.datetime(2023, 12,26,17,14,43,842000, tzinfo=tzutc()), 
    #           'ETag': '"5d41402abc4b2a76b9719d911017c592"', 
    #           'Size': 5, 
    #           'StorageClass': 'STANDARD', 
    #           'Owner': {'DisplayName': '0c323972e3858e19e37a4a4b4f84d6c2', 'ID': '0c323972e3858e19e37a4a4b4f84d6c2' }
    #       }
    #   ], 
    #   'Name': 'ensi-ai-zi', 
    #   'Prefix': 'eyJLIjogIm9iamVjdCIsICJFIjogIjZhZWZlYjQ1LTBhNTgtNDExOS04NzA5LWZhMWU1NTEwMDQwZiJ9/', 
    #   'Delimiter': '/', 
    #   'MaxKeys': 1000, 
    #   'CommonPrefixes': [
    #         {
    #           'Prefix': 'eyJLIjogIm9iamVjdCIsICJFIjogIjZhZWZlYjQ1LTBhNTgtNDExOS04NzA5LWZhMWU1NTEwMDQwZiJ9/sally/'
    #         }
    #     ]
    # }
    def list( self, context : Context, path : str = '') -> ([str], Status):
        if context is None:
            return None, StatusBadRequest.clone( 'missing required context' )
        # TODO, this belongs in the resource manager, placed here for prototype
        if not config.s3_enabled:
            return None, StatusBadRequest.clone('lake not enabled').alarm()
        # set path bytes
        files = []
        try:
            full = f'{self.id}/{path}'
            response = config.s3.list_objects( Bucket=config.s3_bucket, Prefix=full, Delimiter='/' )
            if 'Contents' in response:
                contents = response[ 'Contents' ]
                for content in contents:
                    if 'Key' in content:
                        key = content[ 'Key' ]
                        file = os.path.basename( key )
                        files.append( file )
            log.debug( response )
        except ClientError as e:
            log.alarm( f'list failed due to error, {e}' )
        return files, None
        