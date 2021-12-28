import pygame, pgzrun
from pygame.constants import *

WIDTH = 600
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

bg = pygame.image.load('../assets/girl.jpg')

RADIUS = 60

def surface_with_circle(width, color):
    surface = pygame.Surface((width, width))
    surface.set_colorkey((0, 0, 0))
    radius = width // 2
    pygame.draw.circle(surface, color, center=(radius, radius), radius=radius)
    return surface

def update():
    pass

def draw():
    screen.blit(bg, (0,0))

    mx, my = pygame.mouse.get_pos()
    screen.surface.blit(surface_with_circle(RADIUS, color=(55, 55, 55)), (mx, my), special_flags=BLEND_RGB_SUB)
    screen.surface.blit(surface_with_circle(RADIUS, color=(55, 55, 55)), (mx + 1.5 * RADIUS, my), special_flags=BLEND_RGB_ADD)
    screen.surface.blit(surface_with_circle(RADIUS, color=(0, 0, 55)), (mx, my + 1.5 * RADIUS), special_flags=BLEND_RGB_ADD)
    screen.surface.blit(surface_with_circle(RADIUS, color=(0, 55, 0)), (mx + 1.5 * RADIUS, my + 1.5 * RADIUS), special_flags=BLEND_RGB_ADD)

pgzrun.go()
