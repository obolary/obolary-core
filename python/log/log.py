from pydantic import BaseModel

import os
import sys
import inspect
from datetime import datetime

from log.config import config

class Log(BaseModel):

    level : str
    timestamp : datetime
    process : str
    function : str
    file : str
    line : int
    
    def __init__( self, level : str, offset : int = 0 ):
        process = '<cli>'
        if config.pod_name:
            process = config.pod_name
        elif sys.argv[0]:
            process = os.path.basename( sys.argv[ 0 ] )
        stack = inspect.stack()
        super().__init__(
            level = level,
            timestamp = datetime.now(),
            process = process,
            file = os.path.basename( stack[ 2 + offset ][1] ),
            line = stack[ 2 + offset ][2],
            function = stack[ 2 + offset ][3]
        )
                
    def emit( self, message : str ):
        print( f'{self.level} | {self.timestamp} | {self.process} | {self.file}:{self.line} | {self.function} | {message}')
        
def trace( message : str, offset : int = 0 ):
    if config.log_trace_enabled:
        Log( level = 'TRACE', offset = offset ).emit( message )

def debug( message : str, offset : int = 0 ):
    if config.log_debug_enabled:
        Log( level = 'DEBUG', offset = offset ).emit( message )

def info( message : str, offset : int = 0 ):
    Log( level = 'INFO', offset = offset ).emit( message )

def alarm( message : str, offset : int = 0 ):
    Log( level = 'ALARM', offset = offset ).emit( message )

def event( message : str, offset : int = 0 ):
    Log( level = 'EVENT', offset = offset ).emit( message )
    