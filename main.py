import pygame, sys
from settings import *
from level import Level

pygame.init()
pygame.display.set_caption('That one Game')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
level = Level(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')


    pygame.display.update()
    clock.tick(60)