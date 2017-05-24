import pyglet
from model.object import Circle, FilledCircle

window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()
    circle = Circle(100, 200, radius=100, line=10)
    circle.render()

    fcircle = FilledCircle(400, 200, radius=300)
    fcircle.render()


pyglet.app.run()
