# Try creating your own textures for different types of effects.
# Can you make it look like fire, instead of smoke?

# Попробуйте поменять текстуру, которая использовалась в предыдущем примере.
# Попробуйте сделать огонь вместо дыма.

import random

import pgzrun
import pygame
from pygame.constants import BLEND_RGBA_ADD

from course import util
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2
G = 0.4

image = pygame.image.load("../assets/fire.png").convert_alpha()
image = pygame.transform.smoothscale(image, (100, 100))

bg = pygame.image.load('../assets/autumn_forest.jpg')

class Particle:
    def __init__(self, pos, velocity, acc, top_velocity_limit, mass=1):
        self.pos = pos
        self.velocity = velocity
        self.acc = acc
        self.top_velocity_limit = top_velocity_limit
        self.mass = mass
        self.lifetime = 255

    def apply_force(self, force):
        self.acc += force / self.mass

    def is_alive(self):
        return self.lifetime > 0

    def update(self):
        self.lifetime -= 2.5

        self.velocity += self.acc
        if self.velocity.length() > self.top_velocity_limit:
            self.velocity.scale_to_length(self.top_velocity_limit)

        self.pos += self.velocity

        self.acc = Vector2()

    def draw(self):
        # color = (255 / (255 / self.lifetime), 255 / (255 / self.lifetime), 255 / (255 / self.lifetime))
        #screen.draw.filled_circle(pos=self.pos, radius=16, color=color)
        image_copy = image.copy()
        image_copy.set_alpha(self.lifetime)
        screen.surface.blit(image_copy, self.pos, special_flags=BLEND_RGBA_ADD)
        # screen.draw.text(f"{self.lifetime}", self.pos)


class ParticlesSytem:
    def __init__(self, origin: Vector2):
        self.origin = origin
        self.particles = [self.create_particle() for _ in range(10)]

    def create_particle(self) -> Particle:
        pos = Vector2(self.origin + Vector2(random.gauss(0, 1) * 10, 0))

        vx = random.gauss(0, 1) * 0.1
        vy = random.gauss(0, 1) * 0.3 - 1
        velocity = Vector2(vx, vy)

        return Particle(pos, velocity, acc=Vector2(0, 0), top_velocity_limit=100)

    def apply_force(self, force:Vector2):
        for p in self.particles:
            p.apply_force(force)

    def apply_weight_force(self, gravity):
        for p in self.particles:
            force = gravity * p.mass
            p.apply_force(force)

    def update(self):
        self.particles.append(self.create_particle())

        to_delete = []
        for p in self.particles:
            if p.is_alive():
                p.update()
            else:
                to_delete.append(p)

        self.particles[:] = [p for p in self.particles if p not in to_delete]

    def draw(self):
        for p in self.particles:
            if p.is_alive():
                p.draw()

ps = ParticlesSytem(Vector2(X0 - 200, Y0 + 160))

def update():
    mx, my = pygame.mouse.get_pos()
    dx = util.linear_with_ranges(mx, (0, WIDTH), (-0.2, 0.2))
    wind = Vector2(dx, 0)
    ps.apply_force(wind)

    # gravity = Vector2(0, 0.1)
    # ps.apply_weight_force(gravity)
    ps.update()

def draw():
    screen.blit(bg, (0, 0))
    screen.draw.text(f"particles:{len(ps.particles)}", (0, 0))

    ps.draw()

pgzrun.go()
