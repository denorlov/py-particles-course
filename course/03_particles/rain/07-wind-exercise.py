# Добавьте ветер. Т.е. реализуйте эффект косого дождя

import random

import pgzrun
import pygame
from pygame.math import Vector2

import course.util

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Particle:
    def __init__(self, pos):
        self.pos = pos
        self.acc = Vector2(0, 0.05)
        self.top_velocity_limit = 100
        self.mass = 1
        self.lifetime = 255
        self.z = random.randint(0, 20)
        self.length = course.util.linear(self.z, 0, 20, 10, 20)
        self.velocity = Vector2(0, course.util.linear(self.z, 0, 20, 4, 10))


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

        self.acc.update(0, 0)

    def draw(self):
        thick = course.util.linear(self.z, 0, 20, 1, 3)
        screen.draw.filled_rect(Rect(self.pos, (thick, self.length)), color=(255, 255, 255))

class RainSystem:
    def __init__(self):
        self.particles = [self.create_particle() for _ in range(10)]

    def create_particle(self) -> Particle:
        return Particle(
            pos=Vector2(random.randint(0, WIDTH), random.randint(-200, -10)),
        )

    def update(self):
        wind = Vector2(-0.1, 0)
        gravity = Vector2(0, 0.05)

        self.particles.extend([self.create_particle() for _ in range(2)])

        to_delete = []
        for p in self.particles:
            if p.is_alive():
                p.apply_force(wind)
                p.apply_force(gravity)
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
