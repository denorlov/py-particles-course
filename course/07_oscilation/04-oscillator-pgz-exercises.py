# Try initializing each Oscillator object with velocities and amplitudes that are not random
# to create some sort of regular pattern.
# Can you make the oscillators appear to be the legs of a insect-like creature?

import math
import random

import pgzrun
from pygame.math import Vector2 as Vec

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Oscillator:
    def __init__(self, pos, ampl, period):
        self.pos = pos
        self.ampl = ampl
        self.period = period
        self.lifetime = 0

    def update(self):
        self.lifetime += 1
        print(self.lifetime)

    def draw(self):
        x = self.ampl.x * math.sin(2 * math.pi * self.lifetime / self.period.x)
        y = self.ampl.y * math.sin(2 * math.pi * self.lifetime / self.period.y)

        screen.draw.line(
            start=self.pos, end=(self.pos.x + x, self.pos.y + y),
            color=(255, 255, 255)
        )
        screen.draw.circle(
            pos=(self.pos.x + x, self.pos.y + y),
            radius=5,
            color=(255, 255, 0)
        )
        screen.draw.circle(
            pos=(self.pos.x + x, self.pos.y + y),
            radius=7,
            color=(128, 128, 0)
        )
        # screen.draw.circle(pos=(WIDTH//2, HEIGHT//2), radius=10, color=(255, 222, 255))


particles = [
    Oscillator(
        pos=Vec(X0 + i * 10 - 100, Y0 + i * 10 - 100),
        ampl=Vec(random.randint(100, 120), random.randint(100, 120)),
        period=Vec(random.randint(100, 120), random.randint(100, 120))
    ) for i in range(30)
]

def update():
    for p in particles:
        p.update()

def draw():
    screen.fill((0, 0, 0))

    for p in particles:
        p.draw()

pgzrun.go()

