import random

import pygame

clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("PyGame start project")
screen = pygame.display.set_mode((500, 500))

class Particle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, color=(0,255,0), center=(self.x, self.y), radius=self.radius)

particles = [Particle(
    x=random.randint(0, 500-1),
    y=random.randint(0, 500-1),
    radius=random.randint(0, 10),
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
        particle.draw(screen)

    # flush in memory to real screen
    pygame.display.update()
    # pause if required
    clock.tick(60)

