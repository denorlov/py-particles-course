import random

import pgzrun
import pygame
import course.util

WIDTH = 1000
HEIGHT = 500

X0 = WIDTH // 2
Y0 = HEIGHT // 2

TRANSPARENT_BLACK = pygame.Color(0, 0, 0, 0)
FIRE_COLOR = pygame.Color(226, 88, 34)
BACKGROUND_COLOR = pygame.Color("#000000")

PARTICLE_DIAMETER = 50
PARTICLE_RADIUS = PARTICLE_DIAMETER / 2

PARTICLES_PER_SECOND = 250
EMISSION_DELAY = 1 / PARTICLES_PER_SECOND

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

class Timer:
    def __init__(self, seconds, start_almost_full=True):
        self.delay = seconds
        self.initial_time = seconds - 0.000001 if start_almost_full else 0
        self.time = self.initial_time

    def update(self, dt):
        self.time += dt
        if self.time >= self.delay:
            n, self.time = divmod(self.time, self.delay)
            return int(n)
        return 0

    def reset(self):
        self.time = self.initial_time

class FireSystem:
    def __init__(self):
        self.fire_surface = pygame.Surface((WIDTH, HEIGHT), flags=pygame.SRCALPHA)
        self.is_emitting = False
        self.particle_acceleration = PARTICLE_ACCELERATION
        self.particles = []
        self.emitters = []
        self.emitters.append(Emitter(pygame.mouse.get_pos()))

    def set_emitting(self, is_emitting):
        self.is_emitting = is_emitting
        if not is_emitting:
            for emitter in self.emitters:
                emitter.emission_timer.reset()

    def update(self, dt):
        particle_velocity_change = self.particle_acceleration * dt
        particle_velocity_change_half = particle_velocity_change / 2
        alive_particles = []
        for particle in self.particles:
            particle.update(dt, particle_velocity_change, particle_velocity_change_half)
            if particle.is_alive:
                alive_particles.append(particle)
        self.particles = alive_particles
        for emitter in self.emitters:
            self.particles.extend(
                emitter.update(dt, pygame.mouse.get_pos(), self.is_emitting)
            )

    def draw(self, target_surface):
        self.fire_surface.fill(TRANSPARENT_BLACK)
        for particle in self.particles:
            self.fire_surface.blit(
                particle.image,
                particle.pos,
                special_flags=pygame.BLEND_RGBA_ADD
            )
        target_surface.fill(BACKGROUND_COLOR)
        target_surface.blit(self.fire_surface, (0, 0))

    def clear(self):
        self.particles.clear()


class Emitter:
    def __init__(self, position):
        self.position = pygame.Vector2(position)
        self.emission_timer = Timer(EMISSION_DELAY)

    def update(self, dt, new_position, is_emitting):
        self.position.update(new_position)

        if is_emitting:
            emit_particles_count = self.emission_timer.update(dt)
            if emit_particles_count > 0:
                return self.emit(emit_particles_count)
        return ()

    def emit(self, particles_count):
        return [FireParticle(self.position) for _ in range(particles_count)]


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
        image.blit(transparent_layer, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        images.append(image)

    return images

class FireParticle:
    images = make_particle_images()

    def __init__(self, position:pygame.Vector2):
        self.position = pygame.Vector2(position)
        self.is_alive = True
        self.position = self.position.elementwise() - PARTICLE_RADIUS  # center the image
        self.velocity = pygame.Vector2(random.gauss(SPEED_MEAN, SPEED_SD), 0)
        self.velocity.rotate_ip(random.uniform(0, 360))
        self.image = FireParticle.images[-1]
        self.time = 0
        self.lifetime_limit = random.gauss(LIFETIME_MEAN, LIFETIME_SD)
        self.vanish_start_time = self.lifetime_limit - VANISH_DURATION

    def update(self, dt, velocity_change, velocity_change_half):
        self.time += dt
        if self.time >= self.vanish_start_time:
            if self.time >= self.lifetime_limit:
                self.is_alive = False
                return
            alpha = course.util.linear(
                self.time,
                self.vanish_start_time, self.lifetime_limit,
                255, 0
            )
            self.image = FireParticle.images[int(alpha)]
        self.velocity += velocity_change
        self.position += (self.velocity - velocity_change_half) * dt
        if not PARTICLE_LIMIT_RECT.collidepoint(self.position):
            self.is_alive = False


paused = False
system = FireSystem()
clock = pygame.time.Clock()

def on_mouse_down():
    system.set_emitting(True)

def on_mouse_up():
    system.set_emitting(False)

def on_key_down(key):
    global paused
    if key == keys.SPACE:
        paused = not paused
        pygame.mouse.set_visible(paused)

def update():
    dt_sec = clock.tick(60) / 1000  # in seconds
    if not paused:
        system.update(dt_sec)

def draw():
    system.draw(screen.surface)

    screen.draw.text(f"updates per second: {clock.get_fps():.0f}", (10, 25))
    screen.draw.text(f"number of particles: {len(system.particles)}", (10, 50))
    screen.draw.text(f"number of emitters: {len(system.emitters)}", (10, 75))
    screen.draw.text(f"paused: {paused}", (10, 100))

pgzrun.go()
