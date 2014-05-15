#Ceci est le fichier qui contient le L-Systeme spécifique pour l'arbre.

import lsys.core as core
import random
import math


class TreeSystem(core.System):
    def __init__(self, *args, **kwargs):
        super().__init__(rules={
            "branch": core.StochasticRule(
                    (["fw", "push", "smaller", "branch","pop"], 2),
                    (["fw", "push", "left", "smaller", "branch","pop",
                      "push", "right", "smaller", "branch", "pop"], 3),
                    (["fw", "push", "left", "smaller", "branch","pop",
                      "push", "smaller", "branch","pop",
                      "push", "right", "smaller", "branch", "pop"], 2),
                    ),
            "fw": ["fw","fw"]
        }, actions={
            "fw": self.fw,
            "push": self.push,
            "pop": self.pop,
            "left": self.left,
            "right": self.right,
        }, axiom=["branch"], **kwargs)
    def clamp(self,lower, upper, val):
        return lower if lower>val else (upper if upper < val else val)

    def fw(self):
        self.renderer.draw_segment(20)

    def left(self):
        self.renderer.turn(self.clamp(10,50,random.gauss(30,18)))

    def right(self):
        self.renderer.turn(self.clamp(-10,-50,random.gauss(-30,18)))

    def push(self):
        self.renderer.push ()

    def pop(self):
        self.renderer.pop()
        self.renderer.turn(random.gauss(0,5))
        #cela fait varier l'angle dans une branche

def main():
    mode = "opengl"
    #mode = "turtle"

    if mode == "opengl":
        from lsys.render.gl_renderer import GLRenderer
        r = GLRenderer(scale=0.1, size=(800, 800))
        import OpenGL.GL as GL
        GL.glColor3f(0.2, 1.0, 0.0)
    elif mode == "turtle":
        from lsys.render.turtle_renderer import TurtleRenderer
        r = TurtleRenderer()
    s = TreeSystem(renderer=r)
    s.construct(8, debug=False)
    s.render()

if __name__ == "__main__":
    main()
