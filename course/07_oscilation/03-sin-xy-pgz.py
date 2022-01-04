import math
import random

import pgzrun
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

ampl = Vector2(random.randint(100, 120), random.randint(100, 120))
period = Vector2(random.randint(100, 120), random.randint(100, 120))
frame_count = 0

def update():
    global frame_count
    frame_count += 1


def draw():
    screen.fill((0, 0, 0))

    x = ampl.x * math.sin(2 * math.pi * frame_count / period.x)
    y = ampl.y * math.sin(2 * math.pi * frame_count / period.y)

    screen.draw.line(start=(X0, Y0), end=(X0 + x, Y0 + y), color=(255, 255, 255))
    screen.draw.filled_circle(pos=(X0 + x, Y0 + y), radius=10, color=(0, 255, 255))
    # screen.draw.circle(pos=(WIDTH//2, HEIGHT//2), radius=10, color=(255, 222, 255))

pgzrun.go()

