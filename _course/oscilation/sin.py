import math
import random

import pygame
from pygame.math import Vector2

clock = pygame.time.Clock()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500

pygame.init()
pygame.display.set_caption("Particle oscilation")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

ampl = 10

class Oscilator:
    def __init__(self, coords, period, ampl):
        self.base_coords = coords
        self.coords = Vector2()
        self.period = period
        self.amplide = ampl
        self.lifetime = 0

    def update(self):
        self.coords.x = self.base_coords.x
        self.coords.y = self.base_coords.y - self.amplide * math.sin(math.pi * (self.base_coords.x + 20 * self.lifetime) / self.period)
        self.lifetime += 1

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, color=(0, 0, 255), center=self.coords, radius=10)

particles = [
    Oscilator(
        coords=Vector2(i * 10, WINDOW_HEIGHT // 2),
        period=600//2,
        ampl=100//5
    ) for i in range(100)
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

