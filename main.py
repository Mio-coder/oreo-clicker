from json import load

import pygame as pg

if __name__ == '__main__':
    pg.init()
    from source.scripts.manager import App

    with open("source/config.json") as file:
        data: dict = load(file)
    app = App(data)
    app.run()
