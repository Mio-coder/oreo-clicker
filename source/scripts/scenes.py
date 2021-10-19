from button import Button
from source.scripts.main import App


class Scene:
    settings = {"scale":..., "size":...}

    def __init__(self, app):
        self.app = app

    def render(self):
        pass

    def initialize(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def handle_event(self, event):
        pass

    def handle_input(self, keycode):
        pass

    def handle_mouse_press(self, key, mouse_pos):
        pass


class Menu(Scene):

    def __init__(self, app: App):
        Scene.__init__(self, app)

        def change(*args):
            pass

        button = Button


class Game(Scene):
    pass


class Shop(Scene):
    pass
