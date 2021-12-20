# Encapsulate the above examples into a Wave class and create a sketch that displays two waves
# (with different amplitudes/periods) as in the screenshot below.
# Move beyond plain circles and lines and try visualizing the wave in a more creative way.

import math

import pgzrun
from pygame.math import Vector2 as vec

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
        y = self.ampl.y * math.sin(2 * math.pi * (self.lifetime + self.pos.x) / self.period.y)

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
    Oscillator(pos=vec(i * 10 - 100, Y0), ampl=vec(0, 10), period=vec(1, 200))
    for i in range(150)
]

def update():
    for p in particles:
        p.update()

def draw():
    screen.fill((0, 0, 0))

    for p in particles:
        p.draw()

pgzrun.go()

