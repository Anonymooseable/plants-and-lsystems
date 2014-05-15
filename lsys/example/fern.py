import lsys.core as core
import random


class FernDrawer:
    def __init__(self, renderer, depth=7):
        branch = ["push", "muchsmaller", "turn", "fw", "branch", "pop"]
        root_result = lambda context: (branch + ["flip", "fw", "smaller"] + branch + ["flip", "fw", "smaller"]) * 3 + ["root"]
        branch_result = lambda context: (branch + ["flip", "fw", "smaller"] + branch + ["flip", "fw", "smaller"]) * 3 + ["smaller", "branch"]
        self.system = core.System(rules={
            "root": root_result,
            "branch": branch_result
        }, axiom=["fw", "root"])

        self.actions = {
            "fw": self.fw,
            "push": self.push,
            "pop": self.pop,
            "turn": self.turn,
            "branch": self.branch,
            "smaller": self.smaller,
            "muchsmaller": self.muchsmaller,
            "flip": self.flip,
        }

        self.renderer = renderer
        self.depth = depth
        self.length_stack = [10]
        self.flipped = False

    def fw(self):
        self.renderer.draw_segment(self.length_stack[-1])
        self.renderer.turn((-1 if self.flipped else 1) * random.gauss(2, 2))

    def branch(self):
        self.renderer.draw_segment(self.length_stack[-1] * 4)

    def smaller(self):
        self.length_stack[-1] *= 0.9

    def muchsmaller(self):
        self.length_stack[-1] *= 0.4

    def turn(self):
        self.renderer.turn(80 if self.flipped else -80)

    def push(self):
        self.renderer.push()
        self.length_stack.append(self.length_stack[-1])

    def pop(self):
        self.renderer.pop()
        self.length_stack.pop()

    def flip(self):
        self.flipped = not self.flipped

    def draw(self):
        actions = self.system.construct(depth=self.depth)
        for action in actions:
            self.actions.get(action, lambda: None)()
        self.renderer.display()


def main():
    mode = "opengl"
    #mode = "turtle"

    if mode == "opengl":
        from lsys.render.gl_renderer import GLRenderer
        r = GLRenderer(
            scale=4,
            size=(800, 800),
            fg=(0.0, 0.4, 0.0, 1.0),
            bg=(1.0, 1.0, 1.0, 1.0)
        )
    elif mode == "turtle":
        from lsys.render.turtle_renderer import TurtleRenderer
        r = TurtleRenderer()
    s = FernDrawer(depth=4, renderer=r)
    s.draw()

if __name__ == "__main__":
    main()
