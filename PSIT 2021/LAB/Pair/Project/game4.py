import pygame
pygame.init()
sceen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("GAME.PY")
icon = pygame.image.load("rockman - Copy.png")
pygame.display.set_icon(icon)
background = pygame.image.load("bg.jpg")
player = pygame.image.load("rockman.png")
player = pygame.transform.scale(player, (50,50))
# Define constants for the screen width and height
posx = 350
posy = 400
move = 5

while True:
    pygame.time.delay(12)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and posx > 0:
            posx -= move
        if keys[pygame.K_RIGHT] and posx < 700-50:
            posx += move
    sceen.blit(background,(0, 0))
    sceen.blit(player, (0, 0))
    pygame.display.update()