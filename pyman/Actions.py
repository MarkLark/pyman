from . import Action


class Exit( Action ):
    def __init__( self ):
        super( Exit, self ).__init__( "Exit" )

    def run( self ):
        return self


class Back( Action ):
    def __init__( self ):
        super( Back, self ).__init__( "Back" )


class Cmd( Action ):
    def __init__( self, name, cmd = "" ):
        super( Cmd, self ).__init__( name )
        self.cmd = cmd

    def run( self ):
        from os import system
        system( self.cmd )

        if not self.menu.is_automated: raw_input( "\nFinished...." )
