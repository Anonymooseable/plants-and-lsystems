"""

"""


class System:
    def __init__(self, rules, actions, axiom, renderer):
        self.rules = rules
        self.actions = actions
        self.axiom = axiom
        self.expanded = []
        self.renderer = renderer

    def construct(self, depth):
        actions = self.axiom
        actions_new = []
        for i in range(depth):
            for action in actions:
                actions_new.extend(self.rules.get(action, [action]))
            actions = actions_new
            actions_new = []
        self.expanded = actions

    def render(self):
        for action in self.expanded:
            self.actions[action]()
        self.renderer.display()
