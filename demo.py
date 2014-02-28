import lsys.core as core
#import random

class DemoSystem(core.System):
    def __init__(self, *args, **kwargs):
            super().__init__(rules={
                "1": ["1", "2"],
                "0": ["1", "[", "0", "]", "0"],
            }, actions={
                "1": self.draw_segment,
                "2": self.draw_segment,
                "0": self.draw_segment,
                "[": self.push_left,
                "]": self.pop_right,
            }, axiom="0", **kwargs)

    def draw_segment(self):
        self.renderer.draw_segment(5)
        #self.renderer.turn(1)

    def push_left(self):
        self.renderer.push()
        self.renderer.turn(45)

    def pop_right(self):
        self.renderer.pop()
        self.renderer.turn(-45)


def main():
    from lsys.render.gl_renderer import GLRenderer
    s = DemoSystem(renderer=GLRenderer(scale=1, size=(800, 800)))
    s.construct(depth=10)
    s.render()

if __name__ == "__main__":
    main()
