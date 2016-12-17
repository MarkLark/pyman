from . import BaseTest
import pyman


class TestMainMenu( BaseTest ):
    def test_01_main_menu( self ):
        self.cli.add( [
            pyman.Action.Exit()
        ] )

        self.cli.cli( "5q" )
