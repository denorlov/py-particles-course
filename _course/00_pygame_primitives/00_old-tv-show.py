import pgzrun
import random

import pygame
from pgzero.rect import Rect

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

# изменение свойств обьектов
def update():
    pass

# отрисовка объектов
def draw():
    screen.fill((0, 0, 0))
    screen.draw.text("БЕЛЫЙ ШУМ", (X0 - 150, Y0), fontsize=60)
    for i in range(100):
        screen.draw.filled_rect(Rect(random.random() * WIDTH, random.random() * HEIGHT, 2, 2), pygame.Color('white'))

pgzrun.go()
