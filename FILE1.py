import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__ (self):
        super (Player, self).__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys [K_UP]:
            self.rect.move_ip(0,-1)
        if pressed_keys [K_DOWN]:
            self.rect.move_ip(0,1)
        if pressed_keys [K_LEFT]:
            self.rect.move_ip(-1,0)
        if pressed_keys [K_RIGHT]:
            self.rect.move_ip(1,0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1024:
            self.rect.right = 1024
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 1280:
            self.rect.bottom = 1280
                        
pygame.init()


screen=pygame.display.set_mode((1280, 1024))

player = Player()

background = pygame.Surface(screen.get_size())
background.fill((255,255,0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False
    screen.blit(background, (0,0))

    pressed_keys = pygame.key.get_pressed()
    player.update (pressed_keys)
    
    screen.blit(player.surf, player.rect)
    pygame.display.flip()
#end pygame
pygame.quit()
