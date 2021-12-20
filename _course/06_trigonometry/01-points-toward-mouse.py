import math
import random

import pgzrun
import pygame
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Particle:
    def __init__(self, pos, velocity, acc, top_velocity_limit):
        self.pos = pos
        self.velocity = velocity
        self.acc = acc
        self.top_velocity_limit = top_velocity_limit

    def update(self):
        mouse_vec = Vector2(pygame.mouse.get_pos())
        self.acc = mouse_vec - self.pos
        self.acc.normalize_ip()
        self.acc = self.acc / 5

        self.velocity += self.acc
        if self.velocity.length() > self.top_velocity_limit:
            self.velocity.scale_to_length(self.top_velocity_limit)

        self.pos += self.velocity

        if self.pos.x < 0:
            self.pos.x = WIDTH

        if self.pos.x > WIDTH:
            self.pos.x = 0

        if self.pos.y < 0:
            self.pos.y = HEIGHT

        if self.pos.y > HEIGHT:
            self.pos.y = 0

    def draw(self):
        angle = math.atan(self.velocity.y/self.velocity.x)
        # screen.draw.circle(pos=self.pos, radius=10, color=(0, 255, 0))
        width = 5
        height = 20
        x, y = rotate((self.pos.x, self.pos.y), (self.pos.x - height, self.pos.y - width), angle)
        x1, y1 = rotate((self.pos.x, self.pos.y), (self.pos.x + height, self.pos.y - width), angle)
        x2, y2 = rotate((self.pos.x, self.pos.y), (self.pos.x + height, self.pos.y + width), angle)
        x3, y3 = rotate((self.pos.x, self.pos.y), (self.pos.x - height, self.pos.y + width), angle)

        screen.draw.circle(pos=self.pos, radius=2, color=(0, 255, 0))

        screen.draw.line(start=(x, y), end=(x1, y1), color=(255, 255, 255))
        screen.draw.line(start=(x1, y1), end=(x2, y2), color=(255, 255, 255))
        screen.draw.line(start=(x2, y2), end=(x3, y3), color=(255, 255, 255))
        screen.draw.line(start=(x3, y3), end=(x, y), color=(255, 255, 255))

        screen.draw.text(f"anlge: {angle}", self.pos)



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


particles = [
    Particle(
        Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
        Vector2(0, 0),
        Vector2(-0.001, 0.01),
        10
    ) for _ in range(3)
]

def update():
    for p in particles:
        p.update()

def draw():
    screen.fill((0, 0, 0))
    for p in particles:
        p.draw()

pgzrun.go()

