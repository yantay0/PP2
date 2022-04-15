import random
from re import I
from secrets import randbelow
import sys
import pygame

pygame.init()

FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 5
ENEMTY_STEP = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCORE = 0

clock = pygame.time.Clock()


score_font = pygame.font.SysFont("Verdana", 25)

SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Racer")

bg = pygame.image.load(
    r"C:\Users\Madina\Desktop\mine\python\racer\AnimatedStreet.png")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            r"C:\Users\Madina\Desktop\mine\python\racer\images\coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


    def update(self):
        global SCORE
        self.rect.move_ip(0, ENEMTY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
           # SCORE += 1
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def randomize(self):
     self.top = 0
     self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            r"C:\Users\Madina\Desktop\mine\python\racer\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class MAIN(pygame.sprite.Sprite):
 def __init__(self):
  self.enemy = Enemy()
  self.player = Player()


 def update(self):
  self.player.update()
  self.enemy.update()
  self.check_collision()
 
 def check_collision(self):
  global SCORE
  enemies = pygame.sprite.Group()
  enemies.add(self.enemy)
  if pygame.sprite.spritecollideany(self.player, enemies):
   self.enemy.randomize()
   SCORE+=1
   pygame.mixer.Sound(r'C:\Users\Madina\Desktop\mine\python\racer\coin.wav').play()


 def draw_element(self,surface):
  self.enemy.draw(surface)
  self.player.draw(surface)










P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
#enemies.add(E1)
n = random.randint(0,4)
for i in range (n):
 E1 = Enemy()
 enemies.add(E1)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    main_game.update()
    #enemies.update()
    
    #if pygame.sprite.spritecollideany(P1, enemies):
  
    

    main_game.check_collision()

    SURF.blit(bg, (0, 0))

    #enemies.draw(SURF)
    main_game.draw_element(SURF)

    score_img = score_font.render(str(SCORE), True, BLACK)
    SURF.blit(score_img, (370, 10))

    pygame.display.update()
    clock.tick(FPS)
