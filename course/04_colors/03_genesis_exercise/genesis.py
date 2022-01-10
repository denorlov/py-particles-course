import random

import pgzrun
import pygame

from pygame.math import Vector2
from pygame.surface import Surface
from course.util import *

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

is_in_full_screen = False
is_in_pause = False

def on_key_down(key):
    global is_in_pause, is_in_full_screen

    if key == keys.SPACE:
        is_in_pause = not is_in_pause

    if key == keys.F:
        is_in_full_screen = not is_in_full_screen
        if is_in_full_screen:
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        else:
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))


class Particle:
    def __init__(self, pos):
        self.pos = pos
        self.acc = Vector2(0, 0)
        self.velocity = Vector2(
            random.uniform(-0.3, 0.3),
            random.uniform(-0.3, 0.3)
        )
        self.lifetime = 255

    def apply_force(self, force):
        self.acc += force / self.mass

    def is_alive(self):
        return self.lifetime > 0

    def update(self):
        if self.is_alive():
            self.lifetime -= 3
            self.velocity += self.acc
            self.pos += self.velocity

    def draw(self, surface: Surface):
        if self.is_alive():
            color = (255 / (255 / self.lifetime), 255 / (255 / self.lifetime), 0)
            pygame.draw.circle(surface, center=self.pos, radius=2, color=color)
            # screen.draw.text(f"life:{self.lifetime}", self.pos)
            # screen.draw.text(f"vel:{self.velocity}", self.pos + Vector2(0, 10))


class Genesis:
    def __init__(self, origin: Vector2):
        self.origin = origin
        self.radius = 0
        self.particles = []

    def update(self):
        self.radius += 1
        if self.radius > 300:
            self.radius = 0

        self.generate_particles(self.radius)

        to_delete = []

        for p in self.particles:
            p.update()
            if not p.is_alive():
                to_delete.append(p)

        self.particles[:] = [p for p in self.particles if p not in to_delete]

    def draw(self, surface: Surface):
        for p in self.particles:
            p.draw(surface)

    def generate_particles(self, radius):
        for i in range(15):
            relative_pos: Vector2 = random_vector() * random.randint(radius - 2, radius + 2)
            p = Particle(self.origin + relative_pos)
            self.particles.append(p)

genesis = Genesis(Vector2(X0, Y0))

def update():
    if is_in_pause:
        return

    genesis.update()

def draw():
    screen.fill((0, 0, 0))
    screen.draw.text(f"particles:{len(genesis.particles)}", (10, 10))
    genesis.draw(screen.surface)

pgzrun.go()
