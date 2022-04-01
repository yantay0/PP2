import pygame
from math import pi, cos, sin
import datetime

WIDTH, HEIGHT = 600, 450
center = (WIDTH / 2, HEIGHT / 2)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Backgroung
backgroung = pygame.image.load('clock_mickey.jpg')
# Title and Icon
pygame.display.set_caption('Mickey Mouse Clock')
Icon = pygame.image.load('clock.png')
pygame.display.set_icon(Icon)


clock = pygame.time.Clock()
FPS = 60



# color for the arrows
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#rotation
def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x + WIDTH / 2, -(y - HEIGHT / 2)



running = True
while running:

  screen.fill((0, 0, 0))
  # backgroung Image
  screen.blit(backgroung, (0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  current_time = datetime.datetime.now()
  second = current_time.second
  minute = current_time.minute

  # Minute
  r = 77  
  theta = (minute + second / 60) * (360 / 60)

  pygame.draw.line(screen, BLACK, center,
                   polar_to_cartesian(r, theta), 10)

  # Second
  r = 98
  theta = second * (360 / 60)
  pygame.draw.line(screen, RED, center, polar_to_cartesian(r, theta), 4)

  pygame.display.update()

  clock.tick(FPS)
