import random

import pgzrun
import pygame
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
        self.lifetime = 255

    def apply_force(self, force):
        self.acc += force / self.mass

    def is_alive(self):
        return self.lifetime > 0

    def update(self):
        self.lifetime -= 2

        self.velocity += self.acc
        if self.velocity.length() > self.top_velocity_limit:
            self.velocity.scale_to_length(self.top_velocity_limit)

        self.pos += self.velocity

    def draw(self):
        screen.draw.filled_circle(pos=self.pos, radius=self.mass, color=(0, 255 / (255 / self.lifetime), 0))
        # screen.draw.line(self.pos, self.pos + self.velocity * 20, color=(0, 255, 0))
        # screen.draw.line(self.pos, self.pos + self.acc * 100, color=(255, 255, 0))
        # screen.draw.text(f"{self.lifetime}", self.pos)

class ParticlesSytem:
    def __init__(self, origin:Vector2):
        self.origin = origin
        self.particles = [self.create_particle() for _ in range(10)]

    def create_particle(self) -> Particle:
        return Particle(
            pos=Vector2(self.origin),
            velocity=Vector2(random.uniform(-1, 1), random.uniform(-5, 0)),
            acc=Vector2(0, 0.05),
            top_velocity_limit=10,
            mass=random.randint(1, 10)
        )

    def update(self):
        self.particles.append(self.create_particle())

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

ps = ParticlesSytem(Vector2(X0 - 150, Y0 + 100))
ps1 = ParticlesSytem(Vector2(X0, Y0 + 100))
ps2 = ParticlesSytem(Vector2(X0 + 150, Y0 + 100))

def update():
    ps.update()
    ps.origin = Vector2(pygame.mouse.get_pos())
    ps1.update()
    ps2.update()

def draw():
    screen.fill((0, 0, 0))
    ps.draw()
    ps1.draw()
    ps2.draw()

pgzrun.go()
