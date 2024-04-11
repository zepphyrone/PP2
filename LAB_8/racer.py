#imports
import pygame,sys
import random, time
from pygame.locals import *
pygame.init()

#setting up screen, speed & score
W, H = 338, 600
place = pygame.display.set_mode((338,600))
place.fill("white")
Speed = 5
SCORE = 0

#uploading pic of each creature
pygame.display.set_caption('Racer')
back = pygame.image.load('road.png')
car = pygame.image.load('car.png')
enemy = pygame.image.load('enemy.png')

#setting up FPS
clock = pygame.time.Clock()
FPS = 60

#setting up fonts
end = pygame.font.SysFont('Verdana', 40)
start = pygame.font.SysFont("Verdana", 20)
GameOver = end.render("Game Over", True, "black")
Score = start.render("Your score was", True, "black")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,W-40),0) 
      def move(self):
        global SCORE
        self.rect.move_ip(0,Speed)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, W-40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()   
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < W:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        #self.image = pygame.transform.scale(self.image, (10,10))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,W-40), 530)
    def move(self):
        global SCORE
    def change(self):
        self.rect.center = (random.randint(40,W-40), 530)
 
#setting up sprites 
P1 = Player()
E1 = Enemy()
C1 = Coin()

#creating sprites groups
Enemies = pygame.sprite.Group()
Enemies.add(E1)
Coins = pygame.sprite.Group()
Coins.add(C1)
All_sprites = pygame.sprite.Group()
All_sprites.add(P1)
All_sprites.add(E1)
All_sprites.add(C1)

#adding user event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#game loop
while True:   
    #cycles through all events  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              Speed += 0.5       
        if event.type == pygame.QUIT:
            exit()

    place.blit(back, (0,0))
    total = start.render(str(SCORE), True, "black")
    place.blit(total, (10,10))

    #moves and re-draws all sprites
    for entity in All_sprites:
        entity.move()
        place.blit(entity.image, entity.rect)

    #if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, Enemies):
          pygame.mixer.Sound('crash.mp3').play()
          time.sleep(1)
                    
          place.fill("red")
          place.blit(GameOver, (50,250))
           
          pygame.display.update()
          for entity in All_sprites:
                entity.kill() 
          time.sleep(4)
          pygame.quit()
          exit()

    #case of taking coins
    if pygame.sprite.spritecollideany(P1, Coins):
        pygame.mixer.Sound('collectcoin.mp3').play()
        SCORE += 1
        C1.change()      

    pygame.display.update()
    clock.tick(FPS)