import random

import pygame

SCREEN_SIZE = WIDTH, HEIGHT = 1080, 720

worldsize = 1080
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

running = True

FPS = 60

stars = []
p = 0

pygame.init()

for i in range(10000):
    stars.append(
        (
            # x, y
            random.randint(0 - worldsize + 1, worldsize - 1),
            random.randint(0 - worldsize - 1, worldsize + 1),
            # light
            random.randint(1, worldsize)
         )
    )

#print(stars)

def draw(screen):
    global p
    screen.fill((20, 0, 30))
    for star in stars:
        star_light = star[2]
        if star_light != 0:
            pygame.draw.circle(
                surface=screen,
                color=(star_light % 255, star_light % 255, star_light % 255),
                center=(100 / star_light * star[1] + WIDTH // 2, 100 / star_light * star[0] + HEIGHT // 2),
                radius=2
            )
    # for star in range(len(stars)):
    #     print(stars[star][0])
    #     stars[star][0] += 1
    #     if stars[star][2] == worldsize:
    #         stars[star][2] = 0

while running:
    # внутри игрового цикл еще один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False

    # отрисовка и изменение свойств объектов
    draw(screen)

    # пауза на 1 / fps cek
    clock.tick(FPS)

    # обновление экрана
    pygame.display.flip()

pygame.quit()