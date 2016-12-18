from .Action import Action


class Exit( Action ):
    """Exit the CLI"""
    def __init__( self ):
        super( Exit, self ).__init__( "Exit" )


class Back( Action ):
    """Go back one page"""
    def __init__( self ):
        super( Back, self ).__init__( "Back" )


class Cmd( Action ):
    """Run a command in the terminal"""
    def __init__( self, name, cmd = "" ):
        super( Cmd, self ).__init__( name )
        self.cmd = cmd #: The command to run

    def run( self ):
        from os import system
        system( self.cmd )

        if not self.menu.is_automated: raw_input( "\nFinished...." )
