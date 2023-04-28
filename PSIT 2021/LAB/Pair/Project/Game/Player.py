import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('white')
        self.rect = self.image.get_rect(topleft = pos)

        #Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.flip = False
        self.speed = 5
        self.gravity = 0.8
        self.jump_height = -16

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.flip = False

        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.flip = True
        else:
            self.direction.x = 0

        if keys[pygame.K_w]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_height



    def update(self):
        self.get_input()