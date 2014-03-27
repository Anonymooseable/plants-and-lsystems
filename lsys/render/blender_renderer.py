import bpy
import mathutils
import math

from . import Renderer


class BlenderMeshRenderer(Renderer):
    def __init__(self, *args, **kwargs):
        self.mesh = bpy.data.meshes.new(name="LSystem")
        self.object = bpy.data.objects.new(object_data=self.mesh, name="LSystem")
        self.object.matrix_local = mathutils.Matrix.Translation(bpy.context.scene.cursor_location) * mathutils.Matrix.Scale(kwargs.get("scale", 1), 4)
        self.stack = []
        self.matrix = mathutils.Matrix()

        self.points = [mathutils.Vector((0, 0, 0))]
        self.translate = mathutils.Vector((0, 0, 0))
        self.lines = []
        #self.current_root = mathutils.Vector((0, 0, 0))
        self.prev_point = 0

    def draw_segment(self, length):
        point_idx = len(self.points)
        point = mathutils.Vector((0, 0, length)) * self.matrix + self.points[self.prev_point]
        self.points.append(point)
        #self.matrix *= mathutils.Matrix.Translation(mathutils.Vector((0, 0, length)))
        self.lines.append((self.prev_point, point_idx))
        self.prev_point = point_idx

    def push(self):
        self.stack.append((self.matrix, self.prev_point))
        #self.matrix *= mathutils.Matrix.Rotation(0.2, 4, 'Y')

    def pop(self):
        self.matrix, self.prev_point = self.stack.pop()

    def turn(self, angle):
        self.matrix *= mathutils.Matrix.Rotation(angle / 180 * math.pi, 4, 'Y')

    def scale(self, factor):
        self.matrix *= mathutils.Matrix.Scale(factor, 4) #* self.matrix
        pass

    def display(self):
        self.mesh.from_pydata(self.points, self.lines, [])
        self.mesh.validate()
        self.mesh.update()
        bpy.context.scene.objects.link(self.object)

    def rotz(self, angle):
        self.matrix *= mathutils.Matrix.Rotation(angle / 180 * math.pi, 4, 'X')