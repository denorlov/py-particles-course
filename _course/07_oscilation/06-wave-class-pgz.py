import math
import random

import pgzrun
from pygame.math import Vector2 as vec

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Wave:
    def __init__(self, pos, amp, period):
        self.particles = [
            Oscillator(
                pos=vec(pos.x + i * 10 - 100, pos.y),
                ampl=vec(0, amp),
                period=vec(1, period))
            for i in range(150)
        ]

    def draw(self):
        for p in self.particles:
            p.draw()

    def update(self):
        for p in self.particles:
            p.update()

class Oscillator:
    def __init__(self, pos, ampl, period):
        self.pos = pos
        self.ampl = ampl
        self.period = period
        self.lifetime = 0

    def update(self):
        self.lifetime += 1
        #print(self.lifetime)

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

wave = Wave(pos=vec(0, Y0+20), amp=15, period=100)
wave2 = Wave(pos=vec(0, Y0-20), amp=15, period=200)

def update():
    wave.update()
    wave2.update()

def draw():
    screen.fill((0, 0, 0))
    wave.draw()
    wave2.draw()

pgzrun.go()

