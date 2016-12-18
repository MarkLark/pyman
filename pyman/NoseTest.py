from . import Page, Actions


class NoseTest( Page ):
    def __init__( self ):
        super( NoseTest, self ).__init__( "Testing (Python NoseTest)" )

    def init( self ):
        self.add([
            Actions.Cmd( "Without Stdout", "nosetests -v tests" ),
            Actions.Cmd( "With Stdout", "nosetests -vs tests" ),
            Actions.Back()
        ])
