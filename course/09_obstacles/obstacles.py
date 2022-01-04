#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys, random

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)

TILE_SIZE = 20

# [loc, velocity, timer]
particles = []

tile_map = {}
for i in range(10):
    tile_map[str(i + 4) + ';14'] = [i + 4, 14, (255, 0, 0)]

# tile_map['15;10'] = [15, 10, (0, 0, 255)]
# tile_map['15;11'] = [15, 11, (0, 0, 255)]
# tile_map['15;12'] = [15, 12, (0, 0, 255)]
# tile_map['15;13'] = [15, 13, (0, 0, 255)]

# tile_map['11;11'] = [11, 11, (0, 255, 255)]
# tile_map['11;12'] = [11, 12, (0, 255, 255)]

clicking = False


def particles_explosion(particles):
    for particle in particles:
        particle[0][0] += particle[1][0]  # coordinate sull'asse x
        # stringa con riga e colonna dello schema dello schermo che nel dizionario...
        loc_str = str(int(particle[0][0] / TILE_SIZE)) + ';' + str(int(particle[0][1] / TILE_SIZE))
        # rimbalza su verticali
        # Se si trova quindi a contatto con un tile rimbalza
        if loc_str in tile_map:
            particle[1][0] = -0.7 * particle[1][0]
            particle[1][1] *= 0.95
            particle[0][0] += particle[1][0] * 2
        particle[0][1] += particle[1][1]
        loc_str = str(int(particle[0][0] / TILE_SIZE)) + ';' + str(int(particle[0][1] / TILE_SIZE))
        if loc_str in tile_map:
            # Rimbalza in orizzontale
            particle[1][1] = -0.7 * particle[1][1]
            particle[1][0] *= 0.95
            particle[0][1] += particle[1][1] * 2
        particle[2] -= 0.035
        particle[1][1] += 0.15
        # ============= ecco le particles ==================
        pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])],
                           int(particle[2]))
        if particle[2] == 0:
            particles.remove(particle)


# Loop ------------------------------------------------------- #
while True:

    # Background --------------------------------------------- #
    screen.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()

    # Particles ---------------------------------------------- #
    if clicking:
        for i in range(10):
            particles.append(
                [[mx, my], [random.randint(0, 42) / 6 - 3.5, random.randint(0, 42) / 6 - 3.5],
                 random.randint(4, 6)])
    particles_explosion(particles)

    # Render Tiles ------------------------------------------- #
    for tile in tile_map:
        # ----------------surface---------- colore---------------
        pygame.draw.rect(screen, tile_map[tile][2],
                         # coordinate del rettangolo
                         pygame.Rect(tile_map[tile][0] * TILE_SIZE, tile_map[tile][1] * TILE_SIZE,
                                     TILE_SIZE, TILE_SIZE))

    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                # for i in range(10):
                clicking = True
                particles.append(
                    [
                        [mx, my],  # posizione iniziale
                        [random.randint(0, 42) / 6 - 3.5,  # direzione con una certa casualità
                         random.randint(0, 42) / 6 - 3.5],
                        random.randint(4, 6)])  # grandezza delle sfere

        # if event.type == MOUSEBUTTONUP:
        #     if event.button == 1:
        #         clicking = False

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)