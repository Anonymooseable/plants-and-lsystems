import lsys.core as core
#import random


class DemoSystem(core.System):
    def __init__(self, *args, **kwargs):
        lbranch = ["push", "left", "branch", "pop"]
        rbranch = ["push", "right", "branch", "pop"]
        super().__init__(rules={
            "root": ["exfw"] + (lbranch + ["phatfw", "smaller"] + rbranch + ["phatfw", "smaller"]) * 3 + ["root"],
            "branch": ["phatfw"] + (lbranch + ["exfw", "exfw"] + rbranch + ["exfw", "exfw"]) * 3 + ["branch"],
            "exfw": ["exfw", "exfw"],
            "phatfw": ["phatfw", "phatfw", "exfw", "exfw"],
        }, actions={
            "exfw": self.fw,
            "fw": self.fw,
            "push": self.push,
            "pop": self.pop,
            "left": self.left,
            "right": self.right,
            "branch": self.fw,
            "smaller": self.smaller,
            "pushl": self.pushl,
            "popl": self.popl,
        }, axiom=["root"], **kwargs)
        self.length_stack = [10]

    def fw(self):
        self.renderer.draw_segment(self.length_stack[-1])
        #self.renderer.turn(-0.005)

    def smaller(self):
        self.length_stack[-1] *= 0.9

    def left(self):
        self.renderer.turn(50)

    def right(self):
        self.renderer.turn(-50)

    def push(self):
        self.renderer.push()

    def pop(self):
        self.renderer.pop()

    def pushl(self):
        self.length_stack.append(self.length_stack[-1])

    def popl(self):
        self.length_stack.pop()


def main():
    mode = "opengl"
    #mode = "turtle"

    if mode == "opengl":
        from lsys.render.gl_renderer import GLRenderer
        r = GLRenderer(scale=0.032, size=(800, 800))
        import OpenGL.GL as GL
        GL.glColor3f(0.2, 1.0, 0.0)
    elif mode == "turtle":
        from lsys.render.turtle_renderer import TurtleRenderer
        r = TurtleRenderer()
    s = DemoSystem(renderer=r)
    s.construct(depth=6, debug=False)
    print(s.expanded.count("push"), "pushes,", s.expanded.count("pop"), "pops")
    s.render()

if __name__ == "__main__":
    main()
