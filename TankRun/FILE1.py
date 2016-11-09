import pygame
import random
from pygame.locals import *
import time

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self) .__init__()
        self.image = pygame.image.load('player.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        
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
        if self.rect.right > 820:
            self.rect.right = 820
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 900:
            self.rect.bottom = 900
            
class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super(Opponent,self). __init__ ()
        self.image = pygame.image.load('Enemy.png').convert ()
        self.image.set_colorkey((255, 255, 255,), RLEACCEL)
        self.rect=self.image.get_rect(
            center= (1000,  random.randint(0, 600))
                                      )
        self.speed = random.randint (1,3)


    def update(self):
            self.rect.move_ip(-self.speed, 0)
            if self.rect.right < 0:
                self.kill()



screen=pygame.display.set_mode((820, 900))

player = Player()

done = 0
pygame.init()
myfont = pygame.font.SysFont("times",25)
background = pygame.Surface(screen.get_size())
background.fill((219, 172, 135))
players = pygame.sprite.Group()
opponents = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
ADDOPPONENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADDOPPONENT, 250)
start_ticks = 0
running = True
clock = pygame.time.Clock()
fps = 1000
while running:
    

    clock.tick(fps)
    start_ticks = pygame.time.get_ticks()
    seconds = pygame.time.get_ticks()/1000
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                    

        elif event.type == QUIT:
            running = False
        elif(event.type == ADDOPPONENT):
            new_opponent = Opponent()
            opponents.add(new_opponent)
            all_sprites.add(new_opponent)
    screen.blit(background, (0,0))

    pressed_keys = pygame.key.get_pressed()
    player.update (pressed_keys)
    opponents.update()
    if done == 0:
        timetext = myfont.render("time = " + str(seconds),1,(0,0,0))
    screen.blit(timetext, (5,10))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    

    if pygame.sprite.spritecollideany(player, opponents):
        player.kill()
        if done == 0:
            print ('You died after ' + str(seconds) + ' seconds.')
            done = 1
    pygame.display.flip()
#end pygame
pygame.quit()
