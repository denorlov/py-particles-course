# Blending modes description:
# https://github.com/atizo/pygame/blob/master/src/surface.h

import random

import pgzrun
import pygame

import util
from pgzero.constants import mouse
from pygame.math import Vector2
from pygame.constants import *
WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2
G = 0.4

bg = pygame.image.load('../assets/autumn_forest.jpg')

image = pygame.image.load("../assets/texture.png").convert_alpha()

# color to tint
R, G, B = 255, 0, 0
# This causes that the all the pixels of the image are multiplied by the color,
# rather then set by the color:
image.fill((R, G, B, 255), None, special_flags=BLEND_RGBA_MULT)

class Particle:
    def __init__(self, pos, velocity, acc, top_velocity_limit, mass):
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
        screen.surface.blit(image_copy, self.pos)
        # screen.draw.text(f"{self.lifetime}", self.pos)


class ParticlesSytem:
    def __init__(self, origin: Vector2):
        self.origin = origin
        self.particles = [self.create_particle() for _ in range(200)]

    def create_particle(self) -> Particle:
        vx = random.gauss(0, 1) * 0.3
        vy = random.gauss(0, 1) * 0.3 - 1
        return Particle(
            pos=Vector2(self.origin),
            velocity=Vector2(vx, vy),
            acc=Vector2(0, 0),
            top_velocity_limit=100,
            mass=1
        )

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

ps = ParticlesSytem(Vector2(X0, Y0 + 200))

def update():
    mx, my = pygame.mouse.get_pos()
    dx = util.linear_with_ranges(mx, (0, WIDTH), (-0.2, 0.2))
    wind = Vector2(dx, 0)
    ps.apply_force(wind)

    # gravity = Vector2(0, 0.1)
    # ps.apply_weight_force(gravity)
    ps.update()

frame_count = 0

def draw():
    global frame_count
    frame_count += 1

    #screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    image_copy = image.copy()
    screen.surface.blit(image, (5, 50))

    image_copy.set_alpha(frame_count % 255)
    screen.surface.blit(image_copy, (50, 50))


    screen.draw.text(f"particles:{len(ps.particles)}", (0, 0))
    ps.draw()

pgzrun.go()
