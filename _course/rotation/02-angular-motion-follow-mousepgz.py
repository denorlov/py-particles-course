import math
import random

import pgzrun
import pygame

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

angle = 0
aVelocity = 0
aAcceleration = 0.1

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    return qx, qy

def update():
    global angle, aVelocity, aAcceleration
    angle += aVelocity
    aVelocity += aAcceleration

def draw():
    screen.fill((0, 0, 0))

    x0, y0 = pygame.mouse.get_pos()
    x, y = rotate((x0, y0), (x0, y0 + 100), math.radians(angle))
    x1, y1 = rotate((x0, y0), (x0, y0 - 100), math.radians(angle))

    screen.draw.circle(pos=(x, y), radius=10, color=(0, 255, 0))
    screen.draw.line(start=(x, y), end=(x1, y1), color=(255, 255, 255))
    screen.draw.circle(pos=(x1, y1), radius=10, color=(0, 255, 0))

pgzrun.go()

