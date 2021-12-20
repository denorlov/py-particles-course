import pgzrun

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

x = 100
y = 100

xspeed = 1
yspeed = -3.3


def update():
    global x, y
    global xspeed, yspeed

    x += xspeed
    y += yspeed

    if x < 0 or x > WIDTH:
        print("revert xsp")
        xspeed = xspeed * -1

    if y < 0 or y > HEIGHT:
        print("revert ysp")
        yspeed = yspeed * -1


def draw():
    screen.fill((0, 0, 0))
    screen.draw.text(f"x:{x}, y:{y}", (0, 0))
    screen.draw.text(f"xsp:{xspeed}, ysp:{yspeed}", (0, 20))

    screen.draw.circle(pos=(x, y), radius=10, color=(0, 255, 0))

pgzrun.go()

