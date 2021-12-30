import random

import pgzrun
import pygame
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Particle:
    def __init__(self, pos, velocity, acc, top_velocity_limit=100, mass=1, length = 10):
        self.pos = pos
        self.velocity = velocity
        self.acc = acc
        self.top_velocity_limit = top_velocity_limit
        self.mass = mass
        self.lifetime = 255
        self.length = length

    def apply_force(self, force):
        self.acc += force / self.mass

    def is_alive(self):
        return self.lifetime > 0

    def update(self):
        self.lifetime -= 1

        self.velocity += self.acc
        if self.velocity.length() > self.top_velocity_limit:
            self.velocity.scale_to_length(self.top_velocity_limit)

        self.pos += self.velocity

    def draw(self):
        screen.draw.line(self.pos, self.pos + Vector2(0, self.length), color=(0, 0, 255))

class RainSystem:
    def __init__(self):
        self.particles = [self.create_particle() for _ in range(20)]

    def create_particle(self) -> Particle:
        return Particle(
            pos=Vector2(random.randint(0, WIDTH), random.randint(-200, -10)),
            velocity=Vector2(0, 0),
            acc=Vector2(0, 0.05),
            length=random.randint(10, 20)
        )

    def update(self):
        self.particles.extend([self.create_particle() for _ in range(5)])

        to_delete = []
        for p in self.particles:
            if p.is_alive():
                p.update()
            else:
                to_delete.append(p)

        self.particles[:] = [p for p in self.particles if p not in to_delete]

    def draw(self):
        for p in self.particles:
            if p.is_alive():
                p.draw()

rain = RainSystem()

def update():
    rain.update()

def draw():
    screen.fill((0, 0, 0))
    screen.draw.text(f"particles:{len(rain.particles)}", (0, 0))
    rain.draw()

pgzrun.go()
