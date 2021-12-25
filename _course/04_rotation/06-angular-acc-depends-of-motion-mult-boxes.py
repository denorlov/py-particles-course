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
    def __init__(self, pos, acceleration, aAcceleration, mass):
        self.pos = pos
        self.velocity = Vec(0, 0)
        self.acc = acceleration

        self.angle = 0
        self.aVelocity = 0
        self.aAcceleration = aAcceleration

        self.mass = mass

    def apply_force(self, force):
        self.acc += force / self.mass

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

        self.aAcceleration = constraint(self.acc.x, -0.1, 0.1)
        self.aVelocity += self.aAcceleration
        self.angle += self.aVelocity

        self.acc = Vec(0, 0)

    def draw(self):
        x, y = rotate((self.pos.x, self.pos.y), (self.pos.x - self.mass, self.pos.y - self.mass), math.radians(self.angle))
        x1, y1 = rotate((self.pos.x, self.pos.y), (self.pos.x + self.mass, self.pos.y - self.mass), math.radians(self.angle))
        x2, y2 = rotate((self.pos.x, self.pos.y), (self.pos.x + self.mass, self.pos.y + self.mass), math.radians(self.angle))
        x3, y3 = rotate((self.pos.x, self.pos.y), (self.pos.x - self.mass, self.pos.y + self.mass), math.radians(self.angle))

        screen.draw.circle(pos=self.pos, radius=2, color=(0, 255, 0))

        screen.draw.line(start=(x, y), end=(x1, y1), color=(255, 255, 255))
        screen.draw.line(start=(x1, y1), end=(x2, y2), color=(255, 255, 255))
        screen.draw.line(start=(x2, y2), end=(x3, y3), color=(255, 255, 255))
        screen.draw.line(start=(x3, y3), end=(x, y), color=(255, 255, 255))
        # screen.draw.text(f"v: {self.velocity}", self.pos)
        # screen.draw.text(f"aAcc:{self.aAcceleration}", self.pos + Vec(0, 20))


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


G = 0.4
class Attractor:
    def __init__(self, pos, mass):
        self.pos = pos
        self.mass = mass

    def draw(self):
        screen.draw.filled_circle(self.pos, radius=self.mass, color=(255, 255, 255))

    def attract(self, particle: Particle):
        # 1. cчитаем силу притяжения
        force_vec : Vector2 = self.pos - particle.pos
        distance = force_vec.magnitude()
        distance = constraint(distance, 5, 25)
        force_vec.normalize_ip()
        strenght = (G * self.mass * particle.mass) / (distance * distance)
        force_vec = force_vec * strenght
        # 2. применяем к частице
        particle.apply_force(force_vec)

attractor = Attractor(Vec(X0, Y0), 10)

particles = [
    Particle(
        pos=Vec(random.randint(0, WIDTH), random.randint(0, WIDTH)),
        acceleration=Vec(0, 0),
        aAcceleration=0.01,
        mass=random.randint(5, 10)
    ) for _ in range(50)
]

def update():
    for p in particles:
        attractor.attract(p)
        p.update()

def draw():
    screen.fill((0, 0, 0))
    attractor.draw()
    for p in particles:
        p.draw()

pgzrun.go()

