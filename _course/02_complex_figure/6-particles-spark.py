import math
import random

import pygame
from pygame.math import Vector2

clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("Particles lifetime")
screen = pygame.display.set_mode((1000, 500))

class Particle:
    def __init__(self, coords, velocity, size):
        self.coords = coords
        self.velocity = velocity
        self.lifetime = size * 10

    def update(self):
        self.coords = self.coords + self.velocity
        self.velocity[1] += 0.03
        self.lifetime -= 1

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, color=(0, 255, 0), center=self.coords, radius=self.lifetime // 20)


class Spark:
    def __init__(self, coords, angle_rad, speed):
        self.coords = coords
        self.angle = angle_rad
        self.speed = speed
        self.scale = 1.5

    def update(self, dt):
        velocity = Vector2(math.cos(self.angle), math.sin(self.angle)) * self.speed * dt
        self.coords = self.coords + velocity

        self.angle += .1
        self.speed -= .2

    def draw(self, surface: pygame.Surface):
        scaled_speed = self.speed * self.scale

        p1 = self.coords + Vector2(math.cos(self.angle), math.sin(self.angle)) * scaled_speed
        p2 = self.coords + Vector2(math.cos(self.angle + math.pi / 2), math.sin(self.angle + math.pi / 2)) * scaled_speed * 0.3
        p3 = self.coords - Vector2(math.cos(self.angle), math.sin(self.angle)) * scaled_speed * 3.5
        p4 = self.coords + Vector2(math.cos(self.angle - math.pi / 2), -math.sin(self.angle + math.pi / 2)) * scaled_speed * 0.3

        pygame.draw.polygon(surface, color=(0, 255, 255), points=[p1, p2, p3, p4])

    def is_alive(self):
        return self.speed >= 0



particles = []

is_running = True
while is_running:

    # process all input events (keys, mouse, timers)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            continue
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            is_running = False
            continue

    # update all objects
    # draw all objects to in-memory screen
    screen.fill((0, 0, 0))

    for _ in range(5):
        particles.append(
            Spark(
                coords=pygame.mouse.get_pos(),
                angle_rad=math.radians(random.randint(0, 360)),
                speed=random.randint(3, 6)
            )
        )

    particles_to_remove = []

    for particle in particles:
        particle.update(1)
        particle.draw(screen)
        if not particle.is_alive():
            particles_to_remove.append(particle)

    for particle_to_remove in particles_to_remove:
        particles.remove(particle_to_remove)

    # flush in memory to real screen
    pygame.display.update()
    # pause if required
    clock.tick(60)

