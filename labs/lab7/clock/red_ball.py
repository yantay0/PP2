import random
import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))


clock = pygame.time.Clock()

FPS = 60


def move(x, y):
 screen.blit(screen, (x, y))


x = 50
y = 50
vx = 20
vy = 20


running = True
while running:

  dt = clock.tick(FPS)/1000.0

  screen.fill((255, 255, 255))

  ball = pygame.draw.circle(screen, (255, 0, 0), [int(x), int(y)], 25, 0)

  x += vx * dt
  y += vy * dt
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    # keystrokes
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        x -= 20
        vx *= -1
    if key_input[pygame.K_UP]:
        y -= 20
        vy *= -1
    if key_input[pygame.K_RIGHT]:
        x += 20

    if key_input[pygame.K_DOWN]:
        vy += 20

  if y >= 475 or y <= 0:
    vy *= -1
  if x >= 475 or x <= 0:
    vx *= -1

  if x <= 0:
    x += 20
  if y <= 0:
    y += 20
  if y >= 475:
    y -= 20
  if x >= 475:
    x -= 20

  pygame.display.update()
