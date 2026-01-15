import pygame
pygame.init()
WIDTH = 900
LENGTH = 600
TITLE = "flappy bird"
run = True
flappy1 = pygame.image.load(r"Pygame Developer\Images\flappy bird.png")
flappy2 = pygame.image.load(r"Pygame Developer\Images\flappy bird 2.png")
flappy3 = pygame.image.load(r"Pygame Developer\Images\flappy bird 3.png")
background = pygame.image.load(r"Pygame Developer\Images\ground.png")
screen = pygame.display.set_mode((WIDTH, LENGTH))

class Flappy(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        super().__init__()
        self.image = pygame.transform.scale(image, (50, 50))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

while run:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False 
    pygame.display.update()