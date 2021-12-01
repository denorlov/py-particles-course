import random, pygame

pygame.init()
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Press right arrow key to start")
window2 = pygame.Surface((600, 400))
clock = pygame.time.Clock()

group = []


class Particles(pygame.sprite.Sprite):
    "Creates particles starting from pos with a color"

    def __init__(self, pos, y_dir, color, sparse=0, turn="off"):
        super(Particles, self).__init__()
        self.particles_list = []
        self.pos = pos
        self.color = color
        self.y_dir = y_dir
        self.sparse = sparse  # generate particles not from the same starting point
        # self.generate_particles()
        group.append(self)
        self.turn = turn  # this makes the effect visible

    def choose_y_dir(self):
        "Makes particles go in every direction you want"

        # Make the flow go down
        if self.y_dir == "down":
            y_dir = 2

        elif self.y_dir == "up":
            y_dir = -2

        # Make the particles spread all y_dirs
        elif self.y_dir == "all":
            y_dir = random.randrange(-2, 2, 1)

        return y_dir

    def generate_particles(self):
        "List with position etc of particles"

        if self.sparse == 1:
            self.pos[0] = random.randint(0, 600)

        # setting the data for each particles
        origin = [self.pos[0], self.pos[1]]  # Starting here each particles
        y_dir = self.choose_y_dir()
        x_dir = random.randint(0, 20) / 10 - 1
        dirs = [x_dir, y_dir]  # movement
        radius = random.randint(4, 6)  # radius
        # Appending data to the list
        self.particles_list.append([origin, dirs, radius])
        self.generate_movements()

    def generate_movements(self):

        # Moving the coordinates and size of self.particles_list
        for particle in self.particles_list[:]:
            particle[0][0] += particle[1][0]  # x pos += x_dir
            particle[0][1] += particle[1][1]  # y pos += y_dir
            particle[2] -= 0.05  # how fast circles shrinks
            particle[1][1] += 0.01  # circles speed
            # if particle[2] &lt;= 0:
            if particle[2] == 0:
                self.particles_list.remove(particle)
            # do not call draw from here: it slows down the frame rate
            # self.draw()

    def draw(self):
        "Draws particles based on data in the self.particles_list"
        if self.turn == "on":
            for particle in self.particles_list:
                pygame.draw.circle(
                    window2, (self.color),
                    (round(particle[0][0]), round(particle[0][1])),
                    round(particle[2]))


p1 = 1
# Some random colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
# Creating the list with particles ready to be drawn

Particles([100, 200], y_dir="up", color=RED)
Particles([100, 200], y_dir="down", color=GREEN)
Particles([200, 100], y_dir="down", color=YELLOW)
Particles([300, 100], y_dir="all", color=BLUE)
Particles([400, 100], y_dir="down", color=CYAN)
Particles([500, 200], y_dir="up", color=GREEN)
Particles([0, 0], y_dir="down", color=WHITE, sparse=1)
Particles([0, 400], y_dir="up", color=YELLOW, sparse=1)
Particles([0, 200], y_dir="up", color=RED, sparse=1)
Particles([0, 200], y_dir="down", color=BLUE, sparse=1)
Particles([100, 200], y_dir="all", color=BLUE, sparse=1)


def generate():
    "Start drawing all circles on the screen"
    for par in group:
        par.generate_particles()
        par.draw()


# ================= INFINITE LOOP ================== #
n = 0  # points to an effect in the group list
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                group[n].turn = "off"
            elif event.key == pygame.K_RIGHT:
                group[n].turn = "on"
            n += 1
            if n > len(group) - 1:
                n = 0
    window2.fill(0)
    generate()
    window.blit(window2, (0, 0))
    clock.tick(60)
    pygame.display.flip()