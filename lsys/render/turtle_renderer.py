import turtle
import time

from . import Renderer


class TurtleRenderer(Renderer):
    def __init__(self):
        self.stack = []
        turtle.left(90)

    def draw_segment(self, length):
        turtle.pd()
        turtle.forward(length)
        turtle.pu()

    def push(self):
        self.stack.append(tuple(turtle.position()) + (turtle.heading(),))

    def pop(self):
        popped_x, popped_y, popped_heading = self.stack.pop()
        turtle.setpos(popped_x, popped_y)
        turtle.seth(popped_heading)

    def turn(self, angle):
        turtle.left(angle)

    def display(self):
        time.sleep(5)

    def rotz(self, arg):
        pass