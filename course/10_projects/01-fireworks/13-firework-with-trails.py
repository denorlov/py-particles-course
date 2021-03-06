import math
import random

import pgzrun
import pygame
from pygame.constants import *
from pygame.math import Vector2
from pygame.surface import Surface

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

is_in_full_screen = False

def on_key_down(key):
    global is_in_full_screen

    if key == keys.F:
        is_in_full_screen = not is_in_full_screen
        if is_in_full_screen:
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        else:
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))

class Particle:
    def __init__(self, pos, velocity, is_firework=True, mass=1):
        self.pos = pos
        self.velocity = velocity
        self.acc = Vector2(0, 0)
        self.mass = mass
        self.is_firework = is_firework
        self.lifetime = 255

    def apply_force(self, force):
        self.acc += force / self.mass

    def is_alive(self):
        return self.lifetime > 0

    def update(self):
        self.lifetime -= 1

        if self.is_alive():
            self.velocity += self.acc
            if not self.is_firework:
                self.velocity = self.velocity * 0.9
                self.lifetime -= 4
            self.pos += self.velocity

            self.acc = Vector2(0, 0)

    def draw(self, surface:Surface):
        if self.is_alive():
            if self.is_firework:
                color = (0, 255, 0)
            else:
                color = (0, 255 / (255 / self.lifetime), 0)
            pygame.draw.circle(surface, center=self.pos, radius=2, color=color)
            # screen.draw.text(f"life:{self.lifetime}", self.pos)
            # screen.draw.text(f"vel:{self.velocity}", self.pos + Vector2(0, 10))

def random_vector():
    angle = random.uniform(0, 360)
    return Vector2(1, 0).rotate(angle)

GRAVITY_FORCE = Vector2(0, 0.2)

class Firework:

    def __init__(self, pos:Vector2):
        self.firework = Particle(pos=Vector2(pos), velocity=Vector2(0, random.randint(-12, -8)))
        self.is_exploded = False
        self.particles = []

    def update(self):
        if not self.is_exploded:
            self.firework.apply_force(GRAVITY_FORCE)
            self.firework.update()
            if self.firework.velocity.y > 0 and not self.is_exploded:
                self.is_exploded = True
                self.explode()
        for p in self.particles:
            p.apply_force(GRAVITY_FORCE)
            p.update()

    def draw(self, surface:Surface):
        if not self.is_exploded:
            self.firework.draw(surface)
        for p in self.particles:
            p.draw(surface)

    def explode(self):
        for i in range(50):
            velocity:Vector2 = random_vector() * random.randint(2, 10)
            p = Particle(
                pos=Vector2(self.firework.pos),
                velocity=velocity,
                is_firework=False
            )
            self.particles.append(p)


fireworks = []


def update():
    for firework in fireworks:
        firework.update()

    if random.randint(0, 100) > 90:
        fireworks.append(Firework(Vector2(random.randint(0, WIDTH), HEIGHT - 10)))

surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

def draw():
    surface.fill((0, 0, 0, 25))
    screen.draw.text(f"fireworks:{len(fireworks)}", (10, 10))

    for firework in fireworks:
        firework.draw(surface)

    screen.blit(surface, pos=(0, 0))

pgzrun.go()
