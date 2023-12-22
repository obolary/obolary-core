from typing import Optional
from pydantic_settings import BaseSettings

import boto3
from botocore.client import Config as BotoConfig

class Config(BaseSettings):
    
    s3_enabled : Optional[ bool ] = False
    s3_bucket : Optional[ str ] = ''
    s3_endpoint_url : Optional[ str ] = ''
    s3_access_key : Optional[ str ] = ''
    s3_secret_access_key : Optional[ str ] = ''
    s3_signature_version : Optional[ str ] = ''
    s3_region_name : Optional[ str ] = ''
    
    s3 : Optional[ object ] = None
    
    data_service_url_and_path : Optional[ str ] = ''
    
    def __init__( self, **kwargs ):
        super().__init__( **kwargs )
        
        if self.s3_enabled:
            self.s3 = boto3.client( 
                's3', 
                endpoint_url = self.s3_endpoint_url,
                aws_access_key_id = self.s3_access_key,
                aws_secret_access_key = self.s3_secret_access_key,
                config = BotoConfig( signature_version = self.s3_signature_version ),
                region_name = self.s3_region_name             
            )

config = Config()
