"""

"""
import turtle
import time


class System:
    def __init__(self, rules, actions, axiom):
        self.rules = rules
        self.actions = actions
        self.axiom = axiom
        self.expanded = []

    def construct(self, depth):
        actions = self.axiom
        actions_new = []
        for i in range(depth):
            for action in actions:
                actions_new.extend(self.rules.get(action, [action]))
            actions = actions_new
            actions_new = []
        self.expanded = actions

    def draw(self):
        for action in self.expanded:
            self.actions[action]()


class TurtleDrawSystem(System):
    def __init__(self, *args, **kwargs):
        super().__init__(rules={
            "1": ["1", "1"],
            "0": ["1", "[", "0", "]", "0"]
        }, actions={
            "1": self.draw_segment,
            "0": self.draw_segment,
            "[": self.push_left,
            "]": self.pop_right
        }, axiom="0", **kwargs)
        self.stack = []

    def draw_segment(self):
        turtle.pd()
        turtle.forward(3)
        turtle.pu()

    def push(self):
        self.stack.append(tuple(turtle.position()) + (turtle.heading(),))

    def pop(self):
        popped_x, popped_y, popped_heading = self.stack.pop()
        turtle.setpos(popped_x, popped_y)
        turtle.seth(popped_heading)

    def push_left(self):
        self.push()
        turtle.left(20)

    def pop_right(self):
        self.pop()
        turtle.right(45)

if __name__ == "__main__":
    turtle.speed(0)
    system = TurtleDrawSystem()
    system.construct(6)
    system.draw()
    time.sleep(4)
