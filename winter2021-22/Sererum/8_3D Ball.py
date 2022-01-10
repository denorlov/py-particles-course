import pgzrun
import pygame
import pgzero
import random
from pygame import Vector3

WIDTH = 800
HEIGHT = 600

X0 = WIDTH // 2
Y0 = HEIGHT // 2

size_box = 500
k_deep = 0.83
min_box = size_box * k_deep

position = Vector3(X0, Y0, size_box // 2)
speed = Vector3(5 * random.random(), 5 * random.random(), 5 * random.random())

radius = 60
MIN_RAD = radius - (size_box - min_box) // 2
nin_rad = radius - (size_box - min_box) // 2

k_up = ((size_box - min_box) // 2) / size_box

place = [4000, 4000, radius]
dop = True
is_in_full_screen = False

def on_key_down(key):
    global dop, is_in_full_screen

    if key == keys.SPACE:
        dop = not dop

    if key == keys.F:
        is_in_full_screen = not is_in_full_screen
        if is_in_full_screen:
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        else:
            screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))

def update():
    global position
    global speed
    global min_rad
    global place

    position += speed
    min_rad = (k_up * position.z) + MIN_RAD

    if position.x < X0 - size_box / 2 + radius or position.x > X0 - size_box / 2 + size_box - radius:
        speed.x = -speed.x
    if position.y < Y0 - size_box / 2 + radius or position.y > Y0 - size_box / 2 + size_box - radius:
        speed.y = -speed.y
    if position.z < radius or position.z > size_box - radius:
        speed.z = -speed.z
        place = [position.x, position.y, min_rad]
    
clock = pygame.time.Clock()

def draw():
    X1, Y1 = X0 - size_box / 2, Y0 - size_box / 2
    X2, Y2 = X0 - min_box / 2, Y0 - min_box / 2
    screen.fill((0, 0, 0))

    screen.draw.rect(Rect((0, 0), (WIDTH, HEIGHT)), (255, 255, 255))

    screen.draw.rect(Rect((X1, Y1), (size_box, size_box)), (255, 255, 255))
    screen.draw.rect(Rect((X2, Y2), (min_box, min_box)), (255, 255, 255))

    pts = [
        [(X1, Y1), (X2, Y2)],
        [(X1 + size_box, Y1), (X2 + min_box, Y2)],
        [(X1, Y1 + size_box), (X2, Y2 + min_box)],
        [(X1 + size_box, Y1 + size_box), (X2 + min_box, Y2 + min_box)]
    ]

    for i in pts:
        screen.draw.line(i[0], i[1], (255, 255, 255))

    if dop:
        screen.draw.circle((place[0], place[1]), place[2], (255, 255, 100))
        screen.draw.text(f"fps:{clock.get_fps()}", (10, 10))

    screen.draw.filled_circle((position.x, position.y), min_rad, (139, 0, 255))



pgzrun.go()