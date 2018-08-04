from . import Page, Actions


class Webpack(Page):
    def __init__(self, client_dir="", run_cmd="serve", build_cmd="build"):
        Page.__init__(self, "Webpack")
        self.client_dir = client_dir
        self.run_cmd = run_cmd
        self.build_cmd = build_cmd

    def init(self):
        self.add([
            Actions.Cmd("Dev Server", "cd %s && npm run %s" % (self.client_dir, self.run_cmd)),
            Actions.Cmd("Build", "cd %s && npm run %s" % (self.client_dir, self.build_cmd)),
            Actions.Back()
        ])
