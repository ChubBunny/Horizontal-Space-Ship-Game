import pygame
import random
from pygame.locals import(
  K_UP, K_DOWN, K_RIGHT, K_LEFT, K_ESCAPE, KEYDOWN, QUIT
)
screen_width = 800
screen_height = 600
surface = pygame.Surface((50, 50))
surface.fill((255, 255, 255))
rect = surface.get_rect()
screen.blit(surface, (screen_width/2, screen_height/2))
pygame.display.flip()
class Player(pygame.sprite.Sprite):
  pygame.init()
  def __init__(self):
    super(Player, self).__init__()
    self.surf = pygame.Surface((75,25))
    self.surf.fill((255, 255, 255))
    self.rect = self.surf.get_rect()
  def update(self, pressed_keys):
    if pressed_keys[K_UP]:
      self.rect.move_ip(0, -5)
    if pressed_keys [K_DOWN]:
      self.rect.move_ip(0, 5)
    if pressed_keys[K_RIGHT]:
      self.rect.move_ip(5, 0)
    if pressed_keys[K_LEFT]:
      self.rect.move_ip(-5, 0)
    if self.rect.left < 0:
      self.rect.left = 0
    if se;f.rect.right > screen_width:
      self.rect.right = screen_width
    if self.rect.top <= 0:
      self.rect.top = 0
    if self.rect.bottom >= screen_height:
      self.rect.bottom = screen_height
      
class Enemy(pygame.sprite.Sprite):
  def __init__(self):
    super(Enemy, self).__init__()
    self.surf = pygame.Surface((20,10))
    self.surf.fill((255, 255, 255))
    self.rect = self.surf.get_rect(
      center = (
        random.randint(screen_width+20, screen_width+100)
        random.randint(0, screen_height)
        )
      )
      self.speed = random.randint(5, 20)
screen = pygame.display.set_mode([screen_width, screen_height])
player = Player()
running = True
while running:
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.type == K_ESCAPE:
        running = False
    elif event.type == QUIT:
      running = False
  screen.fill((0, 0, 0))
  screen.blit(player.surf, (screen_width/2, screen_height/2)
  pygame.display.flip()
 
              
              
              
              
      
