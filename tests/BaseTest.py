import pyman


class BaseTest( object ):
    def setup( self ):
        self.cli = pyman.Main( "PyMan - Test Interface" )
