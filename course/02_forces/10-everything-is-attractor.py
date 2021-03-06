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
G = 0.4

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

    def attract(self, particle):
        # 1. cчитаем силу притяжения
        force_vec : Vector2 = self.pos - particle.pos
        distance = force_vec.magnitude()
        distance = constraint(distance, 5, 25)
        force_vec.normalize_ip()
        strenght = (G * self.mass * particle.mass) / (distance * distance)
        force_vec = force_vec * strenght
        # 2. применяем к частице
        particle.apply_force(force_vec)

    def draw(self):
        screen.draw.circle(pos=self.pos, radius=self.mass * 2, color=(0, 255, 0))
        # screen.draw.line(self.pos, self.pos + self.velocity * 20, color=(0, 255, 0))
        # screen.draw.line(self.pos, self.pos + self.acc * 100, color=(255, 255, 0))
        # screen.draw.text(f"p:{self.pos}, v: {self.velocity}, a:{self.acc}", self.pos)

def constraint(distance, bottom, top):
    if distance < bottom:
        distance = bottom
    elif distance > top:
        distance = top
    return distance


particles = [
    Particle(
        pos=Vector2(random.randint(0, WIDTH), random.randint(0, WIDTH)),
        velocity=Vector2(0, 0),
        acc=Vector2(0, 0),
        top_velocity_limit=10,
        mass=random.randint(1,10)
    ) for _ in range(10)
]

def update():
    for p in particles:
        for p1 in particles:
            if p != p1:
                p1.attract(p)

        p.update()

def draw():
    screen.fill((0, 0, 0))
    for p in particles:
        p.draw()

pgzrun.go()

