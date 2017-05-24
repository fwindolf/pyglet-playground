import math
from model.color import Color
from pyglet import graphics, gl

class Object:
    def __init__(self, x, y, color=Color.WHITE):
        self.x = x
        self.y = y
        self.color = color

    def render(self):
        pass

class Point(Object):
    def __init__(self, x, y, color=Color.WHITE):
        super(Point, self).__init__(x, y, color)

    def vertices(self):
        return ('v2f', (self.x, self.y))

    def render(self):
        color = ('c3B', self.color.rgb() * 1)
        graphics.draw(1, gl.GL_POINTS, self.vertices(), color)

class FilledRectangle(Object):
    def __init__(self, x, y, width, height, color=Color.WHITE):
        super(Rectangle, self).__init__(x, y, color)
        self.width = width
        self.height = height

    def vertices(self):
        dx = self.width/2
        dy = self.height/2
        return ('v2f', (self.x - dx, self.y - dy,
                        self.x - dx, self.y + dy,
                        self.x + dx, self.y + dy,
                        self.x + dx, self.y - dy))

    def render(self):
        color = ('c3B', self.color.rgb() * 4)
        graphics.draw(4, gl.GL_QUADS, self.vertices(False), color)

class Rectangle(Object):
    def __init__(self, x, y, width, height, color=Color.WHITE, line=2.0):
        super(Rectangle, self).__init__(x, y, color)
        self.width = width
        self.height = height
        self.lineWidth = line

    def vertices(self):
        dl = self.lineWidth/2
        dx = self.width/2
        dy = self.height/2

        return ('v2f', (self.x - dx, self.y - dy,
                        self.x - dx, self.y + dy,
                        self.x - dx, self.y - dy,
                        self.x + dx, self.y - dy,
                        self.x + dx, self.y - dy,
                        self.x + dx, self.y + dy,
                        self.x - dx, self.y + dy,
                        self.x + dx, self.y + dy))

    def render(self):
        color = ('c3B', self.color.rgb() * 8)
        gl.glLineWidth(self.lineWidth)
        graphics.draw(8, gl.GL_LINES, self.vertices(), color)

class CircleBase(Object):
    def __init__(self, x, y, radius, color=Color.WHITE, points=200):
        super(CircleBase, self).__init__(x, y, color)
        self.radius = radius
        self.points = points

    def vertices(self):
        """
        Create a list of points that make up for the outline of the circle
        """
        verts = list()
        for i in range(self.points):
            angle = math.radians(float(i)/ self.points * 360.0)
            verts.append(self.radius * math.cos(angle) + self.x)
            verts.append(self.radius * math.sin(angle) + self.y)

        return ('v2f', verts)

    def render(self):
        pass

class Circle(CircleBase):
    def __init__(self, x, y, radius, points=200, color=Color.WHITE, line=2.0):
        super(Circle, self).__init__(x, y, radius, color, points)
        self.lineWidth = line

    def render(self):
        color = ('c3B', self.color.rgb() * self.points)
        gl.glEnable(gl.GL_BLEND);
        gl.glEnable(gl.GL_LINE_SMOOTH)
        gl.glHint(gl.GL_LINE_SMOOTH_HINT, gl.GL_NICEST);
        gl.glLineWidth(self.lineWidth)
        graphics.draw(self.points, gl.GL_LINE_LOOP, self.vertices(), color)

class FilledCircle(CircleBase):
    def __init__(self, x, y, radius, points=200, color=Color.WHITE):
        super(FilledCircle, self).__init__(x, y, radius, color, points)

    def render(self):
        color = ('c3B', self.color.rgb() * self.points)
        gl.glEnable(gl.GL_BLEND);
        gl.glEnable(gl.GL_LINE_SMOOTH)
        gl.glHint(gl.GL_LINE_SMOOTH_HINT, gl.GL_NICEST);
        graphics.draw(self.points, gl.GL_POLYGON, self.vertices(), color)
