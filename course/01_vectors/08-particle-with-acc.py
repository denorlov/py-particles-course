import math
import random

import pgzrun
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Particle:
    def __init__(self, pos, velocity, acc):
        self.pos = pos
        self.velocity = velocity
        self.acc = acc

    def update(self):
        self.pos = self.pos + self.velocity
        self.velocity = self.velocity + self.acc

        if self.pos.x < 0 or self.pos.x > WIDTH:
            self.velocity.x = self.velocity.x * -1

        if self.pos.y < 0 or self.pos.y > HEIGHT:
            self.velocity.y = self.velocity.y * -1

    def draw(self):
        screen.draw.circle(pos=self.pos, radius=10, color=(0, 255, 0))
        screen.draw.line(self.pos, self.pos + self.velocity * 20, color=(0, 255, 0))
        screen.draw.line(self.pos, self.pos + self.acc * 20, color=(255, 255, 0))
        #screen.draw.text(f"p:{self.pos}, v: {self.velocity}, a:{self.acc}", self.pos)

particles = [
    Particle(
        Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
        Vector2(0, 0),
        Vector2(-0.001, 0.01),
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

