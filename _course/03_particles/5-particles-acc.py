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
        pygame.draw.circle(surface, color=(0,255,0), center=self.coords, radius=self.lifetime // 20)

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

    particles.append(
        Particle(
            coords=pygame.mouse.get_pos(),
            velocity=Vector2(random.randint(-100, +100) * 0.01, random.randint(-300, 0) * 0.01),
            size=random.randint(10, 15),
        )
    )

    for particle in particles:
        particle.update()
        particle.draw(screen)
        if particle.lifetime <= 0:
            particles.remove(particle)

    # flush in memory to real screen
    pygame.display.update()
    # pause if required
    clock.tick(60)

