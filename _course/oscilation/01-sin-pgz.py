import math
import random

import pgzrun

WIDTH = 1000
HEIGHT = 500

ampl = 100
period = 120
frame_count = 0

def update():
    global frame_count
    frame_count += 1
    print(frame_count)

def draw():
    print(frame_count)
    screen.fill((0, 0, 0))

    x = ampl * math.sin(2 * math.pi * frame_count / period)

    screen.draw.line(start=(WIDTH//2, HEIGHT//2), end=(WIDTH//2 + x, HEIGHT//2), color=(255, 255, 255))
    screen.draw.circle(pos=(WIDTH//2 + x, HEIGHT//2), radius=10, color=(0, 0, 255))
    screen.draw.circle(pos=(WIDTH//2, HEIGHT//2), radius=10, color=(255, 222, 255))

pgzrun.go()

