from setuptools import setup, find_namespace_packages

setup(
    name = 'obolary-core',
    author = 'Obolary, Inc',
    author_email = 'contact@obolary.com',
    version = '1.1.0',
    description = 'A python library for basic resources',
    url = 'https://github.com/obolary/obolary-core',
    install_requires = [ 
        'pydantic', 
        'pydantic-settings' ,
        'boto3'
    ],
    packages = find_namespace_packages( where='python/', include=[ 'obolary.log', 'obolary.resource', 'obolary.rest' ] ),
    package_dir = { '': 'python' },
    python_requires = '>=3.11'
)
