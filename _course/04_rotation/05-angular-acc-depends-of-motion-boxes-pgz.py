import math
import random

import pgzrun
import pygame
from pygame.math import Vector2 as Vec

WIDTH = 1200
HEIGHT = 1000

X0 = WIDTH // 2
Y0 = HEIGHT // 2


class Particle:
    def __init__(self, pos, acceleration, aAcceleration):
        self.pos = pos
        self.velocity = Vec(0, 0)
        self.acc = acceleration

        self.angle = 0
        self.aVelocity = 0
        self.aAcceleration = aAcceleration

    def update(self):
        self.velocity += self.acc
        self.pos += self.velocity

        if self.pos.x < 0:
            self.pos.x = 0

        if self.pos.y < 0:
            self.pos.y = 0

        if self.pos.x > WIDTH:
            self.pos.x = WIDTH

        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT

        self.aAcceleration = self.acc.x / 10
        self.aVelocity += constraint(self.aAcceleration, -0.1, 0.1)
        self.angle += self.aVelocity

        self.acc = Vec(0, 0)

    def draw(self):
        x, y = rotate((self.pos.x, self.pos.y), (self.pos.x - 20, self.pos.y - 20), math.radians(self.angle))
        x1, y1 = rotate((self.pos.x, self.pos.y), (self.pos.x + 20, self.pos.y - 20), math.radians(self.angle))
        x2, y2 = rotate((self.pos.x, self.pos.y), (self.pos.x + 20, self.pos.y + 20), math.radians(self.angle))
        x3, y3 = rotate((self.pos.x, self.pos.y), (self.pos.x - 20, self.pos.y + 20), math.radians(self.angle))

        screen.draw.circle(pos=self.pos, radius=2, color=(0, 255, 0))

        screen.draw.line(start=(x, y), end=(x1, y1), color=(255, 255, 255))
        screen.draw.line(start=(x1, y1), end=(x2, y2), color=(255, 255, 255))
        screen.draw.line(start=(x2, y2), end=(x3, y3), color=(255, 255, 255))
        screen.draw.line(start=(x3, y3), end=(x, y), color=(255, 255, 255))


def constraint(distance, bottom, top):
    if distance < bottom:
        distance = bottom
    elif distance > top:
        distance = top
    return distance


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

p = Particle(Vec(X0, Y0), Vec(0.01, 0.01), 0.01)

def update():
    mx, my = pygame.mouse.get_pos()
    p.acc = Vec((mx - p.pos.x) / 1000, (my - p.pos.y) / 1000)
    p.update()

def draw():
    screen.fill((0, 0, 0))
    screen.draw.text(f"pos: {p.pos}", (10, 10))
    screen.draw.text(f"vel: {p.velocity}", (10, 30))
    screen.draw.text(f"acc: {p.acc}", (10, 50))
    p.draw()

pgzrun.go()

