import pygame
import button

pygame.init()
WINDOW_WIDTH = 650
WINDOW_HEIGHT = 500

# Defining Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
YELLOW = (255, 255, 0)

# creating a screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
baselayer = pygame.Surface((WINDOW_WIDTH,WINDOW_HEIGHT))
baselayer.fill(WHITE)
screen.fill(WHITE)
clock = pygame.time.Clock()

# selector pallete
selector_rect = pygame.Rect(1, 8, 166, 68)
col_1 = pygame.Rect(7, 12, 27, 27)
col_2 = pygame.Rect(37, 12, 27, 27)
col_3 = pygame.Rect(67, 12, 27, 27)
col_4 = pygame.Rect(98, 10, 32, 32)
col_5 = pygame.Rect(131, 10, 32, 32)
col_6 = pygame.Rect(7, 42, 27, 27)
col_7 = pygame.Rect(37, 42, 27, 27)
col_8 = pygame.Rect(67, 42, 27, 27)
col_9 = pygame.Rect(98, 42, 32, 32)
col_10 = pygame.Rect(131, 42, 32, 32)

def draw_selector():
  pygame.draw.rect(screen, (186, 192, 192), selector_rect, 100)
  pygame.draw.rect(screen, BLACK, col_1, 20)
  pygame.draw.rect(screen, RED, col_2, 20)
  pygame.draw.rect(screen, GREEN, col_3, 20)
  pygame.draw.rect(screen, BLACK, col_4, 1)
  pygame.draw.rect(screen, BLACK, col_5, 1)
  pygame.draw.rect(screen, BLUE, col_6, 20)
  pygame.draw.rect(screen, PINK, col_7, 20)
  pygame.draw.rect(screen, YELLOW, col_8, 20)
  pygame.draw.rect(screen, BLACK, col_9, 1)
  pygame.draw.rect(screen, BLACK, col_10, 1)
  screen.blit(pen_Im, (131, 40))
  screen.blit(eraser_Im, (98, 40))
  screen.blit(rect_Im, (98, 10))
  screen.blit(circle_Im,(131,10))


def pencil():
    global prev
    pygame.draw.line(screen, current_color, prev, cur, 5)
    prev = cur


# draw rectangle mode
prevX = 0
prevY = 0
currentX = 0
currentY = 0
isMouseDown = False


def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculateCircle(x1, y1, x2, y2):
    r = max(abs(x2 - x1), abs(y2 - y1))
    pygame.draw.circle(screen, current_color, (x1, y1), r)

#buttons
pen_Im = pygame.image.load(
    r'C:\Users\Madina\Desktop\mine\python\paint\images\pen.png').convert_alpha()
eraser_Im = pygame.image.load(
    r'C:\Users\Madina\Desktop\mine\python\paint\images\eraser.png').convert_alpha()
rect_Im = pygame.image.load(
    r'C:\Users\Madina\Desktop\mine\python\paint\images\rect.png').convert_alpha()
circle_Im = pygame.image.load(
    r'C:\Users\Madina\Desktop\PP2\labs\lab8\paint\images\circle.png').convert_alpha()

pen_button = button.Button(131, 40, pen_Im, 0.8)
eraser_button = button.Button(98, 40, eraser_Im, 0.8)
rect_button = button.Button(98, 10, rect_Im, 0.8)
circle_button = button.Button(131,10,circle_Im,0.8)


current_color = BLACK
prev, cur = None, None  # variables for pencil button

pen_tool = False
rect_tool = False
eraser_tool = False

running = True
while running:
 if pen_button.draw(screen):
    pen_tool = True
    rect_tool = False
    current_color = BLACK
 if eraser_button.draw(screen):
   current_color = WHITE
   pen_tool = True
   rect_tool = False

 if rect_button.draw(screen):
   rect_tool = True
   pen_tool = False
   current_color = BLACK

# if circle_button.draw(screen):
 #       circle_tool = True




 for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if pen_tool:
     rect_tool = False
     if event.type == pygame.MOUSEBUTTONDOWN:
        prev = pygame.mouse.get_pos()
     if event.type == pygame.MOUSEMOTION:
      cur = pygame.mouse.get_pos()
      if prev:
         pencil()
     if event.type == pygame.MOUSEBUTTONUP:
      prev = None
    if rect_tool :
          pen_tool = False
          if event.type == pygame.MOUSEBUTTONDOWN:
               if event.button == 1:
                    isMouseDown = True
                    currentX  = event.pos[0]
                    currentY = event.pos[1]
                    prevX = event.pos[0]
                    prevY = event.pos[1]

          if event.type == pygame.MOUSEBUTTONUP:
               isMouseDown = False
               baselayer.blit(screen, (0, 0))

          if event.type == pygame.MOUSEMOTION:
               if isMouseDown:
                    currentX = event.pos[0]
                    currentY = event.pos[1]
 #if rect_button: 
 if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
      screen.blit(baselayer, (0, 0))
      r = calculateRect(prevX, prevY, currentX, currentY)
      pygame.draw.rect(screen, BLACK, pygame.Rect(r), 1)
      if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1:
          screen.blit(baselayer, (0, 0))
          r = calculateRect(prevX, prevY, currentX, currentY)
          pygame.draw.rect(screen, current_color, pygame.Rect(r), 1)


  # COLOR SELECTION
 select = pygame.mouse.get_pressed()
 if select[0] == 1:
      mouse_pos = pygame.mouse.get_pos()
      if 7 < mouse_pos[0] < 34 and 12 < mouse_pos[1] < 39:
          current_color = BLACK
      elif 37 < mouse_pos[0] < 64 and 12 < mouse_pos[1] < 39:
          current_color = RED
      elif 67 < mouse_pos[0] < 94 and 12 < mouse_pos[1] < 39:
          current_color = GREEN
      elif 7 < mouse_pos[0] < 34 and 42 < mouse_pos[1] < 69:
          current_color = BLUE
      elif 37 < mouse_pos[0] < 64 and 42 < mouse_pos[1] < 69:
          current_color = PINK
      elif 67 < mouse_pos[0] < 94 and 42 < mouse_pos[1] < 69:
          current_color = YELLOW

 draw_selector()

 pygame.display.flip()
 clock.tick(30)

