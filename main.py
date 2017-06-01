import pyglet
import logging
from controller.controller import Controller, RandomObjectController
from view.renderer import Renderer
from model.color import Color


def main():
    # enable debug logging
    logging.getLogger('Controller').setLevel(logging.DEBUG)
    logging.getLogger('Renderer').setLevel(logging.DEBUG)

    # create the renderer for a window
    renderer = Renderer(800, 600)
    renderer.set_background(Color.WHITE)

    # create the controller for user interaction
    controller = RandomObjectController()

    # install the renderer at the controller
    # and the controller at the renderer
    controller.set_renderer(renderer)
    renderer.set_controller(controller)

    pyglet.app.run()







main()
