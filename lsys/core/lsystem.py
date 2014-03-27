"""

"""


class System:
    def __init__(self, rules, actions, axiom, renderer):
        self.rules = rules
        self.actions = actions
        self.axiom = axiom
        self.expanded = []
        self.renderer = renderer

    def construct(self, depth, debug=False):
        actions = self.axiom
        for i in range(depth):
            actions_new = []
            if debug:
                print("Iteration", i, ":", actions)
            for action in actions:
                actions_new.extend(self.rules.get(action, [action]))
            actions = actions_new
            actions_new = []

        if debug:
            print("Result:", actions)
        self.expanded = actions

    def render(self):
        for action in self.expanded:
            self.actions.get(action, lambda: None)()
        self.renderer.display()
