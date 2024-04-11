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
N = 10

#uploading pic of each creature
pygame.display.set_caption('Racer')
back = pygame.image.load("road.png")

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
      def update(self):
        self.rect.move_ip(0,Speed)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, W-40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def update(self):
        pressed_keys = pygame.key.get_pressed()   
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < W:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, image_path, score):
        super().__init__() 
        self.image = pygame.image.load(image_path)
        #self.image = pygame.transform.scale(self.image, (10,10))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,W-40), 530)
        self.score = score
    def change(self):
        self.rect.center = (random.randint(40,W-40), 530)
 
#setting up sprites 
P1 = Player()
E1 = Enemy()
C1 = Coin("coin.png", 1)
C2 = Coin("coin1.png", 2)
C3 = Coin("gem.png", 5)

Coins_chose = [C1, C2, C3]
Coins_now = random.choice(Coins_chose)

#creating sprites groups
Enemies = pygame.sprite.Group()
Enemies.add(E1)
Coins = pygame.sprite.Group()
Coins.add(Coins_now)
All_sprites = pygame.sprite.Group()
All_sprites.add(P1)
All_sprites.add(E1)
All_sprites.add(Coins_now)

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
        entity.update()
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
    a = 0
    if pygame.sprite.spritecollideany(P1, Coins):
        pygame.mixer.Sound('collectcoin.mp3').play()
        SCORE += Coins_now.score
        Coins_now.kill()
        Coins_now = random.choice(Coins_chose) #choses new coins
        Coins_now.change()
        Coins.add(Coins_now)
        All_sprites.add(Coins_now)
        a += 1

    if a>=N: #case when player earns N coins
        Speed += 1
        N += 10

    pygame.display.update()
    clock.tick(FPS)