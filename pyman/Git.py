from . import Page, Action


class Git( Page ):
    def __init__( self ):
        super( Git, self ).__init__( "Git" )

    def init( self ):
        self.add([
            Action.Cmd( "Commit", "git commit" ),
            CommitFile(),
            AddFile(),
            Action.Cmd( "Push", "git push" ),
            Action.Cmd( "History", "git log" ),
            Action.Back()
        ])


class FileCommand( Action.Cmd ):
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
