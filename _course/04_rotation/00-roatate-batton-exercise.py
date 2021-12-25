import math
import random

import pgzrun

# Rotate a baton-like object (see below) around its center for 45 degress
# Поверните гантелю (см ниже) вокруг ее центра на 45 градусов

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2


def update():
    pass

def draw():
    screen.fill((0, 0, 0))

    x, y = X0, Y0 + 100
    x1, y1 = X0, Y0 - 100

    screen.draw.circle(pos=(x, y), radius=10, color=(0, 255, 0))
    screen.draw.line(start=(x, y), end=(x1, y1), color=(255, 255, 255))
    screen.draw.circle(pos=(x1, y1), radius=10, color=(0, 255, 0))

pgzrun.go()

