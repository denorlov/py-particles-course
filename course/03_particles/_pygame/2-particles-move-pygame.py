import random

import pygame
from pygame.math import Vector2

clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("Particles move")
screen = pygame.display.set_mode((500, 500))

class Particle:
    def __init__(self, coords, velocity, size):
        self.coords = coords
        self.velocity = velocity
        self.size = size

    def update(self):
        self.coords = self.coords + self.velocity

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, color=(0,255,0), center=self.coords, radius=self.size)

particles = [Particle(
    coords=Vector2(255, 255),
    velocity=Vector2(random.randint(-5, +5), random.randint(-5, +5)),
    size=random.randint(0, 10),
) for i in range(30)
]

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

    for particle in particles:
        particle.update()
        particle.draw(screen)

    # flush in memory to real screen
    pygame.display.update()
    # pause if required
    clock.tick(60)

