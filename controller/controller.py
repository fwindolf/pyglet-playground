from pyglet import window
from model.object import Point, Rectangle, FilledRectangle

class Controller:
    def __init__(self):
        self.renderer = None

    def set_renderer(self, renderer=None):
        self.renderer = renderer

    def on_mouse_press(self, x, y, button, modifiers):
        print ("Mouse pressed", x, y)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print ("Mouse dragged", x, y, dx, dy)

    def on_key_press(self, symbol, modifiers):
        print("Key pressed", symbol)

    def on_key_release(self, symbol, modifiers):
        print("Key released", symbol)


class RandomObjectController(Controller):
    def __init__(self):
        super(RandomObjectController, self).__init__()

    def on_mouse_press(self, x, y, button, modifiers):
        rnd = random.randint(0, 5)
        # create different shapes
        obj = {
            0 : Circle(x, y, radius=random.randint(1, 40), color=Color.random(),
                line=random.randint(1,10)),
            1 : FilledCircle(x, y, radius=random.randint(1, 40),
                color=Color.random()),
            2 : Rectangle(x, y, random.randint(40, 200),
                random.randint(20, 200), color=random_color(),
                line=random.randint(1,10)),
            3 : FilledRectangle(x, y, random.randint(40, 200),
                random.randint(20, 200), color=random_color())
        }[rnd]
        if self.renderer:
            renderer.add(obj)
