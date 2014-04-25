import lsys.core as core
import random
import math

class StochasticRule:
    def __init__(self, *output_sets):
        self.output_sets = output_sets
        self.sum = sum([s[1] for s in output_sets])

    def __iter__(self):
        r = random.randrange(self.sum + 1)
        subtotal = 0
        for s, factor in self.output_sets:
            subtotal += factor
            if r <= subtotal:
                return iter(s)
        


class FernSystem(core.System):
    def __init__(self, *args, **kwargs):
        super().__init__(rules={
            "branch": StochasticRule(
                    (["fw", "push", "left", "smaller", "branch",
                      "pop", "push", "right", "smaller", "branch", "pop"], 1),
                    (["fw", "push", "left", "smaller", "branch",
                      "pop", "push", "smaller", "branch",
                      "pop", "push", "right", "smaller", "branch", "pop"], 1),
                    )
        }, actions={
            "fw": self.fw,
            "push": self.push,
            "pop": self.pop,
            "left": self.left,
            "right": self.right,
            "smaller": self.smaller,
        }, axiom=["branch"], **kwargs)
        self.length_stack = [85]

    def fw(self):
        self.renderer.draw_segment(self.length_stack[-1])
        self.renderer.turn(-1)

    def branch(self):
        self.renderer.draw_segment(self.length_stack[-1] * 4)

    def smaller(self):
        self.length_stack[-1] /= math.log(len(self.length_stack)+1,math.e)*1.2

    def left(self):
        self.renderer.turn(random.randrange(40,60))

    def right(self):
        self.renderer.turn(-1*random.randrange(40,60))

    def push(self):
        self.renderer.push ()
        self.length_stack.append(self.length_stack[-1])

    def pop(self):
        self.renderer.pop()
        self.renderer.turn(random.randrange(0,50)-25) # this makes the angle waver inside a branch
                                                      # i.e. at every split the angles changes a bit
        self.length_stack.pop()

    def rotz(self):
        self.renderer.rotz(1)


def main():
    mode = "opengl"
    #mode = "turtle"

    if mode == "opengl":
        from lsys.render.gl_renderer import GLRenderer
        r = GLRenderer(scale=4, size=(800, 800))
        import OpenGL.GL as GL
        GL.glColor3f(0.2, 1.0, 0.0)
    elif mode == "turtle":
        from lsys.render.turtle_renderer import TurtleRenderer
        r = TurtleRenderer()
    s = FernSystem(renderer=r)
    s.construct(depth=6, debug=False)
    print(s.expanded.count("push"), "pushes,", s.expanded.count("pop"), "pops")
    s.render()

if __name__ == "__main__":
    main()
