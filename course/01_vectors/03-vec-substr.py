import math
import random

import pgzrun
import pygame
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

def update():
    pass

def draw():
    screen.fill((0, 0, 0))

    mouse_vec = Vector2(pygame.mouse.get_pos())
    center_vec = Vector2(X0, Y0)

    screen.draw.line(center_vec, center_vec + (mouse_vec - center_vec), color=(255, 255, 255))

pgzrun.go()

