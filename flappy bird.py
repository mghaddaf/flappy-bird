import pygame
pygame.init()
WIDTH = 864
LENGTH = 600
TITLE = "flappy bird"
game_over = False
flying = True
run = True
pipe_freq = 3000
last_pipe = pygame.time.get_ticks() - pipe_freq
flappy1 = pygame.image.load(r"Pygame Developer\Images\flappy bird.png")
flappy2 = pygame.image.load(r"Pygame Developer\Images\flappy bird 2.png")
flappy3 = pygame.image.load(r"Pygame Developer\Images\flappy bird 3.png")
pipe = pygame.image.load(r"Pygame Developer\Images\pipe.png")
floor = pygame.image.load(r"Pygame Developer\Images\floor.png")
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
flappy = Flappy(flappy1, 150, 300, 0)
flappys = pygame.sprite.Group()
class Pipes(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        super().__init__()
        self.image = pygame.transform.rotate(image, angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
pipe_s = pygame.sprite.Group()
flappys.add(flappy)
while run:
    screen.blit(background, (0, 0))
    if game_over == False and flying == True:
        if pygame.time.get_ticks() - last_pipe > 3000:
            bottom_pipe = Pipes(pipe, 900, 300, 0)
            top_pipe = Pipes(pipe, 900, -300, 180)
            pipe_s.add(bottom_pipe)
            pipe_s.add(top_pipe)
            last_pipe = pygame.time.get_ticks()
    screen.blit(floor, (0, 525))
    flappys.draw(screen)
    pipe_s.draw(screen)
    for pipe1 in pipe_s:
        pipe1.rect.x = pipe1.rect.x - 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
    pygame.display.update()