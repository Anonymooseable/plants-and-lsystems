import pygame
import OpenGL.GL as GL

from . import Renderer


class GLRenderer(Renderer):
    def __init__(self, scale=1, size=(800, 600)):
        pygame.display.init()
        pygame.display.set_mode(size, pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.clock = pygame.time.Clock()
        self.dragging = False

        self.draw_queue = [lambda self: GL.glClear(GL.GL_COLOR_BUFFER_BIT)]

        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        GL.glColor3f(1.0, 1.0, 1.0)

        GL.glViewport(0, 0, size[0], size[1])
        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(-size[0] / 2, size[0] / 2, -size[1] / 2, size[1] / 2, 0, 10)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()
        self.scale = scale
        GL.glScalef(scale, scale, 0)

    def defer_draw(fun):
        def wrapped(self, *args, **kwargs):
            self.draw_queue.append(lambda self: fun(self, *args, **kwargs))
        return wrapped

    @defer_draw
    def draw_segment(self, length):
        GL.glBegin(GL.GL_LINES)
        GL.glVertex2f(0.0, 0.0)
        GL.glVertex2f(0.0, length)
        GL.glEnd()
        GL.glTranslatef(0.0, length, 0.0)

    @defer_draw
    def push(self):
        GL.glPushMatrix()

    @defer_draw
    def pop(self):
        GL.glPopMatrix()

    @defer_draw
    def turn(self, angle):
        GL.glRotatef(angle, 0.0, 0.0, 1.0)

    def display(self):
        quit = False
        while not quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key in (pygame.K_ESCAPE, pygame.K_q):
                    quit = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        GL.glScalef(0.94, 0.94, 0)
                        self.scale *= 0.94
                    elif event.button == 5:
                        GL.glScalef(1 / 0.94, 1 / 0.94, 0)
                        self.scale /= 0.94
                    elif event.button == 1:
                        self.dragging = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.dragging = False
                elif event.type == pygame.MOUSEMOTION and self.dragging:
                    GL.glTranslatef(event.rel[0] / self.scale, -event.rel[1] / self.scale, 0)

            GL.glPushMatrix()
            for f in self.draw_queue:
                f(self)
            GL.glPopMatrix()
            pygame.display.flip()
            self.clock.tick(30)
