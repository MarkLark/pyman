#!/usr/bin/python
import pyman


class PyPi( pyman.Page ):
    def __init__( self ):
        super( PyPi, self ).__init__( "PyPi" )

    def init( self ):
        self.add([
            pyman.Action.Cmd( "Package Source", "python setup.py sdist" ),
            pyman.Action.Cmd( "Package Wheel", "python setup.py bdist_wheel" ),
            pyman.Action.Cmd( "Upload", "twine upload dist/*" ),
            pyman.Action.Back()
        ])


class Doc( pyman.Page ):
    def __init__( self ):
        super( Doc, self ).__init__( "Documentation" )

    def init( self ):
        self.add([
            pyman.Action.Cmd( "Generate HTML", "cd doc; make html; cd .." ),
            pyman.Action.Back()
        ])


class Test( pyman.Page ):
    def __init__( self ):
        super( Test, self ).__init__( "Testing" )

    def init( self ):
        self.add([
            pyman.Action.Cmd( "Without Stdout", "nosetests -v tests" ),
            pyman.Action.Cmd( "With Stdout", "nosetests -vs tests" ),
            pyman.Action.Back()
        ])


class Git( pyman.Page ):
    def __init__( self ):
        super( Git, self ).__init__( "GitHub" )

    def init( self ):
        self.add([
            pyman.Action.Cmd( "Commit", "git commit" ),
            GitCommitFile(),
            pyman.Action.Cmd( "Push", "git push" ),
            pyman.Action.Back()
        ])


class GitCommitFile( pyman.Action.Cmd ):
    def __init__( self ):
        super( GitCommitFile, self ).__init__( "Commit File" )

    def run( self ):
        filename = raw_input( "Filename: " )
        self.cmd = "git commit %s" % filename
        super( GitCommitFile, self ).run()



menu = pyman.Main( "pyman - Manage" )
menu.add([
    Doc(),
    PyPi(),
    Test(),
    Git(),
    pyman.Action.Exit()
])
menu.cli()
