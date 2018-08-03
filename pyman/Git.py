from . import Page, Actions, Screen


class Git(Page):
    def __init__( self ):
        Page.__init__(self, "Git")

    def init( self ):
        self.add([
            Actions.Cmd("Commit", "git commit -a"),
            CommitFile(),
            AddFile(),
            Actions.Cmd("Push", "git push"),
            Actions.Cmd("History", "git log"),
            Actions.Back()
        ])


class FileCommand(Actions.Cmd):
    def run(self):
        filename = Screen.user_input("Filename: ")
        self.cmd += " %s" % filename
        Actions.Cmd.run(self)


class CommitFile(FileCommand):
    def __init__(self):
        FileCommand.__init__(self, "Commit File", "git commit")


class AddFile(FileCommand):
    def __init__(self):
        FileCommand.__init__(self, "Add File", "gid add")
