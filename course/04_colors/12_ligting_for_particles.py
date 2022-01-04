import pgzrun
import pygame, sys, random

# Setup pygame/window ---------------------------------------- #
from pygame import BLEND_RGB_ADD
from pygame.math import Vector2

WIDTH = 600
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

bg = pygame.image.load('../assets/girl.jpg')

def surface_with_circle(width, color):
    surface = pygame.Surface((width, width))
    surface.set_colorkey((0, 0, 0))
    radius = width // 2
    pygame.draw.circle(surface, color, center=(radius, radius), radius=radius)
    return surface

class Particle:
    def __init__(self, coords, velocity, size):
        self.coords = coords
        self.velocity = velocity
        self.size = size
        self.lifetime = size * 10

    def update(self):
        self.coords += self.velocity
        self.lifetime -= 0.1
        self.velocity.y += 0.15

    def draw(self):
        screen.draw.filled_circle(pos=self.coords, radius=self.size, color=(255, 255, 255))
        radius = self.size * 2
        screen.surface.blit(
            surface_with_circle(width=radius * 2, color=(20, 20, 60)),
            (self.coords.x - radius, self.coords.y - radius),
            special_flags=BLEND_RGB_ADD
        )

particles = []
demo_particle = Particle(coords=Vector2(50, 50), velocity=Vector2(0, 0), size=11)

def update():
    mx, my = pygame.mouse.get_pos()

    particles.append(Particle(
        coords=Vector2(mx, my),
        velocity=Vector2(random.randint(0, 20) / 10 - 1, -5),
        size=random.randint(6, 11)
    ))

    for particle in particles:
        particle.update()


def draw():
    screen.blit(bg, (0,0))

    for particle in particles:
        particle.update()
        particle.draw()

        if particle.lifetime <= 0:
            particles.remove(particle)

    demo_particle.draw()


pgzrun.go()
