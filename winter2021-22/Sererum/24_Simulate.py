import pgzrun
import pygame as pg
from random import random as rand, randint as rdint, uniform as rdflt
from pygame import Color, Surface, Vector2 

WIDTH = 1530
HEIGHT = 860

X0 = WIDTH // 2
Y0 = HEIGHT // 2

COLOR = [200, 0.1, 255]

surface = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)

gravity_force = 1
planets = []
genesises = []
star_pos = []
portal = []

menu = False

len_trek = 0

walls = "Границы"
destroy = "Отключена"

on_space = False

################################################## Planet

class Planet:
    def __init__(self, pos, vel, acc, mas, clr):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.mas = mas
        self.clr = clr
        self.mouse = Vector2(0, 0)

    def force(self, force):
        self.acc += force

    def update(self):
        if self.mouse.length() > 0:
            self.vel = (self.mouse + pg.mouse.get_pos()) - self.pos
            self.pos = self.mouse + pg.mouse.get_pos()
        else:
            self.vel += self.acc
            self.pos += self.vel

        if walls == "Границы":
            Ft = -10
            if self.pos.x < self.mas:
                self.vel.x = self.vel.x / Ft
                self.pos.x = self.mas + 1

            if self.pos.x > WIDTH - self.mas:
                self.vel.x = self.vel.x / Ft
                self.pos.x = WIDTH - self.mas - 1

            if self.pos.y < self.mas:
                self.vel.y = self.vel.y / Ft
                self.pos.y = self.mas + 1

            if self.pos.y > HEIGHT - self.mas:
                self.vel.y = self.vel.y / Ft
                self.pos.y = HEIGHT - self.mas - 1

        elif walls == "Портал":
            if self.pos.x < -self.mas:
                self.pos.x = WIDTH + self.mas

            if self.pos.x > WIDTH + self.mas:
                self.pos.x = -self.mas

            if self.pos.y < -self.mas:
                self.pos.y = HEIGHT + self.mas

            if self.pos.y > HEIGHT + self.mas:
                self.pos.y = -self.mas

        self.acc = Vector2(0, 0)

    def draw(self):
        pg.draw.circle(surface, center=self.pos, radius=self.mas, color=self.clr)

#################################################### Genesis

class Genesis:
    def __init__(self, planet:Planet):
        self.rad = 5
        self.mas = planet.mas * 5
        self.clr = planet.clr
        self.pos = planet.pos
        planets.remove(planet)
        self.parts = []

    def create_circle(self, rad):
        if self.rad > self.mas:
            return
        for _ in range(20):
            one_vec = Vector2(-1, 0)
            one_vec = one_vec.rotate(rdint(0, 360))
            self.parts.append(Part(
                pos=self.pos + (one_vec * rad),
                vel=one_vec * rdflt(-0.1, 1),
                rad=3,
                clr=self.clr,
                time=rdint(100, 255)
            ))

    def update(self):
        self.rad += 1
        self.create_circle(self.rad)
        for p in self.parts:
            if p.is_alive():
                p.update()
            else:
                self.parts.remove(p)

    def draw(self):
        for p in self.parts:
            p.draw()

######################################################### Part

class Part:
    def __init__(self, pos, vel, rad, clr, time):
        self.pos = pos
        self.vel = vel
        self.rad = rad
        self.clr = clr
        self.time = time

    def update(self):
        if not self.is_alive():
            return
        self.time -= 2
        self.pos += self.vel

    def draw(self):
        if self.is_alive():
            print(self.clr[0], self.time, self.clr[0]/(self.clr[0]/self.time))
            pg.draw.circle(surface, center=self.pos, radius=self.rad, color=(self.time*(self.clr[0]/255), self.time*(self.clr[1]/255), self.time*(self.clr[2]/255)))

    def is_alive(self):
        return self.time > 0

############################################## Funktions

for _ in range(400):
    star_pos.append([WIDTH * rand(), HEIGHT * rand()])

def create_planet():
    planets.append(Planet(
        pos=Vector2(WIDTH * rdflt(0.1, 0.9), HEIGHT * rdflt(0.1, 0.9)),
        vel=Vector2(rdflt(-1, 1), rdflt(-1, 1)),
        acc=Vector2(0, 0),
        mas=rdint(20, 50),
        clr=(COLOR[0] * rdflt(0.5, 1), COLOR[1] * rdflt(0.5, 1), COLOR[2] * rdflt(0.5, 1))
    ))

def delete_planet():
    planets.pop(rdint(0, len(planets) - 1))

for _ in range(10):
    create_planet() 

def gravity(main:Planet, body:Planet):
    vec = body.pos - main.pos
    if vec != Vector2(0, 0):
        one_vec = vec.normalize()
        f = one_vec * ((gravity_force * body.mas) / ((vec.length() + 10) ** 2))
        return f
    return Vector2(0, 0)

#################################################### Update and Drow

def update():
    if len(planets) > 100:
        delete_planet()

    if on_space:
        return
    if walls == "Портал":
        for i in [
            [0, -60, 0, HEIGHT, 0, 0.5, -0.5, 0.5], [WIDTH, 60, 0, HEIGHT, -0.5, 0, -0.5, 0.5],
            [0, WIDTH, 0, -60, -0.5, 0.5, 0, 0.5], [0, WIDTH, HEIGHT, 60, -0.5, 0.5, -0.5, 0]
        ]:
            portal.append(Part(
                pos=Vector2(i[0] + i[1] * rand(), i[2] + i[3] * rand()),
                vel=Vector2(rdflt(i[4], i[5]), rdflt(i[6], i[7])),
                rad=rdflt(4, 8),
                clr=(20 * rand(), 255 * rand(), 20 * rand()),
                time=rdint(200, 255)
                ))

    if walls == "Портал":
        for p in portal:
            p.update()

    for p in planets:
        p.update()
        for p1 in planets:
            if p != p1:
                p.force(gravity(p, p1))

    for g in genesises:
        if g.rad < g.mas * 10:
            g.update()
        else:
            genesises.remove(g)

def draw():
    if on_space:
        return

    if len_trek <= 0:
        surface.fill((0, 0, 0, 255))
    else:
        surface.fill((0, 0, 0, 255 / (len_trek * 5)))

    for s in star_pos:
        pg.draw.circle(surface, center=s, radius=2, color=(250, 235, 215))

    if walls == "Портал":
        for p in portal:
            p.draw()

    for p in planets:
        p.draw()

    for g in genesises:
        g.draw()

    screen.surface = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    screen.blit(surface, pos=(0, 0))

    if menu:
        draw_instruction()
    else:
        screen.draw.text("M-Меню", pos=(0, 0), fontsize=35, color=(255, 255, 255))

################################################################ Меню

def draw_instruction():
    font = 38
    screen.draw.text("SPACE-Пауза", pos=(0, 0), fontsize=font, color=(255, 255, 255))
    screen.draw.text(f"Объектов:{len(planets)}", pos=(0, font * 2), fontsize=font, color=(255, 255, 255))
    screen.draw.text("1-Создать", pos=(0, font * 3), fontsize=font, color=(255, 255, 255))
    screen.draw.text("2-Удалить", pos=(0, font * 4), fontsize=font, color=(255, 255, 255))
    screen.draw.text(f"Гравитация:{gravity_force}", pos=(0, font * 6), fontsize=font, color=(255, 255, 255))
    screen.draw.text("3-Увеличить", pos=(0, font * 7), fontsize=font, color=(255, 255, 255))
    screen.draw.text("4-Уменишить", pos=(0, font * 8), fontsize=font, color=(255, 255, 255))
    screen.draw.text(f"Длина треков:{len_trek}", pos=(0, font * 10), fontsize=font, color=(255, 255, 255))
    screen.draw.text("5-Увеличить", pos=(0, font * 11), fontsize=font, color=(255, 255, 255))
    screen.draw.text("6-Уменишить", pos=(0, font * 12), fontsize=font, color=(255, 255, 255))
    screen.draw.text(f"Режим Границ:{walls}", pos=(0, font * 14), fontsize=font, color=(255, 255, 255))
    screen.draw.text("7-Без Границ", pos=(0, font * 15), fontsize=font, color=(255, 255, 255))
    screen.draw.text("8-Границы", pos=(0, font * 16), fontsize=font, color=(255, 255, 255))
    screen.draw.text("9-Портал", pos=(0, font * 17), fontsize=font, color=(255, 255, 255))
    screen.draw.text(f"Анигиляция Объектов:{destroy}", pos=(0, font * 19), fontsize=font, color=(255, 255, 255))
    screen.draw.text("0-Переключить режим", pos=(0, font * 20), fontsize=font, color=(255, 255, 255))
    screen.draw.text("E-Exit", pos=(0, font * 22), fontsize=font, color=(255, 255, 255))

##################################################### Обработка Нажатий

def on_mouse_down():
    for p in planets:
        if (p.pos - pg.mouse.get_pos()).length() < p.mas:
            if destroy == "Активна":
                genesises.append(Genesis(p))
            else:
                p.mouse = p.pos - pg.mouse.get_pos()

def on_mouse_up():
    for p in planets:
        p.mouse = Vector2(0, 0)

def on_key_down(key):

    global menu
    if key == keys.M:
        menu = True
    if key == keys.E:
        menu = False

    global on_space
    if key == keys.SPACE:
        on_space = not on_space

    if key == keys.K_1:
        create_planet()
    if key == keys.K_2 and len(planets) > 0:
        delete_planet()

    global gravity_force
    if key == keys.K_3:
        gravity_force += 1
    if key == keys.K_4:
        gravity_force -= 1

    global len_trek
    if key == keys.K_5 and len_trek < 31:
        len_trek += 1
    if key == keys.K_6 and len_trek > 0:
        len_trek -= 1

    global walls
    if key == keys.K_7:
        walls = "Без Границ"
    if key == keys.K_8:
        walls = "Границы"
    if key == keys.K_9:
        walls = "Портал"

    global destroy
    if key == keys.K_0:
        print(destroy, destroy == "Активна")
        if destroy == "Активна":
            destroy = "Отключена"
        else:
            destroy = "Активна"

pgzrun.go()