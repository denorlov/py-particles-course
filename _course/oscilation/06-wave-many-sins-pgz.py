import math
import random

import pgzrun
from pygame.math import Vector2 as vec

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Wave:
    def __init__(self, pos):
        self.particles = [
            Oscillator(
                pos=vec(pos.x + i * 10 - 100, pos.y),
                ampl=vec(0, 5), period=vec(1, 120),
                ampl1=vec(0, 10), period1=vec(1, 200),
                ampl2=vec(0, 5), period2=vec(1, 220),
            )
            for i in range(150)
        ]

    def draw(self):
        for p in self.particles:
            p.draw()

    def update(self):
        for p in self.particles:
            p.update()

class Oscillator:
    def __init__(self, pos, ampl, period, ampl1, period1, ampl2, period2):
        self.pos = pos
        self.ampl = ampl
        self.ampl1 = ampl1
        self.ampl2 = ampl2
        self.period = period
        self.period1 = period1
        self.period2 = period2
        self.lifetime = 0

    def update(self):
        self.lifetime -= 2
        #print(self.lifetime)

    def draw(self):
        x = self.ampl.x * math.sin(2 * math.pi * self.lifetime / self.period.x)

        y = self.ampl.y * math.sin(2 * math.pi * (self.lifetime + self.pos.x) / self.period.y)
        y += self.ampl1.y * math.sin(2 * math.pi * (self.lifetime + self.pos.x) / self.period1.y)
        y += self.ampl2.y * math.sin(2 * math.pi * (self.lifetime + self.pos.x) / self.period2.y)

        # screen.draw.line(
        #     start=self.pos, end=(self.pos.x + x, self.pos.y + y),
        #     color=(255, 255, 255)
        # )
        screen.draw.circle(
            pos=(self.pos.x + x, self.pos.y + y),
            radius=5,
            color=(0, 255, 0)
        )
        screen.draw.circle(
            pos=(self.pos.x + x, self.pos.y + y),
            radius=3,
            color=(0, 128, 0)
        )
        # screen.draw.circle(pos=(WIDTH//2, HEIGHT//2), radius=10, color=(255, 222, 255))

wave = Wave(pos=vec(0, Y0+20))
wave2 = Wave(pos=vec(0, Y0-20))
wave3 = Wave(pos=vec(0, Y0+40))

def update():
    wave.update()
    wave2.update()
    wave3.update()

def draw():
    screen.fill((0, 0, 0))
    wave.draw()
    wave2.draw()
    wave3.draw()

pgzrun.go()

