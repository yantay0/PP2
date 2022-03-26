import random
import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Backgroung
backgroung = pygame.image.load('clock_mickey.jpg')

# Title and Icon
pygame.display.set_caption("Mickey Mouse Clock")
Icon = pygame.image.load('clock.jpg')
pygame.display.set_icon(Icon)


# Game loop
running = True
while running:

  screen.fill((0, 0, 0))
  # backgroung Image
  screen.blit(backgroung, (0, 0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.update()
