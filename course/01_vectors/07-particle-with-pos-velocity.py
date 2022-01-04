import math
import random

import pgzrun
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Particle:
    def __init__(self, pos, velocity):
        self.pos = pos
        self.velocity = velocity

    def update(self):
        self.pos += self.velocity

        if self.pos.x < 0 or self.pos.x > WIDTH:
            self.velocity.x = self.velocity.x * -1

        if self.pos.y < 0 or self.pos.y > HEIGHT:
            self.velocity.y = self.velocity.y * -1

    def draw(self):
        screen.draw.circle(pos=self.pos, radius=10, color=(0, 255, 0))
        screen.draw.text(f"p:{self.pos}, v: {self.velocity}", self.pos)

particles = [
    Particle(
        Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
        Vector2(random.randint(-2, 2), random.randint(-2, 2))
    ) for _ in range(20)
]

def update():
    for p in particles:
        p.update()

def draw():
    screen.fill((0, 0, 0))
    for p in particles:
        p.draw()

pgzrun.go()

