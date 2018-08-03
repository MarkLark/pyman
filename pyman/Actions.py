from . import Screen
from .Action import Action
from os import system


class Exit(Action):
    """Exit the CLI"""
    def __init__(self):
        Action.__init__(self, "Exit")


class Back(Action):
    """Go back one page"""
    def __init__( self ):
        Action.__init__(self, "Back")


class Cmd(Action):
    """Run a command in the terminal"""
    def __init__(self, name, cmd=""):
        Action.__init__(self, name)
        self.cmd = cmd  # The command to run

    def run(self):
        system(self.cmd)

        if not self.menu.is_automated:
            Screen.user_input("\nFinished....")
