import pygame

clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption("PyGame start project")
screen = pygame.display.set_mode((500, 500))

is_running = True
while is_running:
    # process all input events (keys, mouse, timers)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            continue
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            is_running = False
            continue

    # update all objects
    # draw all objects to in-memory screen
    screen.fill((255, pygame.time.get_ticks() % 255, 255 - pygame.time.get_ticks() % 255))
    # flush in memory to real screen
    pygame.display.update()
    # pause if required
    clock.tick(60)

