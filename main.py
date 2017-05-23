import pyglet
import random
from enum import Enum
from pyglet.window import mouse

window = pyglet.window.Window()

objects = list()

def random_color():
    rnd = random.randint(0, 3)
    return {
            0 : Color.WHITE,
            1 : Color.RED,
            2 : Color.GREEN,
            3 : Color.BLUE
        }[rnd]


    return {
        0 : Color.WHITE,
        1 : Color.RED,
        2 : Color.GREEN,
        3 : Color.BLUE
    }[rnd]

class Color(Enum):
    WHITE = (255, 255, 255)
    RED =   (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE =  (0, 0, 255)

    def rgb(self):
        return self.value

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
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, self.vertices(), color)

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
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, self.vertices(False), color)

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
        pyglet.gl.glLineWidth(self.lineWidth)
        pyglet.graphics.draw(8, pyglet.gl.GL_LINES, self.vertices(), color)



@window.event
def on_draw():
    window.clear()
    print("ON_DRAW called")
    for obj in objects:
        obj.render()

@window.event
def on_mouse_press(x,y,button, modifiers):
    print("ON_MOUSE_PRESS called")
    if button == mouse.LEFT:
        objects.append(Point(x, y, random_color()))
    elif button == mouse.RIGHT:
        objects.append(Rectangle(x, y,
                                 random.randint(40, 200),
                                 random.randint(20, 200),
                                 random_color(),
                                 line=10.0
                                 ))


pyglet.app.run()
