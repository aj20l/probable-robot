from enum import Enum
import pygame, pgzero, pgzrun
from app import App
from input import InputManager
import os
print("CWD:", os.getcwd())


TITLE = "Cavern"
pgzero_version = [int(s) if s.isnumeric() else s for s in pgzero.__version__.split('.')]
if pgzero_version < [1,2]:
    print("This game requires at least version 1.2 of Pygame Zero. You have version {0}. Please upgrade using the command 'pip3 install --upgrade pgzero'".format(pgzero.__version__))
    sys.exit()


app = App()
input_manager = InputManager()


def update():
    input_state = input_manager.poll()
    app.update(input_state)


def draw():
    screen.clear()
    app.draw(screen) 





pgzrun.go()
