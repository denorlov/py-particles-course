import math
import random

import pgzrun
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

position = Vector2(100, 100)
speed = Vector2(1, -3.3)

def update():
    global position
    global speed

    position += speed

    if position.x < 0 or position.x > WIDTH:
        speed.x = speed.x * -1

    if position.y < 0 or position.y > HEIGHT:
        speed.y = speed.y * -1


def draw():
    screen.fill((0, 0, 0))
    screen.draw.text(f"pos:{position}", (0, 0))
    screen.draw.text(f"speed:{speed}", (0, 20))

    screen.draw.circle(pos=position, radius=10, color=(0, 255, 0))

pgzrun.go()

