from pyglet import window, gl
from model.color import Color


class Renderer:
    def __init__(self, width=None, height=None, resizable=True, fullscreen=False):
        """
        Create a new window and initialize it
        """
        self.width = widht
        self.height = height
        self.resizable = resizable
        self.fullscreen = fullscreen
        self.background = Color.BLACK # default
        self.objects = list()
        self.window = window.Window(width=width, height=height,
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

    def set_controller(self):
        """
        Change the controller that is attached to the window
        """

    def add(self, generic_object):
        """
        Add an object that should be drawn later
        """
        self.objects.append(generic_object)
        self.on_draw()

    @window.event
    def on_draw(self):
        """
        Method gets invoked when a re-draw window event is issued
        """
        gl.glClearColor(self.background)
        self.window.clear()
        for obj in self.objects:
            obj.render()

    @window.event
    def on_mouse_press(self, x, y, button, modifiers):
        if self.controller:
            self.controller.on_mouse_press(x, y, button, modifiers)

    @window.event
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print ("Mouse dragged", x, y, dx, dy)

    @window.event
    def on_key_press(self, symbol, modifiers):
        print("Key pressed", symbol)

    @window.event
    def on_key_release(self, symbol, modifiers):
        print("Key released", symbol)
