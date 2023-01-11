import pygame
from pygame.locals import(
  K_UP, K_DOWN, K_RIGHT, K_LEFT, K_ESCAPE, KEYDOWN, QUIT
)
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
running = True
surface = pygame.Surface((50, 50))
surface.fill((255, 255, 255))
rect = surface.get_rect()
screen.blit(surface, (screen_width/2, screen_height/2))
pygame.display.flip()
while running:
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.type == K_ESCAPE:
        running = False
    elif event.type == QUIT:
      running = False
class Player(pygame.sprite.Sprite):
