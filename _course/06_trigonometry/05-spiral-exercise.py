# Using prvious exercise as a basis, draw a spiral path.
# Start in the center and move outwards.
# Note that this can be done by only changing one line of code and adding one line of code!

# Используйте за основу предыдущий пример. Нарисуйте спираль.
# Спираль начинается в центре и раскручивается к краям экрана.
# Это можно сделать поменяв одну единственную строчку кода предыдущего примера.

import math
import random

import pgzrun
import pygame
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

r = 1
theta = 0

def update():
    global theta, r
    theta += 1
    r += .1

def draw():
    # screen.fill((0, 0, 0))

    x = X0 + r * math.cos(math.radians(theta))
    y = Y0 + r * math.sin(math.radians(theta))

    pos = Vector2(x, y)

    screen.draw.filled_circle(pos, 10, color=(255,255,0))
    # screen.draw.line((X0, Y0), pos, color=(255,255,0))
    # screen.draw.text(f"theta: {theta}, pos={pos}", pos)


pgzrun.go()
