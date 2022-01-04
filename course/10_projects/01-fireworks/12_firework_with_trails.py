import math
import random

import pgzrun
import pygame
from pygame.constants import *
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

def update():
    pass

frame_count = 0

bg = pygame.image.load('../../assets/autumn_forest.jpg')

BLUE = pygame.Color('dodgerblue4')

# I just create the background surface in the following lines.
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((90, 120, 140))
for y in range(0, 600, 20):
    for x in range(0, 800, 20):
        pygame.draw.rect(background, BLUE, (x, y, 20, 20), 1)

# This dark gray surface will be blitted above the background surface.
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
surface.fill(pygame.Color('gray11'))

def draw():
    global frame_count
    frame_count += 1

    if frame_count == 1:
        screen.surface.blit(background, (0, 0))

    # if frame_count == 1:
    #     # screen.fill((0, 0, 0))
    #     screen.blit(bg, (0, 0))
    #     screen.draw.text(f"frame:{frame_count}", (10, 10))
    surface.fill((0, 0, 0, 25))
    # ... and draw a transparent circle onto it to create a hole.
    pygame.draw.circle(surface, (0, 0, 0, 25), pygame.mouse.get_pos(), 90)

    # see https://stackoverflow.com/questions/53643165/how-do-i-leave-a-trail-behind-a-sprite-with-pygame
    # screen.surface.fill((255, 255, 0, 25))
    screen.surface.blit(surface, (0, 0))
pgzrun.go()
