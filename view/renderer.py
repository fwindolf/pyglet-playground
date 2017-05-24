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


    def set_background(self, color=Color.BLACK):
        """
        Change the background color of the window
        """
        self.background = color

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
        window.clear()
        for obj in self.objects:
            obj.render()
