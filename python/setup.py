from setuptools import setup, find_packages

setup(
    name='obolary-core',
    author='Obolary, Inc',
    author_email='contact@obolary.com',
    version='1.1.0',
    description='A python library for basic resources',
    url='https://github.com/obolary/obolary-core',
    install_requires=[ 'pydantic', 'pydantic-settings' ],
    packages=find_packages( include=[ 'log', 'resource', 'rest' ] ),
    python_requires='>=3.11'
)
