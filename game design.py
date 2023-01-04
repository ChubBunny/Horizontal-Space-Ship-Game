import pygame
pygame.init()
screen = pygame.display.set_mode([500,500])
#A way of setting up boundaries for the game
running = True
while running:
  #Because running is equal to true, andso we can stop the loop by setting the running variable to False
  for event in pygame.event.get():
    #It will keep running as long as you do not tell it to stop
    if event.type == pygame.QUIT: #QUIT = event
      running = False
  screen.fill((255, 255, 255))  
  #Circle arguments: circle(location (screen), color (tuple) , x,y-location, radius)
  pygame.draw.circle(screen, 'blue', (0,0), 20)
  pygame.display.flip()
pygame.quit() #quit() function
