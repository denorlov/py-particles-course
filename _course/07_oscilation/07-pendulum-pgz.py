import math
import random

import pgzrun
from pygame.math import Vector2 as vec

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Pendulum:
    def __init__(self, pos, r, angle):
        self.pos = pos
        self.r = r
        self.angle = angle
        self.aVelocity = 0
        self.aAcc = 0
        self.lifetime = 0

    def update(self):
        self.lifetime += 1

        gravity = 0.004

        self.aAcc = -1 * gravity * math.sin(self.angle)
        self.aVelocity += self.aAcc
        self.angle += self.aVelocity

    def draw(self):
        location = self.pos + vec(math.sin(self.angle), math.cos(self.angle)) * self.r
        screen.draw.line(start=self.pos, end=location, color=(255, 255, 255))
        screen.draw.circle(pos=location, radius=5, color=(0, 255, 0))
        screen.draw.circle(pos=location, radius=3, color=(0, 128, 0))

p = Pendulum(pos=(X0, Y0), r=100, angle=math.pi/4)

def update():
    p.update()

def draw():
    screen.fill((0, 0, 0))
    p.draw()

pgzrun.go()

