import pyglet
from controller.controller import Controller
from view.renderer import Renderer
from model.color import Color


def main():
    renderer = Renderer(800, 600)
    renderer.set_background(Color.WHITE)
    controller = RandomObjectController(renderer)

    pyglet.app.run()
