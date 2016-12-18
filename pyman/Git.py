from . import Page, Actions


class Git( Page ):
    def __init__( self ):
        super( Git, self ).__init__( "Git" )

    def init( self ):
        self.add([
            Actions.Cmd( "Commit", "git commit -a" ),
            CommitFile(),
            AddFile(),
            Actions.Cmd( "Push", "git push" ),
            Actions.Cmd( "History", "git log" ),
            Actions.Back()
        ])


class FileCommand( Actions.Cmd ):
    def run( self ):
        filename = raw_input( "Filename: " )
        self.cmd += " %s" % filename
        super( FileCommand, self ).run()


class CommitFile( FileCommand ):
    def __init__( self ):
        super( CommitFile, self ).__init__( "Commit File", "git commit" )


class AddFile( FileCommand ):
    def __init__( self ):
        super( AddFile, self ).__init__( "Add File", "git add" )
