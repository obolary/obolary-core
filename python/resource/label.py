from resource.identity import Identity

class Label(Identity):
    
    name : str
    value : str

    def __init__( self, **kwargs ):
        super().__init__( kind = 'label', **kwargs )
