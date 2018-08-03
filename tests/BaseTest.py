import pyman


class BaseTest:
    def setup( self ):
        self.cli = pyman.Main("PyMan - Test Interface")
