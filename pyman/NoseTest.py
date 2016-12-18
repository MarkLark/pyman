from . import Page, Action


class NoseTest( Page ):
    def __init__( self ):
        super( NoseTest, self ).__init__( "Testing (Python NoseTest)" )

    def init( self ):
        self.add([
            Action.Cmd( "Without Stdout", "nosetests -v tests" ),
            Action.Cmd( "With Stdout", "nosetests -vs tests" ),
            Action.Back()
        ])
