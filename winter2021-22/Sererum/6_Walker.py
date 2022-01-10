import pgzrun
import pygame
import pgzero
import random
from pygame import Vector2

WIDTH = 1530
HEIGHT = 860

X0 = WIDTH // 2
Y0 = HEIGHT // 2

position = Vector2(X0, Y0)
speed = Vector2(5, 5)
radius = 10

def update():
    global position 
    global speed
    global radius

    position += speed

    if random.random() > 0.5:
        speed.x = -speed.x
    if random.random() > 0.5:
        speed.y = -speed.y

    if position.x < radius:
        position.x = radius
    elif position.x > WIDTH - radius:
        position.x = WIDTH - radius

    if position.y < radius:
        position.y = radius
    elif position.y > HEIGHT - radius:
        position.y = HEIGHT - radius

def draw():
    screen.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.draw.rect(Rect((0, 0), (WIDTH, HEIGHT)), (255, 255, 255)) 
    
    screen.draw.filled_circle((position.x, position.y), radius, (0, 255, 255))
    

pgzrun.go()