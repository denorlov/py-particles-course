# Try creating your own textures for different types of effects.
# Can you make it look like fire, instead of smoke?

# Попробуйте поменять текстуру, которая использовалась в предыдущем примере.
# Попробуйте сделать огонь вместо дыма.

import random, pygame

import pgzrun
import pygame

import util
from pygame.constants import *
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2
G = 0.4

image = pygame.image.load("../assets/fire.png").convert_alpha()
image = pygame.transform.smoothscale(image, (128, 128))

bg = pygame.image.load('../assets/autumn_forest.jpg')

frame_count = 0
def update():
    global frame_count
    frame_count += 1

def draw():
    screen.blit(bg, (0, 0))

    mx, my = pygame.mouse.get_pos()
    delta = 20
    for dx in range(-delta, delta, delta):
        for dy in range(-delta, delta, delta):
            screen.surface.blit(image, (mx + dx, my + dy), special_flags=BLEND_RGBA_ADD)

    mx += 200
    for dx in range(-delta, delta, delta):
        for dy in range(-delta, delta, delta):
            screen.surface.blit(image, (mx + dx, my + dy), special_flags=BLENDMODE_NONE)

pgzrun.go()