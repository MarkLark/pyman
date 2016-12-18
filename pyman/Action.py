class Action( object ):
    def __init__( self, name ):
        self.name   = name
        self.parent = None
        self.menu   = None

    def run( self ):
        return self

    def init( self ):
        pass
