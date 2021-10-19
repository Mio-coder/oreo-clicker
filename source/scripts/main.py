from json import load
from typing import Union

import pygame as pg
from pygame import Surface, event
from pygame.display import set_mode, set_caption, set_icon, get_surface, update
from pygame.time import Clock
from pygame.transform import scale

from source.scripts.scenes import Game, Menu, Shop, Scene


class App:
    all_keycodes = tuple(getattr(pg.constants, key_str) for key_str in
                         filter(lambda k: k.startswith("K_"), dir(pg.constants)))

    def __init__(self, config: dict[str, Union[int, str]] = None):
        if config is None:
            with open("source/config.json") as file:
                config = load(file)
        self.width: int = ...
        self.high: int = ...
        self.fps: int = ...
        self.start_scene: str = ...
        for name in ["width", "high", "fps", "start_scene"]:
            setattr(self, name, config[name])

        self.game = Game(self)
        self.menu = Menu(self)
        self.shop = Shop(self)
        self._scene: Scene = ...

        self.done = True
        self.clock = Clock()
        self.screen: Surface

        self._scene = getattr(self, self.start_scene, "menu")
        # self.bgm = get_song("source/sounds/bgm.wav")

    @property
    def scene(self) -> Scene:
        return self._scene

    @scene.setter
    def scene(self, value: Scene):
        self._scene = value
        if not self.done:
            self._scene.initialize()
        self.update_screen()

    @property
    def scene_scale(self):
        return self.scene.settings["scale"][0] / self.scene.settings["size"][0], \
               self.scene.settings["scale"][1] / self.scene.settings["size"][1]

    def update_screen(self):
        set_mode(self.scene.settings["scale"])
        set_caption(self.scene.settings["title"])
        if self.scene.settings["icon"]:
            set_icon(self.scene.settings["icon"])

        # noinspection PyAttributeOutsideInit
        self.screen = get_surface()

    def get_scene_screen(self):
        return Surface(self.scene.settings["size"])

    def draw(self):
        self.screen.blit(scale(self.scene.draw(), self.scene.settings["scale"]), (0, 0))
        update()

    def update(self):
        self.scene.update()

    def run(self):
        # self.bgm.play(-1)
        self.done = False
        self._scene.initialize()
        while not self.done:
            self.update()
            self.draw()
            self.handle_events()
            self.handle_input()
            self.clock.tick(self.fps)

    def handle_events(self):
        for event_ in event.get():
            if event_.type == pg.QUIT:
                self.done = True
                break
            if "events_filter" not in self.scene.settings or event_.type in self.scene.settings["events_filter"]:
                self.scene.handle_event(event)

    def handle_input(self):
        self.handle_mouse_press()
        keys_pressed = pg.key.get_pressed()
        for keycode in self.all_keycodes:
            if keys_pressed[keycode]:
                self.scene.handle_input(keycode)

    def handle_mouse_press(self):
        pressed = pg.mouse.get_pressed(3)
        mouse_pos = self.get_mouse_pos()
        for key in range(3):
            if pressed[key]:
                self.scene.handle_mouse_press(key, mouse_pos)

    def get_mouse_pos(self):
        return pg.mouse.get_pos()[0] // self.scene_scale[0], pg.mouse.get_pos()[1] // self.scene_scale[1]
