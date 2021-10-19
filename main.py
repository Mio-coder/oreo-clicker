from source.scripts.main import App
from json import load

if __name__ == '__main__':
    with open("source/config.json") as file:
        data: dict = load(file)
    app = App(data)
