import pgzrun
import pgzero
import pygame as pg
from random import random as rand, randint as rdint, uniform as rdflt
from pygame import Color, Vector2 

WIDTH = 1530
HEIGHT = 860

X0 = WIDTH // 2
Y0 = HEIGHT // 2

num_baloon = 40
mid_h = Y0
G = Vector2(0, 10)
wind = Vector2(0, 0)
debag = False

class Baloon:
    def __init__(self, pos, v, a, m, rad, color):
        self.pos = pos
        self.v = v
        self.a = a
        self.m = m
        self.rad = rad
        self.color = color

    def force(self, force):
        self.a += force / self.m

    def update(self):
        self.a.y += -(self.pos.y / self.m) * (G.y / mid_h)
        self.v += self.a
        self.v *= 0.01
        self.pos += self.v

        if self.pos.x < self.rad or self.pos.x > WIDTH - self.rad:
            self.v.x = -self.v.x

        if self.pos.y < self.rad or self.pos.y > HEIGHT - self.rad:
            self.v.y = -self.v.y

        if self.pos.y - 1 > HEIGHT - self.rad:
            self.pos.y = HEIGHT - self.rad

        if self.pos.y + 1 < self.rad:
            self.pos.y = self.rad

        if self.pos.x - 1 > WIDTH - self.rad:
            self.pos.x = WIDTH - self.rad

        if self.pos.x + 1 < self.rad:
            self.pos.x = self.rad

        self.pos += self.v

    def draw(self):
        screen.draw.filled_circle(pos=self.pos, radius=self.rad, color=self.color)
        if debag:
            screen.draw.text(f"pos:{self.pos}", self.pos, color=(255, 255, 255))
            screen.draw.text(f"vel:{self.v}", self.pos + Vector2(0, 15), color=(255, 255, 255))
            screen.draw.line(self.pos, self.pos + (self.v * 50), (0, 255, 0))

baloon = [
    Baloon(pos=Vector2(X0 * rdflt(0.1, 1.9), Y0 * rdflt(0.3, 1.7)),
           v=Vector2(0, 0), a=Vector2(0, 0), m=rdint(5, 25), 
           rad=rdint(25, 35), color=(rdint(0, 255), rdint(0, 150), rdint(0, 255))
           )for _ in range(num_baloon)
    ]

def on_key_down(key):
    global wind, debag
    if key == keys.LEFT:
        wind = Vector2(rdflt(-10, 0), rdflt(-1, 1))
    if key == keys.RIGHT:
        wind = Vector2(rdflt(0, 10), rdflt(-1, 1))
    if key == keys.DOWN:
        wind = Vector2(0, 0)
    if key == keys.F:
        debag = bool(int(debag) - 1)


def update():
    for b in baloon:
        b.force(G)
        b.force(wind)
        b.update()


def draw():
    screen.fill((0, 0, 0))
    screen.surface = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    screen.draw.rect(Rect((0, 0), (WIDTH, HEIGHT)), (255, 255, 255)) 
    
    for b in baloon:
        b.draw()
        
pgzrun.go()