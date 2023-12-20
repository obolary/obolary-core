from typing import Optional
from pydantic_settings import BaseSettings
import os

import boto3
from botocore.client import Config as BotoConfig

s3 = boto3.resource('s3',
                    endpoint_url='https://<XXXXXX>.stackhero-network.com',
                    aws_access_key_id='YOUR_ACCESS_KEY',
                    aws_secret_access_key='YOUR_SECRET_KEY',
                    config=BotoConfig(signature_version='s3v4'),
                    region_name='us-east-1')

class Config(BaseSettings):
    
    resource_host : Optional[ str ] = 'http://127.0.0.1:8080'
    
    s3_enabled : Optional[ bool ] = False
    s3_endpoint_url : Optional[ str ] = ''
    s3_access_key : Optional[ str ] = ''
    s3_secret_access_key : Optional[ str ] = ''
    s3_signature_version : Optional[ str ] = 's3v4'
    s3_region_name : Optional[ str ] = 'us-east-1'
    
    s3 : Optional[ object ] = None
    
    def __init__( self, **kwargs ):
        super().__init__( **kwargs )
        
        if self.s3_enabled:
            self.s3 = boto3.resource( 
                's3', 
                endpoint_url = self.s3_endpoint_url,
                aws_access_key_id = self.s3_access_key,
                aws_secret_access_key = self.s3_secret_access_key,
                config = BotoConfig( signature_version = self.s3_signature_version ),
                region_name = self.s3_region_name             
            )
        
config = Config()
