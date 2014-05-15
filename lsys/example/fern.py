import lsys.core as core
#import random


class FernSystem(core.System):
    def __init__(self, *args, **kwargs):
        lbranch = [
            "pushl", "muchsmaller", "push", "left", "branch", "pop", "popl"]
        rbranch = [
            "pushl", "muchsmaller", "push", "right", "branch", "pop", "popl"]
        super().__init__(rules={
            "root": ["fw"] + (lbranch + ["fw", "smaller", "rotz"] + rbranch +
                ["fw", "smaller", "rotz"]) * 3 + ["rotz", "root"],
            "branch": ["fw"] + (lbranch + ["fw", "rotz"] + rbranch +
                ["fw", "rotz"]) * 3 + ["muchsmaller", "rotz", "branch"],
        }, actions={
            "fw": self.fw,
            "push": self.push,
            "pop": self.pop,
            "left": self.left,
            "right": self.right,
            "branch": self.branch,
            "smaller": self.smaller,
            "muchsmaller": self.muchsmaller,
            "pushl": self.pushl,
            "popl": self.popl,
            "rotz": self.rotz,
        }, axiom=["root"], **kwargs)
        self.length_stack = [10]

    def fw(self):
        self.renderer.draw_segment(self.length_stack[-1])
        self.renderer.turn(-1)

    def branch(self):
        self.renderer.draw_segment(self.length_stack[-1] * 4)

    def smaller(self):
        self.length_stack[-1] *= 0.9

    def muchsmaller(self):
        self.length_stack[-1] *= 0.4

    def left(self):
        self.renderer.turn(80)

    def right(self):
        self.renderer.turn(-80)

    def push(self):
        self.renderer.push()

    def pop(self):
        self.renderer.pop()

    def pushl(self):
        self.length_stack.append(self.length_stack[-1])

    def popl(self):
        self.length_stack.pop()

    def rotz(self):
        self.renderer.rotz(1)


def main():
    mode = "opengl"
    #mode = "turtle"

    if mode == "opengl":
        from lsys.render.gl_renderer import GLRenderer
        r = GLRenderer(scale=6, size=(800, 800))
        import OpenGL.GL as GL
        GL.glColor3f(0.2, 1.0, 0.0)
    elif mode == "turtle":
        from lsys.render.turtle_renderer import TurtleRenderer
        r = TurtleRenderer()
    s = FernSystem(renderer=r)
    s.construct(depth=3, debug=False)
    print(s.expanded.count("push"), "pushes,", s.expanded.count("pop"), "pops")
    s.render()

if __name__ == "__main__":
    main()
