# create a simulation of a car (or runner) that accelerates
# when you press the up key and brakes when you press the down key

# реализуйте симуляцию машины (или бегуна) которая ускоряется когда вы нажимаете кнопку Вверх
# и тормозит когда вы нажимаете клавишу Вниз

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
        self.pos += self.velocity
        self.velocity += self.acc

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

