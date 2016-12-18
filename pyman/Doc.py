from . import Page, Actions


class Doc( Page ):
    def __init__( self ):
        super( Doc, self ).__init__( "Documentation" )

    def init( self ):
        self.add([
            Actions.Cmd( "Generate Multi-Page HTML", "cd docs; make html; cd .." ),
            Actions.Cmd( "Generate Single-Page HTML", "cd docs; make singlehtml; cd .." ),
            Actions.Cmd( "Clean", "cd docs; make clean; cd .." ),
            Actions.Back()
        ])
