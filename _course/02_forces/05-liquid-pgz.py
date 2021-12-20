import math
import random

import pgzrun
import pygame
from pgzero.constants import mouse
from pgzero.rect import Rect
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Liquid:
    def __init__(self, rect, c):
        self.rect = rect
        self.c = c

    def draw(self):
        screen.draw.filled_rect(self.rect, color=(0,0,255))

    def update(self):
        pass


class Particle:
    def __init__(self, pos, velocity, acc, top_velocity_limit, mass):
        self.pos = pos
        self.velocity = velocity
        self.acc = acc
        self.top_velocity_limit = top_velocity_limit
        self.mass = mass

    def apply_force(self, force):
        self.acc += force / self.mass

    def update(self):
        self.velocity += self.acc
        if self.velocity.length() > self.top_velocity_limit:
            self.velocity.scale_to_length(self.top_velocity_limit)

        self.pos += self.velocity

        if self.pos.x < 0:
            self.pos.x = WIDTH

        if self.pos.x > WIDTH:
            self.pos.x = 0

        if self.pos.y < 0 or self.pos.y > HEIGHT:
            self.velocity.y *= -1

        if self.pos.y < 0:
            self.pos.y = 0

        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT


        self.acc = Vector2(0, 0)

    def draw(self):
        screen.draw.circle(pos=self.pos, radius=self.mass, color=(0, 255, 0))
        # screen.draw.line(self.pos, self.pos + self.velocity * 20, color=(0, 255, 0))
        # screen.draw.line(self.pos, self.pos + self.acc * 100, color=(255, 255, 0))
        # screen.draw.text(f"p:{self.pos}, v: {self.velocity}, a:{self.acc}", self.pos)

particles = [
    Particle(
        Vector2(random.randint(0, WIDTH), 0),
        Vector2(0, 0),
        Vector2(0, 0),
        10,
        random.randint(1,10)
    ) for _ in range(10)
]

liquid = Liquid(Rect(0, Y0, WIDTH, HEIGHT // 2), 0.01)

c = 0.01

def update():
    wind = Vector2(0.001, 0)
    for p in particles:
        p.apply_force(wind)

        gravity = Vector2(0, 0.1 * p.mass)
        p.apply_force(gravity)

        friction = p.velocity * -1
        if friction.magnitude() > 0:
            friction.normalize_ip()
            friction = friction * c
            p.apply_force(friction)

        p.update()

def draw():
    screen.fill((0, 0, 0))
    liquid.draw()
    for p in particles:
        p.draw()

pgzrun.go()

