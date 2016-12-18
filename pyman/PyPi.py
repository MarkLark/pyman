from . import Page, Action


class PyPi( Page ):
    def __init__( self ):
        super( PyPi, self ).__init__( "PyPi" )

    def init( self ):
        self.add([
            Action.Cmd( "Package Source", "python setup.py sdist" ),
            Action.Cmd( "Package Wheel", "python setup.py bdist_wheel" ),
            Action.Cmd( "Upload", "twine upload dist/*" ),
            Action.Back()
        ])
