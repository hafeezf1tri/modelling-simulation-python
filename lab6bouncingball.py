import sys

import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pymunk - bouncing ball")
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 900)

floor = pymunk.Segment(space.static_body, (50, 550), (750, 550), 5)
floor.elasticity = 0.9
floor.friction = 0.8
space.add(floor)

mass = 1
radius = 25
moment = pymunk.moment_for_circle(mass, 0, radius)

body = pymunk.Body(mass, moment)
body.position = (400, 100)

ball = pymunk.Circle(body, radius)
ball.elasticity = 0.9
ball.friction = 0.5
space.add(body, ball)

draw_options = pymunk.pygame_util.DrawOptions(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            body.position = (400, 100)
            body.velocity = (0, 0)

    screen.fill((255, 255, 255))
    space.step(1 / 60)
    space.debug_draw(draw_options)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()