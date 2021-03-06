import random

import pgzrun
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Particle:
    def __init__(self, pos, velocity, mass=1):
        self.pos = pos
        self.velocity = velocity
        self.acc = Vector2(0, 0)
        self.mass = mass
        self.lifetime = 255

    def apply_force(self, force):
        self.acc += force / self.mass

    def is_alive(self):
        return self.lifetime > 0

    def update(self):
        self.lifetime -= 1

        if self.is_alive():
            self.velocity += self.acc
            self.pos += self.velocity

    def draw(self):
        if self.is_alive():
            screen.draw.filled_circle(pos=self.pos, radius=2, color=(0, 255 / (255 / self.lifetime), 0))
            # screen.draw.line(self.pos, self.pos + self.velocity * 20, color=(0, 255, 0))
            # screen.draw.line(self.pos, self.pos + self.acc * 100, color=(255, 255, 0))
            screen.draw.text(f"{self.lifetime}", self.pos)

class ParticlesSytem:
    def __init__(self, pos:Vector2):
        self.origin = pos
        self.particle = Particle(pos=Vector2(self.origin), velocity=Vector2(0, -4))

    def update(self):
        self.particle.update()

    def draw(self):
        self.particle.draw()
        screen.draw.text(f"{self.origin}", (0, 10))

ps = ParticlesSytem(Vector2(random.randint(0, WIDTH), HEIGHT - 10))

def update():
    ps.update()

def draw():
    screen.fill((0, 0, 0))
    ps.draw()

pgzrun.go()
