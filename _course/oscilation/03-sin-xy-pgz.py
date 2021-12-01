import math
import random

import pgzrun
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

ampl = Vector2(random.randint(100, 120), random.randint(100, 120))
period = Vector2(random.randint(100, 120), random.randint(100, 120))
frame_count = 0

def update():
    global frame_count
    frame_count += 1
    print(frame_count)

def draw():
    print(frame_count)
    screen.fill((0, 0, 0))

    x = ampl.x * math.sin(2 * math.pi * frame_count / period.x)
    y = ampl.y * math.sin(2 * math.pi * frame_count / period.y)

    screen.draw.line(start=(WIDTH//2, HEIGHT//2), end=(WIDTH//2 + x, HEIGHT//2 + y), color=(255, 255, 255))
    screen.draw.circle(pos=(WIDTH//2 + x, HEIGHT//2 + y), radius=10, color=(0, 0, 255))
    # screen.draw.circle(pos=(WIDTH//2, HEIGHT//2), radius=10, color=(255, 222, 255))

pgzrun.go()

