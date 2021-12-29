import random

import pgzrun
import pygame

from _course import util
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2
G = 0.4

bg = pygame.image.load('../assets/autumn_forest.jpg')

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

        self.acc = Vector2()

    def draw(self):
        color = (255 / (255 / self.lifetime), 255 / (255 / self.lifetime), 255 / (255 / self.lifetime))
        screen.draw.filled_circle(pos=self.pos, radius=10, color=color)
        # screen.draw.line(self.pos, self.pos + self.velocity * 20, color=(0, 255, 0))
        # screen.draw.line(self.pos, self.pos + self.acc * 100, color=(255, 255, 0))
        # screen.draw.text(f"{self.lifetime}", self.pos)


class ParticlesSytem:
    def __init__(self, origin: Vector2):
        self.origin = origin
        self.particles = [self.create_particle() for _ in range(200)]

    def create_particle(self) -> Particle:
        vx = random.gauss(0, 1) * 0.3
        vy = random.gauss(0, 1) * 0.3 - 1
        return Particle(
            pos=Vector2(self.origin),
            velocity=Vector2(vx, vy),
            acc=Vector2(0, 0),
            top_velocity_limit=100,
            mass=1
        )

    def apply_force(self, force:Vector2):
        for p in self.particles:
            p.apply_force(force)

    def apply_weight_force(self, gravity):
        for p in self.particles:
            force = gravity * p.mass
            p.apply_force(force)

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

ps = ParticlesSytem(Vector2(X0 + 50, Y0 + 200))

def update():
    mx, my = pygame.mouse.get_pos()
    dx = util.linear_with_ranges(mx, (0, WIDTH), (-0.2, 0.2))
    wind = Vector2(dx, 0)
    ps.apply_force(wind)

    # gravity = Vector2(0, 0.1)
    # ps.apply_weight_force(gravity)
    ps.update()

def draw():
    #screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.draw.text(f"particles:{len(ps.particles)}", (0, 0))
    ps.draw()

pgzrun.go()
