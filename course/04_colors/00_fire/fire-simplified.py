import random

import pgzrun
import pygame
from pygame.constants import BLEND_RGBA_SUB
from pygame.math import Vector2

from course.util import linear

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

TRANSPARENT_BLACK = pygame.Color(0, 0, 0, 0)
FIRE_COLOR = pygame.Color(226, 88, 34)
BACKGROUND_COLOR = pygame.Color(0, 0, 0, 255)

PARTICLE_DIAMETER = 50
PARTICLE_RADIUS = PARTICLE_DIAMETER / 2

PARTICLES_PER_SECOND = 250

LIFETIME_MEAN = 1  # seconds
LIFETIME_SD = 0.1
# Time in seconds it takes for a particle to vanish. The particles start
# vanishing at lifetime - vanish_duration and die when time >= lifetime.
VANISH_DURATION = 0.5
SPEED_MEAN = 100  # pixels per second
SPEED_SD = 25

PARTICLE_ACCELERATION = pygame.Vector2(0, -400)  # updraft

PARTICLE_LIMIT_RECT = pygame.Rect(-PARTICLE_DIAMETER, -PARTICLE_DIAMETER, 0, 0)
PARTICLE_LIMIT_RECT.size = (WIDTH, HEIGHT)
PARTICLE_LIMIT_RECT.width += PARTICLE_DIAMETER
PARTICLE_LIMIT_RECT.height += PARTICLE_DIAMETER * 3  # allow to briefly go below the window

def make_particle_images():
    base_image = pygame.Surface((PARTICLE_DIAMETER, PARTICLE_DIAMETER), flags=pygame.SRCALPHA)
    max_distance = (PARTICLE_DIAMETER - 1) / 2
    center = pygame.Vector2(max_distance)
    for x in range(PARTICLE_DIAMETER):
        for y in range(PARTICLE_DIAMETER):
            # linear interpolation (not how real light behaves)
            position = (x, y)
            distance = center.distance_to(position)
            ratio = min(distance / max_distance, 1)
            color = FIRE_COLOR.lerp(TRANSPARENT_BLACK, ratio)
            base_image.set_at(position, color)

    # Generate a list of images with varying transparency. Pygame doesn't let me mix
    # per pixel alpha and surface alpha so I have to blit a semitransparent layer
    # on the base image to achieve this effect.
    # The index corresponds to the transparency where 0 is transparent and 255 is opaque.
    images = []
    transparent_layer = pygame.Surface(base_image.get_size(), flags=pygame.SRCALPHA)
    for alpha in range(255, -1, -1):
        image = base_image.copy()
        transparent_layer.fill((0, 0, 0, alpha))
        image.blit(transparent_layer, (0, 0), special_flags=BLEND_RGBA_SUB)
        images.append(image)

    return images

class FireSystem:
    def __init__(self):
        self.fire_surface = pygame.Surface((WIDTH, HEIGHT), flags=pygame.SRCALPHA)
        self.is_emitting = False
        self.particles = []

    def set_emitting(self, is_emitting):
        self.is_emitting = is_emitting

    def toggle_emitting(self):
        if self.is_emitting:
            self.set_emitting(False)
        else:
            self.set_emitting(True)

    def update(self, dt):
        alive_particles = []
        for particle in self.particles:
            particle.update(dt)
            if particle.is_alive:
                alive_particles.append(particle)
        self.particles = alive_particles
        self.particles.extend(
            [FireParticle(pygame.mouse.get_pos(), PARTICLE_ACCELERATION) for _ in range(3)]
        )

    def draw(self, target_surface):
        self.fire_surface.fill(TRANSPARENT_BLACK)
        for particle in self.particles:
            self.fire_surface.blit(
                particle.image,
                particle.pos,
                special_flags=pygame.BLEND_RGBA_ADD
            )
            # screen.draw.circle(particle.pos, radius=PARTICLE_RADIUS, color=(255, 255, 0))
        target_surface.fill(BACKGROUND_COLOR)
        target_surface.blit(self.fire_surface, (0, 0))



class FireParticle:
    images = make_particle_images()

    def __init__(self, pos:Vector2, acc:Vector2):
        self.is_alive = True
        self.pos = pygame.Vector2(pos)
        self.pos = self.pos - Vector2(PARTICLE_RADIUS, PARTICLE_RADIUS)  # center the image
        self.velocity = Vector2(random.gauss(SPEED_MEAN, SPEED_SD), 0)
        self.velocity.rotate_ip(random.uniform(0, 360))
        self.acc = acc
        self.image = FireParticle.images[-1]
        self.time = 0
        self.lifetime_limit = random.gauss(LIFETIME_MEAN, LIFETIME_SD)
        self.vanish_start_time = self.lifetime_limit - VANISH_DURATION

    def update(self, dt):
        self.time += dt
        if self.time >= self.vanish_start_time:
            if self.time >= self.lifetime_limit:
                self.is_alive = False
                return

            alpha = linear(
                self.time,
                self.vanish_start_time, self.lifetime_limit,
                255, 0
            )

            self.image = FireParticle.images[int(alpha)]

        self.velocity += self.acc * dt
        self.pos += self.velocity * dt

        if not PARTICLE_LIMIT_RECT.collidepoint(self.pos):
            self.is_alive = False


paused = False
particles_system = FireSystem()
particles_system.is_emitting = True
clock = pygame.time.Clock()

def on_mouse_up():
    particles_system.toggle_emitting()

def on_key_down(key):
    global paused
    if key == keys.SPACE:
        paused = not paused
        pygame.mouse.set_visible(paused)

def update():
    global counter

    dt_sec = clock.tick(60) / 1000  # in seconds
    if not paused:
        particles_system.update(dt_sec)
        counter += 1


counter = 0
test_surface = pygame.Surface((PARTICLE_DIAMETER, PARTICLE_DIAMETER), flags=pygame.SRCALPHA)

def draw():
    screen.fill((0,0,0))
    particles_system.draw(screen.surface)

    img_num = counter % len(FireParticle.images)

    screen.draw.text(f"updates per second: {clock.get_fps():.0f}", (10, 25))
    screen.draw.text(f"number of particles: {len(particles_system.particles)}", (10, 50))
    screen.draw.text(f"imgs: {len(FireParticle.images)}, img_n {img_num}", (10, 75))
    screen.draw.text(f"paused: {paused}", (10, 100))

    screen.surface.blit(FireParticle.images[img_num], (10, 125))

    test_surface.fill(TRANSPARENT_BLACK)

    upper_idx = counter % len(FireParticle.images)

    for img in FireParticle.images[upper_idx-3:upper_idx]:
        test_surface.blit(img, (0,0), special_flags=pygame.BLEND_RGBA_ADD)
    screen.surface.blit(test_surface, (10, 200))

pgzrun.go()
