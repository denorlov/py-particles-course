import math
import random

import pgzrun
import pygame
from pgzero.constants import mouse
from pgzero.rect import Rect
from pygame.math import Vector2

WIDTH = 1500
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
        self.lifetime = 255

    def apply_force(self, force):
        self.acc += force / self.mass

    def is_alive(self):
        return self.lifetime > 0

    def update(self):
        if not self.is_alive():
            return

        self.lifetime -= 1

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


    def draw(self):
        if self.is_alive():
            screen.draw.circle(pos=self.pos, radius=self.mass * 2, color=(0, 255 / (255/self.lifetime), 0))
            # screen.draw.line(self.pos, self.pos + self.velocity * 20, color=(0, 255, 0))
            # screen.draw.line(self.pos, self.pos + self.acc * 100, color=(255, 255, 0))
            #screen.draw.text(f"v: {self.velocity}, l:{self.lifetime}", self.pos)

particles = []

for _ in range(10):
    p = Particle(
        pos=Vector2(X0, Y0 - 100),
        velocity=Vector2(random.uniform(-1, 1), random.uniform(-2, 0)),
        acc=Vector2(0, 0.05),
        top_velocity_limit=10,
        mass=random.randint(5, 10)
    )
    particles.append(p)

def update():
    for p in particles:
        p.update()

def draw():
    screen.fill((0, 0, 0))
    for p in particles:
        p.draw()

pgzrun.go()

