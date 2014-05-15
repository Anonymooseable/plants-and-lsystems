#Ceci est le fichier qui contient le L-Systeme spécifique pour l'arbre.

import lsys.core as core
import random
import math


class TreeDrawer:
    def __init__(self, renderer, depth=8):
        self.system = core.System(rules={
            "branch": core.StochasticRule(
                    (["fw", "push", "smaller", "branch","pop"], 2),
                    (["fw", "push", "left", "smaller", "branch","pop",
                      "push", "right", "smaller", "branch", "pop"], 3),
                    (["fw", "push", "left", "smaller", "branch","pop",
                      "push", "smaller", "branch","pop",
                      "push", "right", "smaller", "branch", "pop"], 2),
                    ),
            "fw": lambda context: ["fw","fw"]
        }, axiom=["branch"])

        self.actions={
            "fw": self.fw,
            "push": self.push,
            "pop": self.pop,
            "left": self.left,
            "right": self.right,

        self.renderer = renderer
        self.depth = depth

    def clamp(self,lower, upper, val):
        return lower if lower>val else (upper if upper < val else val)

    def fw(self):
        self.renderer.draw_segment(20)

    def left(self):
        self.renderer.turn(self.clamp(10,50,random.gauss(30,18)))

    def right(self):
        self.renderer.turn(self.clamp(-10,-50,random.gauss(-30,18)))

    def push(self):
        self.renderer.push()

    def pop(self):
        self.renderer.pop()
        self.renderer.turn(random.gauss(0,5))
        #cela fait varier l'angle dans une branche

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
            scale=0.1,
            size=(800, 800),
            fg=(0.0, 0.4, 0.0, 1.0),
            bg=(1.0, 1.0, 1.0, 1.0)
        )
    elif mode == "turtle":
        from lsys.render.turtle_renderer import TurtleRenderer
        r = TurtleRenderer()
    s = TreeDrawer(depth=8, renderer=r)
    s.draw()

if __name__ == "__main__":
    main()
