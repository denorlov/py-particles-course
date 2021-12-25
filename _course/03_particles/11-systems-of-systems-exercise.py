# Rewrite example so that each particle system doesn’t live forever.
# When a particle system is empty (i.e. has no particles left in its list),
# remove it from the list systems.

# Перепишете предыдущий пример. Нужно сделать так, что когда в системе частиц совсем не осталось,
# система частиц уничтожалась (т.е. удаляется из списка систем частиц).

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

particle_systems = [ParticlesSytem(Vector2(X0, Y0 + 100))]

def on_mouse_down(pos):
    particle_systems.append(ParticlesSytem(pos))

def update():
    for ps in particle_systems:
        ps.update()

def draw():
    screen.fill((0, 0, 0))
    for ps in particle_systems:
        ps.draw()

pgzrun.go()
