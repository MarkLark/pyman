import Screen
from . import Page


class Main( Page ):
    def __init__( self, title, chars = None ):
        self.title         = title
        self.chars         = chars
        self.current       = [ self ]
        self.current_title = ""
        self.width, self.height = Screen.size()
        self.is_automated  = False

        if self.chars  is None: self.chars = [ "=", "-", ") " ]

        super( Main, self ).__init__( "Main Menu", menu = self, parent = self )

    def header( self ):
        Screen.clear()
        self.width, self.height = Screen.size()
        print self.chars[0] * self.width

        spaces = (self.width - len(self.title)) / 2
        print "%s%s" % (" " * spaces, self.title)

        print self.chars[0] * self.width

        title = ""
        if len( self.current ) == 1: title = self.current[0].name
        else:
            for p in self.current:
                if p.name == "Main Menu": continue
                elif title != "": title += "."
                title += p.name.lower().replace( " ", "_" )

        print
        print title
        print self.chars[1] * ( self.width / 4 )
        self.current_title = title

    def cli( self, commands = None ):
        from . import Page, Action

        # If a list of commands is provided as a string, convert them to an array
        if commands is not None:
            self.is_automated = True
            if isinstance( commands, basestring ): commands = list( commands )
        else:
            self.is_automated = False

        while True:
            self.header()
            self.current[-1].choices()
            print self.chars[1] * (self.width / 4)

            try:
                if commands is not None: choice = commands.pop()
                else                   : choice = raw_input( "\nChoice: " )

                if choice.lower() == "q": break
                rtn = self.current[-1].run( int( choice ) )

                if   isinstance( rtn, Page        ): self.current.append( rtn )
                elif isinstance( rtn, Action.Back ): self.current.pop()
                elif isinstance( rtn, Action.Exit ): break
            except ValueError:
                print "Incorrect value, try again...."
                if commands is None:  raw_input( "" )
            except KeyboardInterrupt:
                print
                break
