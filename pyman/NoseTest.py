from . import Page, Actions


class NoseTest(Page):
    def __init__(self, test_dir="tests"):
        Page.__init__(self, "Testing (Python NoseTest)")
        self.test_dir = test_dir

    def init(self):
        self.add([
            Actions.Cmd("Without Stdout", "nosetests -v %s" % self.test_dir),
            Actions.Cmd("With Stdout", "nosetests -vs %s" % self.test_dir),
            Actions.Back()
        ])
