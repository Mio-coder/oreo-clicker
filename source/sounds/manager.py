from os.path import join, abspath

from pygame.mixer import Sound


def get_song(song: str) -> Sound:
    return Sound(get_path(song))


def get_path(name: str):
    return join(abspath(""), "assets", "sounds", name)
