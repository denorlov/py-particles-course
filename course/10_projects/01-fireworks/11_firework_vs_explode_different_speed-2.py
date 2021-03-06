import math
import random

import pgzrun
from pygame.constants import *
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Particle:
    def __init__(self, pos, velocity, is_firework=True, mass=1):
        self.pos = pos
        self.velocity = velocity
        self.acc = Vector2(0, 0)
        self.mass = mass
        self.is_firework = is_firework
        self.lifetime = 255

    def apply_force(self, force):
        self.acc += force / self.mass

    def is_alive(self):
        return self.lifetime > 0

    def update(self):
        self.lifetime -= 1

        if self.is_alive():
            self.velocity += self.acc
            if not self.is_firework:
                self.velocity = self.velocity * 0.9
                self.lifetime -= 4
            self.pos += self.velocity

            self.acc = Vector2(0, 0)

    def draw(self):
        if self.is_alive():
            if self.is_firework:
                color = (0, 255, 0)
            else:
                color = (0, 255 / (255 / self.lifetime), 0)
            screen.draw.filled_circle(pos=self.pos, radius=2, color=color)
            # screen.draw.text(f"life:{self.lifetime}", self.pos)
            # screen.draw.text(f"vel:{self.velocity}", self.pos + Vector2(0, 10))

def random_vector():
    angle = random.uniform(0, 2.0 * math.pi)
    rnd_vec = Vector2(math.cos(angle), math.sin(angle))
    rnd_vec.normalize_ip()
    return rnd_vec

GRAVITY_FORCE = Vector2(0, 0.2)

class Firework:

    def __init__(self, pos:Vector2):
        self.firework = Particle(pos=Vector2(pos), velocity=Vector2(0, random.randint(-12, -8)))
        self.is_exploded = False
        self.particles = []

    def update(self):
        if not self.is_exploded:
            self.firework.apply_force(GRAVITY_FORCE)
            self.firework.update()
            if self.firework.velocity.y > 0 and not self.is_exploded:
                self.is_exploded = True
                self.explode()
        for p in self.particles:
            p.apply_force(GRAVITY_FORCE)
            p.update()

    def draw(self):
        if not self.is_exploded:
            self.firework.draw()
        for p in self.particles:
            p.draw()

    def explode(self):
        for i in range(50):
            velocity:Vector2 = random_vector() * random.randint(2, 10)
            self.particles.append(Particle(pos=Vector2(self.firework.pos), velocity=velocity, is_firework=False))


fireworks = []


def update():
    for firework in fireworks:
        firework.update()

    if random.randint(0, 100) > 95:
        fireworks.append(Firework(Vector2(random.randint(0, WIDTH), HEIGHT - 10)))

def draw():
    screen.surface.fill((0, 0, 0, 25), special_flags=BLEND_RGBA_MULT)
    screen.draw.text(f"fireworks:{len(fireworks)}", (10, 10))

    for firework in fireworks:
        firework.draw()

pgzrun.go()
