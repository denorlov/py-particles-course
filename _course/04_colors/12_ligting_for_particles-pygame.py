import pygame, sys, random

# Setup pygame/window ---------------------------------------- #
from pygame.math import Vector2

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500))

def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf

class Particle:
    def __init__(self, coords, velocity, size):
        self.coords = coords
        self.velocity = velocity
        self.size = size
        self.lifetime = size * 10

    def update(self):
        particle.coords += particle.velocity
        particle.lifetime -= 0.1
        particle.velocity.y += 0.15

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(screen, (255, 255, 255), particle.coords, particle.size)
        radius = particle.size * 2
        screen.blit(circle_surf(radius, (20, 20, 60)), (int(particle.coords.x - radius), int(particle.coords.y - radius)), special_flags=BLEND_RGB_ADD)


particles = []

bg = pygame.image.load('../assets/girl.jpg')

# Loop ------------------------------------------------------- #
is_running = True
while is_running:

    # Background --------------------------------------------- #
    screen.blit(bg, (0,0))

    mx, my = pygame.mouse.get_pos()

    particles.append(Particle(
        coords=Vector2(mx, my),
        velocity=Vector2(random.randint(0, 20) / 10 - 1, -5),
        size=random.randint(6, 11)
    ))

    for particle in particles:
        particle.update()
        particle.draw(screen)

        if particle.lifetime <= 0:
            particles.remove(particle)

    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            is_running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                is_running = False

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)

pygame.quit()
