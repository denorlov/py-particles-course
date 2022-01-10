import pgzrun
import pygame
import random
from pygame import Vector2

WIDTH = 1530
HEIGHT = 860

X0 = WIDTH // 2
Y0 = HEIGHT // 2

num_drops = 1500
drops_1, drops_2, drops_3 = int(num_drops * 0.5), int(num_drops * 0.3), int(num_drops * 0.2)

a = (0, 0.05)
spd = [[0, 0.03], [0, 0.4], [0, 1]]

drops = []
for i in range(drops_1):
    drops.append([Vector2(WIDTH * random.random(), -2000 * random.random()), 
                   Vector2(spd[0][0] * (random.random() + 1), spd[0][1] * (random.random() + 1)), 
                   Vector2(a), (3 * random.random(), 5 * random.random()), (0, 0, 140)])
for i in range(drops_2):
    drops.append([Vector2(WIDTH * random.random(), -2000 * random.random()), 
                   Vector2(spd[1][0] * (random.random() + 1), spd[1][1] * (random.random() + 1)), 
                   Vector2(a), (6 * random.random(), 7 * random.random()), (0, 0, 255)])
for i in range(drops_3):
    drops.append([Vector2(WIDTH * random.random(), -2000 * random.random()), 
                   Vector2(spd[2][0] * (random.random() + 1), spd[2][1] * (random.random() + 1)), 
                   Vector2(a), (8 * random.random(), 10 * random.random()), (80, 80, 255)])

def update():
    for i in range(num_drops):
        drops[i][1] += drops[i][2]
        drops[i][0] += drops[i][1]

        if drops[i][0][1] > HEIGHT - drops[i][3][1]:
            drops[i][0][1] = drops[i][3][1] - 60
            if int(num_drops * 0.5) <= i :
                drops[i][1] = Vector2(spd[2][0] * (random.random() + 1), spd[2][1] * (random.random() + 1))
            elif int(num_drops * 0.2) <= i <= int(num_drops * 0.5):
                drops[i][1] = Vector2(spd[1][0] * (random.random() + 1), spd[1][1] * (random.random() + 1))
            else:
                drops[i][1] = Vector2(spd[0][0] * (random.random() + 1), spd[0][1] * (random.random() + 1))
        if drops[i][0][0] < drops[i][3][0]:
            drops[i][0][0] = WIDTH - drops[i][3][0] * random.random()
        if drops[i][0][0] > WIDTH - drops[i][3][0]:
            drops[i][0][0] = drops[i][3][0] * random.random()

def draw():
    screen.fill((50, 50, 50))
    screen.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.draw.rect(Rect((0, 0), (WIDTH, HEIGHT)), (255, 255, 255)) 

    for i in range(num_drops):
        screen.draw.filled_rect(Rect(drops[i][0].x, drops[i][0].y, drops[i][3][0], drops[i][3][1]), drops[i][4])
    

pgzrun.go()