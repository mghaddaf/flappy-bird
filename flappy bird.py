import pygame
pygame.init()
WIDTH = 864
LENGTH = 600
TITLE = "flappy bird"
floor_x = 0
game_over = False
flying = False
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
    def __init__(self, x, y, angle):
        super().__init__()
        self.images = [flappy1, flappy2, flappy3]
        self.index = 0
        self.counter = 0
        self.image = pygame.transform.scale(self.images[self.index], (50, 50))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        if flying == True:
            self.counter = self.counter + 1
            if self.counter >= 10:
                self.counter = 0
                self.index = self.index + 1
                if self.index == 3:
                    self.index = 0
                    self.image = pygame.transform.scale(self.images[self.index], (50, 50))
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
            top_pipe = Pipes(pipe, 900, -400, 180)
            pipe_s.add(bottom_pipe)
            pipe_s.add(top_pipe)
            last_pipe = pygame.time.get_ticks()
    pipe_s.draw(screen)
    screen.blit(floor, (floor_x, 525))
    flappys.draw(screen)
    for pipe1 in pipe_s:
        pipe1.rect.x = pipe1.rect.x - 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
    floor_x = floor_x - 1
    if floor_x <= -36:
        floor_x = 0
    pygame.display.update()