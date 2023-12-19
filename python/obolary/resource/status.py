from typing import Optional, Self
import http

import obolary.log as log

# forward references
if globals().get( 'Identity' ) is None:
    from obolary.resource.identity import Identity

StatusCodeToHttpStatus = {
   'internal_server': http.HTTPStatus.INTERNAL_SERVER_ERROR,
   'bad_request': http.HTTPStatus.BAD_REQUEST,
   'bad_gateway': http.HTTPStatus.BAD_GATEWAY,
   'not_implemented': http.HTTPStatus.NOT_IMPLEMENTED,
   'not_found': http.HTTPStatus.NOT_FOUND,
   'forbidden': http.HTTPStatus.FORBIDDEN
}

class Status(Identity):
    
    code : str
    description : Optional[ str ] = ''
    uri : Optional[ str ] = ''

    def __init__( self, **kwargs ):
        super().__init__( kind = 'status', **kwargs )

    def status( self ) -> int:
        if self.code in StatusCodeToHttpStatus:
            return StatusCodeToHttpStatus[ self.code ]
        return http.HTTPStatus.BAD_REQUEST
    
    def clone( self, message : str ) -> Self:
        return Status( code = self.code, description = message, uri = self.uri )
    
    def trace( self ) -> Self:
        log.trace( self.description, offset = 1 )
        return self
        
    def debug( self ) -> Self:
        log.debug( self.description, offset = 1 )
        return self

    def info( self ) -> Self:
        log.info( self.description, offset = 1 )
        return self

    def alarm( self ) -> Self:
        log.alarm( self.description, offset = 1 )
        return self

    def event( self ) -> Self:
        log.event( self.description, offset = 1 )
        return self
            
StatusOk = Status(code = 'ok', description = 'OK')
StatusInternalServer = Status(code = 'internal_server', description = 'internal server error')
StatusBadRequest = Status(code = 'bad_request', description = 'bad request error')
StatusBadGateway = Status(code = 'bad_gateway', description = 'bad gateway error')
StatusNotImplemented = Status(code = 'not_implemented', description = 'endpoint not implemented')
StatusNotFound = Status(code = 'not_found', description = 'resource not found')
StatusForbidden = Status(code = 'forbidden', description = 'requested endpoint or resource access forbidden')
