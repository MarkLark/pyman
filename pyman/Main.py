from . import Page, Screen, Actions


class Main(Page):
    def __init__(self, title, actions=None, chars=None):
        self.title = title
        self.chars = chars
        self.current = [self]
        self.current_title = ""
        self.is_automated = False

        self.width, self.height = Screen.size()

        if self.chars  is None:
            self.chars = ["=", "-", ") "]

        Page.__init__(self, "Main Menu", menu=self, parent=self)

        if actions is not None:
            self.add(actions)

    def header(self):
        Screen.clear()
        self.width, self.height = Screen.size()
        Screen.write("%s\n" % (self.chars[0] * self.width))

        spaces = int((self.width - len(self.title)) / 2)
        Screen.write("%s%s\n" % (" " * spaces, self.title))
        Screen.write("%s\n" % (self.chars[0] * self.width))

        title = ""
        if len(self.current) == 1:
            title = self.current[0].name
        else:
            for p in self.current:
                if p.name == "Main Menu":
                    continue
                elif title != "":
                    title += "."

                title += p.name.lower().replace(" ", "_")

        Screen.write("\n%s\n%s\n" % (title, self.chars[1] * int( self.width / 4 )))
        self.current_title = title

    def cli(self, commands=None):
        # If a list of commands is provided as a string, convert them to an array
        if commands is not None:
            self.is_automated = True
            try:
                if isinstance(commands, basestring):
                    commands = list(commands)
            except NameError:
                if isinstance(commands, str):
                    commands = list(commands)
        else:
            self.is_automated = False

        while True:
            self.header()
            self.current[-1].choices()
            Screen.write("%s\n" % (self.chars[1] * int(self.width / 4)))

            try:
                if commands is not None:
                    choice = commands.pop()
                else:
                    choice = Screen.user_input("\nChoice: ")

                if choice.lower() == "q":
                    break

                rtn = self.current[-1].run(int(choice))

                if isinstance(rtn, Page):
                    self.current.append(rtn)
                elif isinstance(rtn, Actions.Back):
                    self.current.pop()
                elif isinstance(rtn, Actions.Exit):
                    break
            except ValueError:
                Screen.write("Incorrect value, try again....\n")
                if commands is None:
                    Screen.user_input()
            except KeyboardInterrupt:
                Screen.write("\n")
                break
