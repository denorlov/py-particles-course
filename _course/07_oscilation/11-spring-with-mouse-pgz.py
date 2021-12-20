import math

import pgzrun
from pygame.math import Vector2 as Vec

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

K = 0.1
C = 0.01

class Spring:
    def __init__(self, anchor_pos : Vec, bob_pos : Vec, mass):
        self.anchor_pos = anchor_pos
        self.pos = bob_pos
        self.rest_length = (anchor_pos - bob_pos).magnitude()
        self.velocity = Vec(0, 0)
        self.acc = Vec(0, 0)
        self.mass = mass

    def connect(self) -> Vec :
        force: Vec = self.pos - self.anchor_pos
        current_length = force.magnitude()
        x = current_length - self.rest_length
        force.normalize_ip()
        print(f"force before: {force}, {K}, {x}")
        force = force * -1 * K * x
        print(f"force after: {force}")
        return force

    def apply_force(self, force):
        self.acc += force / self.mass

    def update(self):
        self.velocity += self.acc
        self.pos += self.velocity
        self.acc = Vec(0, 0)

    def draw(self):
        screen.draw.line(start=self.anchor_pos, end=self.pos, color=(255, 255, 255))
        screen.draw.circle(pos=self.pos, radius=self.mass, color=(0, 255, 0))

spr = Spring(anchor_pos=Vec(X0, Y0), bob_pos=Vec(X0, Y0 + 100), mass=10)

def update():
    gravity = Vec(0, 0.1 * spr.mass)
    spr.apply_force(gravity)

    friction = spr.velocity * -1
    if friction.magnitude() > 0:
        friction.normalize_ip()
        friction = friction * C
        spr.apply_force(friction)

    force = spr.connect()
    spr.apply_force(force)

    spr.update()

def on_mouse_down(pos):
    print(f"on mouse down: {pos}")
    spr.pos = pos
    spr.velocity = Vec(0, 0)


def draw():
    screen.fill((0, 0, 0))
    spr.draw()

pgzrun.go()

