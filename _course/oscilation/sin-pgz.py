import math

import pgzrun

WIDTH = 1000
HEIGHT = 500

ampl = 10

class Oscilator:
    def __init__(self, pos, period, ampl):
        self.base_pos = pos
        self.pos = pos
        self.period = period
        self.amplide = ampl
        self.lifetime = 0

    def update(self):
        self.pos = self.base_pos[0], self.base_pos[1] - self.amplide * math.sin(math.pi * (self.base_pos[0] + 20 * self.lifetime) / self.period)
        self.lifetime += 1

    def draw(self):
        screen.draw.circle(pos=self.pos, radius=10, color=(0, 0, 255))

particles = [
    Oscilator(
        pos=(i * 10, HEIGHT // 2),
        period=600//2,
        ampl=100//5
    ) for i in range(100)
]

def update():
    for particle in particles:
        particle.update()

def draw():
    # update all objects
    # draw all objects to in-memory screen
    screen.fill((0, 0, 0))

    for particle in particles:
        particle.draw()

pgzrun.go()

