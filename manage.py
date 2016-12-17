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


menu = pyman.Main( "pyman - Manage" )
menu.add([
    Doc(),
    PyPi(),
    Test(),
    pyman.Action.Exit()
])
menu.cli()
