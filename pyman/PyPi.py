from . import Page, Actions


class PyPi( Page ):
    def __init__( self ):
        super( PyPi, self ).__init__( "PyPi" )

    def init( self ):
        self.add([
            Actions.Cmd( "Package Source", "python setup.py sdist" ),
            Actions.Cmd( "Package Wheel", "python setup.py bdist_wheel" ),
            Actions.Cmd( "Upload", "twine upload dist/*" ),
            Actions.Cmd( "Clean Dist", "rm -Rf dist" ),
            Actions.Back()
        ])
