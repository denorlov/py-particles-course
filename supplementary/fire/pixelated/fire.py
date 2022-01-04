import pygame as pg
import traceback
from random import uniform, choice
from os import path

vec = pg.math.Vector2
vec3 = pg.math.Vector3
Color = pg.Color

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def lerp_colors(color, start, end, dist):
    color.r, color.g, color.b = list(map(lambda x: int((x[0] * (1 - dist)) +
                                                       (x[1] * dist)), zip(start[:3], end[:3])))


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((800, 600))
        self.screen_rect = self.screen.get_rect()
        self.fps = 60
        self.all_sprites = pg.sprite.Group()
        try:
            dir_path = path.dirname(path.abspath(__file__))
            filename = path.join(dir_path, 'fire_particles_strip.png')
            p_image_strip = pg.image.load(filename).convert_alpha()
            self.p_images = [p_image_strip.subsurface(((i * 40, 0), (40, 40)))
                             for i in range(4)]
        except:
            traceback.print_exc()
            # if loading the image fails, create some dummy images
            self.p_images = []
            for i in range(4):
                surf = pg.Surface((20, 20), pg.SRCALPHA)
                surf.fill(WHITE)
                self.p_images.append(surf)

        self.create_particle((self.screen_rect.w / 4 * 3,
                              self.screen_rect.h - 30))

    def create_particle(self, pos):
        # create a list of colors for a gradient over time
        # this looks something like a fire:
        colors = [
            Color(255, 255, 180),
            Color(255, 200, 0),
            Color(200, 50, 0),
            Color(140, 70, 20),
            Color(50, 50, 70)
        ]
        # instantiate a paticle with a reference to the particle images
        # and the list of colors
        Particle(self, pos, self.p_images, colors)

    def update(self):
        # create particles every frame
        self.create_particle(pg.mouse.get_pos())

        self.all_sprites.update()
        # print(self.all_sprites.sprites()[0].color)

    def draw(self):
        self.screen.fill(BLACK)
        for s in self.all_sprites:
            s.draw(self.screen)

        pg.display.update()

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(self.fps)
            caption = 'FPS: {} | number of particles: {}'.format(
                int(self.clock.get_fps()),
                len(self.all_sprites))
            pg.display.set_caption(caption)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.update()
            self.draw()

        pg.quit()


class Particle(pg.sprite.Sprite):
    def __init__(self, game, pos, images=None, colors=[]):
        super().__init__()
        self.game = game
        self.game.all_sprites.add(self)

        if images:
            # if initialized with a list of images, choose one at random
            self.original_image = choice(self.game.p_images).copy()
            self.image = self.original_image.copy()
            self.rect = self.image.get_rect()
        else:
            # if not initialized with images, draw a circle
            self.image = pg.Surface((20, 20))
            self.image.set_colorkey((0, 0, 0))
            self.rect = self.image.get_rect()
            pg.draw.ellipse(self.image, (255, 255, 255), self.rect)
        self.colors = colors
        self.color = self.colors[0]
        self.alpha = 255
        if len(self.colors) > 1:
            self.prev_color = self.colors[0]
            self.target_color = self.colors[1]
            self.target_index = 1
        self.lerp_dist = 0
        self.lerp_speed = 0.07

        self.pos = vec(pos)
        self.rect.topleft = self.pos
        # set random velocity vector
        self.vel = vec(uniform(-0.6, 0.6), uniform(-3, -2))

    def update(self):
        # add velocity to position
        self.pos += self.vel
        # update rect
        self.rect.topleft = self.pos
        # reduce alpha gradually
        self.alpha -= 2
        if self.alpha < 0:
            self.kill()
        else:
            self.color.a = int(self.alpha)

    def draw(self, screen):
        self.blend_colors()
        self.image = self.original_image.copy()
        self.image.fill(self.color, None, pg.BLEND_RGBA_MULT)

        screen.blit(self.image, self.pos)

    def blend_colors(self):
        if len(self.colors) > 1:
            if self.lerp_dist < 1:
                # linear interpolation between previous and target color
                lerp_colors(self.color, self.prev_color,
                            self.target_color, self.lerp_dist)
                self.lerp_dist += self.lerp_speed
            else:
                # if lerp distance reached 1, set the next target color
                self.target_index += 1
                if self.target_index < len(self.colors):
                    self.prev_color = self.target_color
                    self.target_color = self.colors[self.target_index]
                    self.lerp_dist = 0


if __name__ == '__main__':
    try:
        g = Game()
        g.run()
    except Exception:
        traceback.print_exc()
        pg.quit()