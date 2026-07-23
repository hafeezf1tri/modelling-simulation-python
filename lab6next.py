import pygame
import pymunk
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 900)

mass = 1
radius = 20

moment = pymunk.moment_for_circle(mass, 0, radius)

body = pymunk.Body(mass, moment)
body.position = (400, 100)

ball = pymunk.Circle(body, radius)

space.add(body,ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    x,y = body.position

    pygame.draw.circle(screen, (0, 0, 255), (int(x), int(y)), radius)

    space.step(1/60.0)

    pygame.display.flip()

    clock.tick(60)
