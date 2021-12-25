# 1) реализуйте функцию limit(vector, max_magnitude),
# которая принимает в качестве аргумента vector и возвращает вектор с совпадающим направлением
# и длинной ограниченной max_magnitude
# 2) добавьте в пример шарика движущегося с ускорением ограничение по скорости

import math
import random

import pgzrun
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2


def limit(velocity:Vector2, max_magnitude) -> Vector2:
    print(f"velocity:{velocity}, max_mag: {max_magnitude}")
    if velocity.magnitude() > max_magnitude:
        return velocity.normalize() * max_magnitude
    else:
        return velocity


class Particle:
    def __init__(self, pos, velocity, acc, topspeed):
        self.pos = pos
        self.velocity = velocity
        self.acc = acc
        self.topspeed = topspeed

    def update(self):
        self.pos += self.velocity
        self.velocity += self.acc
        self.velocity = limit(self.velocity, self.topspeed)

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
        screen.draw.line(self.pos, self.pos + self.velocity * 10, color=(0, 255, 0))
        screen.draw.line(self.pos, self.pos + self.acc * 20, color=(255, 255, 0))
        screen.draw.text(f"v:{self.velocity}, a:{self.acc}", self.pos)

particles = [
    Particle(
        pos=Vector2(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
        velocity=Vector2(0, 0),
        acc=Vector2(-0.001, 0.01),
        topspeed=10
    ) for _ in range(5)
]

def update():
    for p in particles:
        p.update()

def draw():
    screen.fill((0, 0, 0))
    for p in particles:
        p.draw()

pgzrun.go()

