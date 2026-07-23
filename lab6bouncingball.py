import pygame
import pymunk
import pymunk.pygame_util
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600   

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pymunk - bouncing ball")

clock = pygame.time.Clock()