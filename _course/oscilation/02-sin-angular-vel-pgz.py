import math
import random

import pgzrun
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500
X0 = WIDTH // 2
Y0 = HEIGHT // 2

ampl = random.randint(200, 220)
angle = 0
a_velocity = .05

def update():
    global angle
    angle += a_velocity
    print(angle)

def draw():
    screen.fill((0, 0, 0))

    x = ampl * math.sin(angle)

    screen.draw.line(start=(X0, Y0), end=(X0 + x, Y0), color=(255, 255, 255))
    screen.draw.circle(pos=(X0 + x, Y0), radius=10, color=(255, 255, 0))

pgzrun.go()

