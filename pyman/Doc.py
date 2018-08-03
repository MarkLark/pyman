from . import Page, Actions


class Doc(Page):
    def __init__(self):
        Page.__init__(self, "Documentation")

    def init(self):
        self.add([
            Actions.Cmd("Generate Multi-Page HTML", "cd docs; make html; cd .."),
            Actions.Cmd("Generate Single-Page HTML", "cd docs; make singlehtml; cd .."),
            Actions.Cmd("Clean", "cd docs; make clean; cd .."),
            Actions.Back()
        ])
