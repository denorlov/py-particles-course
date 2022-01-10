import math
import random

import pgzrun
import pygame
from pgzero.constants import mouse
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Particle:
    def __init__(self, pos, velocity, acc, top_velocity_limit, mass):
        self.pos = pos
        self.velocity = velocity
        self.acc = acc
        self.top_velocity_limit = top_velocity_limit
        self.mass = mass

    def apply_force(self, force):
        self.acc += force / self.mass

    def update(self):
        self.velocity += self.acc
        if self.velocity.length() > self.top_velocity_limit:
            self.velocity.scale_to_length(self.top_velocity_limit)

        self.pos += self.velocity

        if self.pos.x < 0:
            self.pos.x = WIDTH

        if self.pos.x > WIDTH:
            self.pos.x = 0

        if self.pos.y < 0:
            self.pos.y = HEIGHT

        if self.pos.y > HEIGHT:
            self.velocity.y = -self.velocity.y

        self.acc = Vector2(0, 0)

    def draw(self):
        screen.draw.circle(pos=self.pos, radius=self.mass, color=(255, 255, 255))
        if draw_debug:
            screen.draw.line(self.pos, self.pos + self.velocity * 20, color=(0, 255, 255))
            screen.draw.text(f"{self.velocity}", (self.pos))

particles = []
for i in range(50):
    p = Particle(
        pos=Vector2(X0, Y0 + 200),
        velocity=Vector2(random.uniform(-1,1), random.uniform(-1,0)),
        acc=Vector2(-0.001, 0.01),
        top_velocity_limit=10,
        mass=random.randint(1, 20)
    )
    particles.append(p)

on_pause = False
draw_debug = False

def on_key_down(key):
    print(key)

    wind = Vector2(0,0)
    if key == keys.RIGHT:
        wind = Vector2(-0.5, 0)
    elif key == keys.LEFT:
        wind = Vector2(0.5, 0)

    if wind.length() > 0:
        for p in particles:
            p.apply_force(wind)

    global draw_debug
    if key == keys.D:
        draw_debug = not draw_debug

    global on_pause
    if key == keys.SPACE:
        on_pause = not on_pause

def on_mouse_down(button):
    if mouse.LEFT == button:
        wind = Vector2(0.5, 0)
    elif mouse.RIGHT == button:
        wind = Vector2(-0.5, 0)

    for p in particles:
        p.apply_force(wind)

def update():
    if on_pause:
        return

    gravity = Vector2(0, 0.01)

    for p in particles:
        p.apply_force(gravity)
        p.update()

def draw():
    screen.fill((0, 0, 0))
    for p in particles:
        p.draw()

pgzrun.go()

