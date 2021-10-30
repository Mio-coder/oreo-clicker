from pygame import Surface

from source.scripts.button import Button
from source.sounds.manager import get_song

click_sound = get_song("click.wav")


class Scene:
    settings = {"scale": ..., "size": ..., "icon": None}

    def __init__(self, app):
        self.app = app

    def initialize(self):
        pass

    def render(self):
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
    settings = {"scale": (500, 900), "size": (500, 900), "title": "{app.name} - Menu", "icon": None}

    def __init__(self, app):
        Scene.__init__(self, app)
        self.settings["title"].format(app=app)
        self.screen: Surface = ...
        self.button_game: Button = ...
        # self.button_settings: Button = ...

    def initialize(self):
        self.screen = self.app.scene_screen

        def game(_):
            self.app.scene = self.app.menu

        # def settings(_):
        #     # self.app.scene = self.app.settings
        #     pass

        self.button_game = Button(
            self.screen,
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

    def render(self):
        self.button_game.render()

    def draw(self):
        return self.screen


class Clicker:

    def __init__(self, game, num):
        self.game = game
        self.num = num
        self.screen: Surface = ...

    def initialize(self):
        self.screen = Surface((
            self.game.settings["size"][0] // 3 * self.num,
            self.game.settings["size"][1]
        ))

    def draw(self):
        return self.screen

    def handle_mouse_press(self, key, mouse_pos):
        print(f"click in {self.__class__.__name__}: key {key} at {mouse_pos}")


class MilkClicker(Clicker):

    def __init__(self, game):
        Clicker.__init__(self, game, 1)

    def draw(self):
        self.screen.fill((40, 40, 40))
        return self.screen


class CookieClicker(Clicker):

    def __init__(self, game):
        Clicker.__init__(self, game, 3)

    def draw(self):
        self.screen.fill((200, 40, 40))
        return self.screen


class OREOClicker(Clicker):

    def __init__(self, game):
        Clicker.__init__(self, game, 2)

    def draw(self):
        return self.screen


class Game(Scene):
    settings = {"scale": (1500, 900), "size": (1500, 900), "title": "{app.name} - Game", "icon": None}

    def __init__(self, app):
        Scene.__init__(self, app)
        self.settings["title"].format_map({"app": app})
        self.screen: Surface = ...

        self.milkClicker: MilkClicker = ...
        self.cookieClicker: CookieClicker = ...
        self.oreoClicker: OREOClicker = ...

    def initialize(self):
        self.screen = self.app.get_scene_screen()

        self.milkClicker = MilkClicker(self)
        self.cookieClicker = CookieClicker(self)
        self.oreoClicker = OREOClicker(self)

        self.milkClicker.initialize()
        self.cookieClicker.initialize()
        self.oreoClicker.initialize()

    def draw(self):
        milk_screen = self.milkClicker.draw()
        self.screen.blit(milk_screen, (0, 0), milk_screen.get_rect())
        return self.screen

    def handle_mouse_press(self, key, mouse_pos):
        click_sound.play()
        print(self.cookieClicker.screen.get_rect())
        breakpoint()
        if self.milkClicker.screen.get_rect().collidepoint(mouse_pos):
            self.milkClicker.handle_mouse_press(key, [mouse_pos[0] - self.settings["size"][0] * 0, mouse_pos[1]])
        if self.cookieClicker.screen.get_rect().collidepoint(mouse_pos):
            self.milkClicker.handle_mouse_press(key, [mouse_pos[0] - self.settings["size"][0] * 1, mouse_pos[1]])
        if self.oreoClicker.screen.get_rect().collidepoint(mouse_pos):
            self.milkClicker.handle_mouse_press(key, [mouse_pos[0] - self.settings["size"][0] * 2, mouse_pos[1]])

    def update(self):
        pass


class Shop(Scene):
    settings = {"scale": (400, 500), "size": (400, 500), "title": "{app.name} - Shop", "icon": None}

    def __init__(self, app):
        Scene.__init__(self, app)
        self.settings["title"].format(app=app)

    def initialize(self):
        pass


class Settings(Scene):

    def __init__(self, app):
        Scene.__init__(self, app)
