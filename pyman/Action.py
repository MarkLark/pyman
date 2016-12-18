class Action( object ):
    """Base Action class to be used by all actions"""

    def __init__( self, name ):
        self.name   = name #: The display name for this action
        self.parent = None #: The parent page this action is assigned to
        self.menu   = None #: The main page for this CLI instance

    def run( self ):
        """This method is called when the Action is executed. Overwrite it to perform your specific action"""
        return self

    def init( self ):
        """This method is called when the Action is assigned to a Page"""
        pass
