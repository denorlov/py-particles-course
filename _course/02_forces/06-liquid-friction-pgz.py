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


class Liquid:
    def __init__(self, rect, c):
        self.rect = rect
        self.c = c

    def draw(self):
        screen.draw.filled_rect(self.rect, color=(0, 0, 255))

    def is_inside(self, vector_pos: Vector2):
        return self.rect.collidepoint(vector_pos)

    def drag(self, particle: Particle):
        # считаем силу сопротивления воздуха
        vel = particle.velocity
        speed = vel.magnitude()
        drag_magnitude = self.c * speed * speed
        if drag_magnitude:
            drag_vec = vel * -1
            drag_vec.normalize_ip()
            drag_vec = drag_vec * drag_magnitude

            # применяем к частице
            particle.apply_force(drag_vec)

    def update(self):
        pass

particles = [
    Particle(
        Vector2(random.randint(0, WIDTH), 0),
        Vector2(0, 0),
        Vector2(0, 0),
        10,
        random.randint(1,10)
    ) for _ in range(10)
]

liquid = Liquid(Rect(0, Y0, WIDTH // 2, HEIGHT // 8), 0.1)
liquid1 = Liquid(Rect(WIDTH // 2, Y0 + HEIGHT // 4 + HEIGHT // 8, WIDTH, HEIGHT // 8), 0.1)

c = 0.01

def update():
    wind = Vector2(0.001, 0)
    for p in particles:
        p.apply_force(wind)

        gravity = Vector2(0, 0.1 * p.mass)
        p.apply_force(gravity)

        if liquid.is_inside(p.pos):
            liquid.drag(p)

        if liquid1.is_inside(p.pos):
            liquid1.drag(p)

        # friction = p.velocity * -1
        # if friction.magnitude() > 0:
        #     friction.normalize_ip()
        #     friction = friction * c
        #     p.apply_force(friction)

        p.update()

def draw():
    screen.fill((0, 0, 0))
    liquid.draw()
    liquid1.draw()
    for p in particles:
        p.draw()

pgzrun.go()

