import math
import random

import pgzrun
import pygame
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

r = 75
theta = 0

def update():
    global theta
    theta += 1

def draw():
    screen.fill((0, 0, 0))

    x = X0 + r * math.cos(math.radians(theta))
    y = Y0 + r * math.sin(math.radians(theta))

    pos = Vector2(x, y)

    screen.draw.circle(pos, r // 4, color=(255,255,0))
    screen.draw.line((X0, Y0), pos, color=(255,255,0))
    screen.draw.text(f"theta: {theta}, pos={pos}", pos)


pgzrun.go()

