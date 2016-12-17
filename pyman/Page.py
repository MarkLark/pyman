

class Page( object ):
    def __init__( self, name, parent = None, menu = None ):
        self.name    = name
        self.parent  = parent
        self.menu    = menu
        self.actions = []

    def init( self ):
        pass

    def choices( self ):
        i = 1
        for a in self.actions:
            print "%d%s%s" % ( i, self.menu.chars[2], a.name )
            i += 1

    def add( self, actions ):
        for a in actions:
            a.parent = self
            a.menu   = self.menu
            a.init()
            self.actions.append( a )

    def add_action( self, action ):
        action.parent = self
        action.menu   = self.menu
        action.init()
        self.actions.append( action )

    def run( self, index ):
        if index <= 0 or index > len( self.actions ):
            raw_input( "Value out of range, try again...." )
            return

        action = self.actions[ index - 1 ]

        self.menu.current.append( action )
        self.menu.header()
        self.menu.current.pop()

        if isinstance( action, Page ): return action
        return action.run()
