import lsys.core as core
import random
import math


class TreeSystem(core.System):
    def __init__(self, *args, **kwargs):
        super().__init__(rules={
            "branch": core.StochasticRule(
                    (["fw", "push", "smaller", "branch","pop"], 3),
                    (["fw", "push", "left", "smaller", "branch","pop",
                      "push", "right", "smaller", "branch", "pop"], 2),
                    (["fw", "push", "left", "smaller", "branch","pop",
                      "push", "smaller", "branch","pop",
                      "push", "right", "smaller", "branch", "pop"], 2),
                    )
            "fw": core.StochasticRule(
                    (["fw","fw","fw"],math.floor(40/len(self.actions))+1)
                    (["fw","fw"],math.floor(80/len(self.actions))+1)
                    (["fw"],6)
        }, actions={
            "fw": self.fw,
            "push": self.push,
            "pop": self.pop,
            "left": self.left,
            "right": self.right,
        }, axiom=["branch"], **kwargs)

    def fw(self):
        self.renderer.draw_segment(20)

    def left(self):
        self.renderer.turn(random.gauss(20,6.5))

    def right(self):
        self.renderer.turn(random.gauss(-20,6.5))

    def push(self):
        self.renderer.push ()

    def pop(self):
        self.renderer.pop()
        self.renderer.turn(random.gauss(0,5)) #cela fait varier l'angle
                                             #dans une branche
                         
def main():
    #mode = "opengl"
    mode = "turtle"

    if mode == "opengl":
        from lsys.render.gl_renderer import GLRenderer
        r = GLRenderer(scale=4, size=(800, 800))
        import OpenGL.GL as GL
        GL.glColor3f(0.2, 1.0, 0.0)
    elif mode == "turtle":
        from lsys.render.turtle_renderer import TurtleRenderer
        r = TurtleRenderer()
    s = TreeSystem(renderer=r)
    s.construct(, debug=False)
    s.render()

if __name__ == "__main__":
    main()
