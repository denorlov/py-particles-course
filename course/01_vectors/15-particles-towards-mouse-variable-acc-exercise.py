# Try implementing the above example with a variable magnitude of acceleration,
# stronger when it is either closer or farther away.

# Перепишите предыдущую программу, так что величина вектора ускорения будет зависеть от того
# насколько частица далеко от курсора мыши.
# 1) Ускорение становиться сильнее, с приближением частицы к курсору
# 2) Ускорение становиться слабее, с приближением частицы к курсору

import math
import random

import pgzrun
import pygame
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Particle:
    def __init__(self, pos, velocity, acc, top_velocity_limit):
        self.pos = pos
        self.velocity = velocity
        self.acc = acc
        self.top_velocity_limit = top_velocity_limit

    def update(self):
        mouse_vec = Vector2(pygame.mouse.get_pos())
        self.acc = mouse_vec - self.pos
        self.acc.normalize_ip()
        self.acc = self.acc / 5

        self.velocity += self.acc
        if self.velocity.length() > self.top_velocity_limit:
            self.velocity.scale_to_length(self.top_velocity_limit)

        self.pos += self.velocity

        if self.pos.x < 0:
            self.pos.x = WIDTH

        if self.pos.x > WIDTH:
            self.pos.x = 0

        if self.pos.y < 0:
            self.pos.y = HEIGHT

        if self.pos.y > HEIGHT:
            self.pos.y = 0

    def draw(self):
        screen.draw.circle(pos=self.pos, radius=10, color=(0, 255, 0))
        #screen.draw.line(self.pos, self.pos + self.velocity * 20, color=(0, 255, 0))
        screen.draw.line(self.pos, self.pos + self.acc * 100, color=(255, 255, 0))
        #screen.draw.text(f"p:{self.pos}, v: {self.velocity}, a:{self.acc}", self.pos)

particles = [
    Particle(
        Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
        Vector2(0, 0),
        Vector2(-0.001, 0.01),
        10
    ) for _ in range(3)
]

def update():
    for p in particles:
        p.update()

def draw():
    screen.fill((0, 0, 0))
    for p in particles:
        p.draw()

pgzrun.go()

