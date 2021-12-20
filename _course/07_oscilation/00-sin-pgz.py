import math
import random

import pgzrun

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

ampl = 100
period = 120
frame_count = 0

def update():
    global frame_count
    frame_count += 1
    print(frame_count)

def draw():
    screen.fill((0, 0, 0))

    x = ampl * math.sin(2 * math.pi * frame_count / period)

    screen.draw.line(start=(X0, Y0), end=(X0 + x, Y0), color=(255, 255, 255))
    screen.draw.circle(pos=(X0 + x, Y0), radius=10, color=(0, 0, 255))
    screen.draw.circle(pos=(X0, Y0), radius=10, color=(255, 222, 255))

pgzrun.go()

