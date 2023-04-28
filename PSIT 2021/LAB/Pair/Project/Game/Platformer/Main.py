import pygame, sys
from Setting import *
from Level import *
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Test")
#setframe rate
clock = pygame.time.Clock()
FPS = 60
#player action variables
moving_left = False
moving_right = False

BG = (0, 0, 0)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')

    pygame.display.update()
    clock.tick(FPS)