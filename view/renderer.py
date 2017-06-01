from pyglet import window, gl
from model.color import Color


class Renderer(window.Window):
    def __init__(self, width=None, height=None, resizable=True, fullscreen=False):
        """
        Create a new window and initialize it
        """
        self.x = 0
        self.y = 0
        self.background = Color.BLACK # default
        self.objects = list()

        super(Renderer, self).__init__(width=width, height=height,
                                    resizable=resizable, fullscreen=fullscreen)
        self.controller = None


    def get_window(self):
        """
        Get the current window
        """
        return self.window

    def set_background(self, color=Color.BLACK):
        """
        Change the background color of the window
        """
        self.background = color

    def set_controller(self, controller):
        """
        Change the controller that is attached to the window
        """
        self.controller = controller

    def add(self, generic_object):
        """
        Add an object that should be drawn later
        """
        self.objects.append(generic_object)
        self.on_draw()

    def on_draw(self):
        """
        Method gets invoked when a re-draw window event is issued
        """
        #gl.glClearColor(self.background)
        super(Renderer, self).clear()
        for obj in self.objects:
            obj.render()

    def on_mouse_press(self, x, y, button, modifiers):
        if self.controller:
            self.controller.on_mouse_press(x, y, button, modifiers)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print ("Mouse dragged", x, y, dx, dy)

    def on_key_press(self, symbol, modifiers):
        print("Key pressed", symbol)

    def on_key_release(self, symbol, modifiers):
        print("Key released", symbol)
