import math
import random

import pgzrun
import pygame
from pgzero.constants import mouse
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

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

        self.acc = Vector2(0, 0)

    def draw(self):
        screen.draw.circle(pos=self.pos, radius=self.mass, color=(255, 255, 0))
        screen.draw.line(self.pos, self.pos + self.velocity * 20, color=(255, 255, 0))
        screen.draw.line(self.pos, self.pos + self.acc * 100, color=(255, 255, 0))
        #screen.draw.text(f"p:{self.pos}, v: {self.velocity}, a:{self.acc}", self.pos)

particles = [
    Particle(
        Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
        Vector2(0, 0),
        Vector2(0, 0),
        10,
        random.randint(1, 20)
    ) for _ in range(30)
]

def update():
    wind = Vector2(0.01, 0)
    gravity = Vector2(0, 0.1)
    for p in particles:
        p.apply_force(gravity)
        p.apply_force(wind)
        p.update()

def draw():
    screen.fill((0, 0, 0))
    for p in particles:
        p.draw()

pgzrun.go()

