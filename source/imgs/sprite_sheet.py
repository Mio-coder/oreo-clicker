import json
import os
from typing import Dict, Tuple, Union

from pygame import Surface, Rect
from pygame.transform import scale
from pygame.image import load
from os.path import join


class SpriteSheet:
    def __init__(self, source: Surface, info: Dict[str, Union[Tuple[int, int, int, int], str]], ):
        self.source = source
        self.info = info
        self.images: Dict[str, Surface] = dict()
        self.generated = False

    def generate(self):
        if not self.generated:
            self.source = self.source.convert_alpha()
        for image in self.info:
            self.images[image] = self.get_subsurface(image)
        self.generated = True

    def get(self, name: str):
        if name not in self.images:
            self.generate()
        return self.images[name] if name in self.images else self.images[self.info["default"]]

    def __getitem__(self, item):
        return self.get(item)

    def get_subsurface(self, name: str) -> Surface:
        cords = self.info[name]
        if self.info["scale"] == 1:
            return self.source.subsurface(Rect(cords))
        raw_image = self.source.subsurface(Rect(cords))

        return scale(raw_image, (
            int(raw_image.get_width() * self.info["scale"]),
            int(raw_image.get_height() * self.info["scale"]
                )))


def load_sprite_sheet(name: str):
    return SpriteSheet(load_image(name + "_sheet.png"), json.load(open(get_path(name + "_sheet_info.json"))))


def load_image(name: str):
    return load(get_path(name))


def get_path(name: str):
    return join(os.path.abspath(""), "source", "imgs", name)
