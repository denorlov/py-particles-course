# Take random walker program and convert it to use vectors

# Перед вами программа random walker. Объект перемещается на плоскости случайным образом.
# Каждый ход объект перемещается на соседнюю клетку случайным образом.
# Перепишите программу с использованием векторов.

import random

import pgzrun

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

class Walker:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        screen.draw.circle(pos=(self.x, self.y), radius=2, color=(0, 255, 0))

    def move(self):
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)

        self.x += dx
        self.y += dy

walker = Walker(X0, Y0)

def update():
    walker.move()

def draw():
    #screen.fill((0, 0, 0))
    walker.draw()

pgzrun.go()



