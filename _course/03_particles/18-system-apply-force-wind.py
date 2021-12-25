# включаем ветер

import math
import random

import pgzrun
from pgzero.rect import Rect
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
        self.lifetime = 255

    def apply_force(self, force):
        self.acc += force / self.mass

    def is_alive(self):
        return self.lifetime > 0

    def update(self):
        self.lifetime -= 2

        self.velocity += self.acc
        if self.velocity.length() > self.top_velocity_limit:
            self.velocity.scale_to_length(self.top_velocity_limit)

        self.pos += self.velocity

    def draw(self):
        screen.draw.filled_circle(pos=self.pos, radius=self.mass, color=(0, 255 / (255 / self.lifetime), 0))
        # screen.draw.line(self.pos, self.pos + self.velocity * 20, color=(0, 255, 0))
        # screen.draw.line(self.pos, self.pos + self.acc * 100, color=(255, 255, 0))
        # screen.draw.text(f"{self.lifetime}", self.pos)

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    return qx, qy

class Confetti(Particle):
    def __init__(self, pos, velocity, acc, top_velocity_limit, mass):
        self.angle = 0
        super().__init__(pos, velocity, acc, top_velocity_limit, mass)

    def update(self):
        self.angle -= 2
        super().update()

    def draw(self):
        x, y = rotate((self.pos.x, self.pos.y), (self.pos.x - self.mass, self.pos.y - self.mass), math.radians(self.angle))
        x1, y1 = rotate((self.pos.x, self.pos.y), (self.pos.x + self.mass, self.pos.y - self.mass), math.radians(self.angle))
        x2, y2 = rotate((self.pos.x, self.pos.y), (self.pos.x + self.mass, self.pos.y + self.mass), math.radians(self.angle))
        x3, y3 = rotate((self.pos.x, self.pos.y), (self.pos.x - self.mass, self.pos.y + self.mass), math.radians(self.angle))

        c = (255 / (255 / self.lifetime), 255 / (255 / self.lifetime), 0)

        screen.draw.line(start=(x, y), end=(x1, y1), color=c)
        screen.draw.line(start=(x1, y1), end=(x2, y2), color=c)
        screen.draw.line(start=(x2, y2), end=(x3, y3), color=c)
        screen.draw.line(start=(x3, y3), end=(x, y), color=c)

        #screen.draw.text(f"{self.lifetime}, c={c}", self.pos)



class ParticlesSytem:
    def __init__(self):
        self.particles = [self.create() for _ in range(200)]

    def create(self) -> Particle:
        return self.create_particle() if random.randint(0, 1) else self.create_confetti()

    def create_particle(self) -> Particle:
        return Particle(
            pos=Vector2(X0, Y0 - 100),
            velocity=Vector2(random.uniform(-3, 3), random.uniform(-3, 0)),
            acc=Vector2(0, 0.05),
            top_velocity_limit=10,
            mass=random.randint(1, 10)
        )

    def create_confetti(self) -> Confetti:
        return Confetti(
            pos=Vector2(X0, Y0 - 100),
            velocity=Vector2(random.uniform(-3, 3), random.uniform(-3, 0)),
            acc=Vector2(0, 0.05),
            top_velocity_limit=10,
            mass=random.randint(1, 5)
        )

    def update(self):
        self.particles.append(self.create())

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

ps = ParticlesSytem()

def update():
    ps.update()

def draw():
    screen.fill((0, 0, 0))
    screen.draw.text(f"particles:{len(ps.particles)}", (0,0))
    ps.draw()

pgzrun.go()
