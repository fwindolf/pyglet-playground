import logging as log
import random
from pyglet import window
from model.object import Point, Rectangle, FilledRectangle, Circle, FilledCircle
from model.color import Color

class Controller:
    def __init__(self):
        self.renderer = None
        self.logger = log.getLogger("Controller")
        self.logger.debug("Controller superclass created")

    def set_renderer(self, renderer):
        self.renderer = renderer
        self.logger.debug("Controller has new renderer")

    def on_mouse_press(self, x, y, button, modifiers):
        self.logger.debug("Controller acting on mouse press", x, y)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.logger.debug("Controller acting on mouse drag", x, y, dx, dy)

    def on_key_press(self, symbol, modifiers):
        self.logger.debug("Controller acts on key press", smybol)

    def on_key_release(self, symbol, modifiers):
        self.logger.debug("Controller acts on key released", symbol)



class RandomObjectController(Controller):
    def __init__(self):
        super(RandomObjectController, self).__init__()

    def on_mouse_press(self, x, y, button, modifiers):
        self.logger.debug("RandomObjectController acts on mouse press", x, y)
        rnd = random.randint(0, 3)
        # create different shapes
        obj = {
            0 : Circle(x, y, radius=random.randint(1, 40), color=Color.random(),
                line=random.randint(1,10)),
            1 : FilledCircle(x, y, radius=random.randint(1, 40),
                color=Color.random()),
            2 : Rectangle(x, y, random.randint(40, 200),
                random.randint(20, 200), color=Color.random(),
                line=random.randint(1,10)),
            3 : FilledRectangle(x, y, random.randint(40, 200),
                random.randint(20, 200), color=Color.random())
        }[rnd]
        if self.renderer:
            self.renderer.add(obj)
