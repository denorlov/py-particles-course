import pgzrun
import pygame
import random

WIDTH = 1530
HEIGHT = 860

list_star_little = []
list_star_midl = []
list_star_big = []
speed = 1
speed_y = -0.5
num_star = 1000

#r, g, b = 255, 255, 255
#r, g, b = 0, 0, 255
#r, g, b = 20, 225, 160 
r, g, b = 139, 0, 255

for i in range(num_star):
    rand = random.random()
    list_star_little.append([[random.random() * WIDTH, random.random() * HEIGHT], 1, (r * rand, g * rand, b * rand)])

for i in range(num_star // 4):
    rand = random.random()
    list_star_midl.append([[random.random() * WIDTH, random.random() * HEIGHT], 3, (r * rand, g * rand, b * rand)])

for i in range(num_star // 10):
    rand = random.random()
    list_star_big.append([[random.random() * WIDTH, random.random() * HEIGHT], 10, (r * rand, g * rand, b * rand)])



def update():
    pass

def draw():
    screen.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill((0, 0, 0))

    for i in range(num_star):
        list_star_little[i][0][0] += speed
        list_star_little[i][0][1] += speed_y
        screen.draw.filled_circle((list_star_little[i][0][0] % WIDTH, list_star_little[i][0][1] % HEIGHT), list_star_little[i][1], list_star_little[i][2])
    
    for i in range(num_star // 4):
        list_star_midl[i][0][0] += speed / 1.5
        list_star_midl[i][0][1] += speed_y / 1.5
        screen.draw.filled_circle((list_star_midl[i][0][0] % WIDTH, list_star_midl[i][0][1] % HEIGHT), list_star_midl[i][1], list_star_midl[i][2])
    
    for i in range(num_star // 10):
        list_star_big[i][0][0] += speed / 4
        list_star_big[i][0][1] += speed_y / 4
        screen.draw.filled_circle((list_star_big[i][0][0] % WIDTH, list_star_big[i][0][1] % HEIGHT), list_star_big[i][1], list_star_big[i][2])

pgzrun.go()