import math
import random

import pgzrun
import pygame
from pygame.constants import *
from pygame.math import Vector2
from pygame.surface import Surface

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

background = pygame.image.load("../../assets/night-city-light.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background.set_alpha(25)

is_in_full_screen = False

def on_key_down(key):
    global is_in_full_screen

    if key == keys.F:
        is_in_full_screen = not is_in_full_screen
        if is_in_full_screen:
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        else:
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))

class Particle:
    def __init__(self, pos, velocity, hue, is_firework=True, mass=1):
        self.pos = pos
        self.velocity = velocity
        self.acc = Vector2(0, 0)
        self.mass = mass
        self.is_firework = is_firework
        self.lifetime = 100
        self.hue = hue

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

    def draw(self, surface:Surface):
        if self.is_alive():
            if self.is_firework:
                color = pygame.Color(0, 0, 0, 0)
                color.hsva = (self.hue, 100, 100, 100)
            else:
                color = pygame.Color(0, 0, 0, 0)
                color.hsva = (self.hue, 100, 100, self.lifetime)
            pygame.draw.circle(surface, center=self.pos, radius=2, color=color)
            # screen.draw.text(f"life:{self.lifetime}", self.pos)
            # screen.draw.text(f"vel:{self.velocity}", self.pos + Vector2(0, 10))

def random_vector():
    angle = random.uniform(0, 2.0 * math.pi)
    rnd_vec = Vector2(math.cos(angle), math.sin(angle))
    rnd_vec.normalize_ip()
    return rnd_vec

GRAVITY_FORCE = Vector2(0, 0.2)

class Firework:

    def __init__(self, pos:Vector2, hue):
        self.firework = Particle(
            pos=Vector2(pos),
            velocity=Vector2(0, random.randint(-12, -8)),
            hue=hue
        )
        self.is_exploded = False
        self.particles = []
        self.hue = hue

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

    def draw(self, surface:Surface):
        if not self.is_exploded:
            self.firework.draw(surface)
        for p in self.particles:
            p.draw(surface)

    def explode(self):
        for i in range(50):
            velocity:Vector2 = random_vector() * random.randint(2, 10)
            p = Particle(
                pos=Vector2(self.firework.pos),
                velocity=velocity,
                is_firework=False,
                hue=self.hue
            )
            self.particles.append(p)


fireworks = []


def update():
    for firework in fireworks:
        firework.update()

    if random.randint(0, 100) > 90:
        f = Firework(
            pos=Vector2(random.randint(0, WIDTH), HEIGHT - 10),
            hue=random.randint(0, 360)
        )
        fireworks.append(f)

surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

def draw():
#    surface.fill((0, 0, 0, 25))
    surface.blit(background, (0, 0))

    screen.draw.text(f"fireworks:{len(fireworks)}", (10, 10))

    for firework in fireworks:
        firework.draw(surface)

    #screen.surface.fill((255, 255, 255, 25), special_flags=BLEND_RGBA_MULT)
    screen.blit(surface, pos=(0, 0))

pgzrun.go()
