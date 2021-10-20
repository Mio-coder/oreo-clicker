from source.scripts.button import Button
from source.scripts.main import App
from source.sounds.manager import get_song

click_sound = get_song("source/sounds/click.wav")


class Scene:
    settings = {"scale": ..., "size": ...}

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
        self.settings = {"scale": ..., "size": ..., "title": ...}

        def game(_):
            self.app.scene = self.app.menu

        def settings(_):
            # self.app.scene = self.app.settings
            pass

        self.button_game = Button(
            self.app.screen,
            (300, 200),
            ["menu"],
            action=game
        )

        # button_settings = Button(
        #     self.app.screen,
        #     (400, 200),
        #     ["settings"],
        #     action=settings
        # )

    def draw(self):
        self.button_game.render()


class Game(Scene):

    def __init__(self, app: App):
        Scene.__init__(self, app)
        self.settings = {"scale": ..., "size": ..., "title": ...}

    def handle_mouse_press(self, key, mouse_pos):
        click_sound.play()


class Shop(Scene):

    def __init__(self, app: App):
        Scene.__init__(self, app)
        self.settings = {"scale": ..., "size": ..., "title": "Shop"}


class Settings(Scene):

    def __init__(self, app: App):
        Scene.__init__(self, app)
