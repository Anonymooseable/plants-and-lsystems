import core
import random

from render.gl_renderer import GLRenderer


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
        self.renderer.draw_segment(random.randrange(0, 11) / 3)
        self.renderer.turn(random.randrange(-3, 4))

    def push_left(self):
        self.renderer.push()
        self.renderer.turn(random.randrange(0, 50))

    def pop_right(self):
        self.renderer.pop()
        self.renderer.turn(random.randrange(-50, 1))


def main():
    s = DemoSystem(renderer=GLRenderer(scale=1, size=(800, 800)))
    s.construct(depth=10)
    for i in range(5):
        s.renderer = GLRenderer(scale=3, size=(800, 800))
        s.render()

if __name__ == "__main__":
    main()
