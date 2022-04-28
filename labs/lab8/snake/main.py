import pygame
import sys
import random , time
from pygame.math import Vector2
from pygame import mixer
# initializing pygame
pygame.init()
# timer
font = pygame.font.SysFont('Consolas', 30)
counter, text = 10, '10'.rjust(3)
text = str(counter).rjust(3)
level = 1
snake_color = (0, 0, 255)


class SNAKE:
 def __init__(self):
  self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]  # snake's body
  self.direction = Vector2(1, 0)
  self.new_block = False

 def draw_snake(self):
  for block in self.body:
   x_pos = int(block.x*cell_size)
   y_pos = int(block.y*cell_size)
   block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)  # x y w h
   pygame.draw.rect(screen, (snake_color), block_rect)

 def move_snake(self):
   # if snake eates a fruit body increases by one block (copying the body + new block --> continue moves at the same direction as the head)
  if self.new_block == True:
   body_copy = self.body[:]
   body_copy.insert(0, body_copy[0] + self.direction)
   self.body = body_copy[:]
   self.new_block = False
  else:
   # for another condition the body moves in usual way  i.e. the whole body ( except the head ) copes and moving at the the same direction as the head
   body_copy = self.body[:-1]
   body_copy.insert(0, body_copy[0] + self.direction)
   self.body = body_copy[:]

 def add_block(self):
  self.new_block = True


class FRUIT:
 def __init__(self):
  self.randomize()  # two-dim vector

 def draw_fruit(self):
  fruit_rect = pygame.Rect(int(self.pos.x*cell_size),
                           int(self.pos.y*cell_size), cell_size, cell_size)
  screen.blit(apple, fruit_rect)
 # pygame.draw.rect(screen, (126 , 166 , 114), fruit_rect)
 # -3 cause we do not want to appear fruit randomly on the frame

 def randomize(self):
  self.x = random.randint(0, cell_number - 3)
  self.y = random.randint(0, cell_number - 3)
  self.pos = Vector2(self.x, self.y)

class MAIN:
 def __init__(self):
  # class main inherits all methods from class SNAKE and class FRUIT
  self.snake = SNAKE()
  self.fruit = FRUIT()

 def update(self):
  self.snake.move_snake()
  self.check_collision()
  self.check_fail()

 def draw_element(self):
  self.fruit.draw_fruit()
  self.snake.draw_snake()
  self.draw_score()
 # snake has eaten the fruit

 def check_collision(self):
  if self.fruit.pos == self.snake.body[0]:
    self.fruit.randomize()
    self.snake.add_block()
    mixer.Sound(r'C:\Users\Madina\Desktop\PP2\labs\lab8\snake\resources\1_snake_game_resources_ding.mp3').play()
 # condition to check if a snake has touches itself if it does then tha game is over

 def check_fail(self):
  if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
   self.game_over()
   
  for block in self.snake.body[1:]:
   if block == self.snake.body[0]:
    self.game_over()

 def game_over(self):
   #screen.fill(0,0,255)
   mixer.Sound(
      r'C:\Users\Madina\Desktop\PP2\labs\lab8\snake\resources\1_snake_game_resources_crash.mp3').play()
   time.sleep(2)   
   pygame.quit
   sys.exit()
   '''
 def timer(self):
   global level , counter
   if level == 3 :
     counter -= 1
     text = str(counter).rjust(3) 
     if counter == 0 :
        self.fruit.randomize() 
        counter = 10
     screen.blit(font.render(text, True, (255, 0, 0)), (10, 10))]'''
 #level conditons
 def draw_score(self):
   global level
   if len(self.snake.body)-3 == 5:
     level = 2
   elif len(self.snake.body)-3 == 15:
     level = 3


 # score table
   score_text = str(len(self.snake.body)-3) + f' level : {level}'
   score_surface = game_font.render(score_text, True, (56, 74, 12))
   score_x = int(cell_size*cell_number - 60)
   score_y = int(cell_size*cell_number - 40)
   score_rect = score_surface.get_rect(center=(score_x, score_y))
   apple_rect = apple_score.get_rect(
       midright=(score_rect.left, score_rect.centery))
   bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,
                         apple_rect.width + score_rect.width+6, apple_rect.height)
  

   pygame.draw.rect(screen, (56, 75, 12), bg_rect, 2)
   screen.blit(score_surface, score_rect)
   screen.blit(apple_score, apple_rect)
  



mixer.init()
mixer.Sound(r'C:\Users\Madina\Desktop\PP2\labs\lab8\snake\resources\bg_music_1.mp3').play() # background music


# creation of illuison of a grid
cell_size = 30
cell_number = 20
screen = pygame.display.set_mode(
    (cell_number*cell_size, cell_number*cell_size))  # screen (grid)
clock = pygame.time.Clock()  # for  managing fps per minute
# converts into convinient format pyhton to work with
apple = pygame.image.load(
    r'C:\Users\Madina\Desktop\PP2\labs\lab8\snake\resources\apple.jpg').convert_alpha()
apple_score = pygame.image.load(
    r'C:\Users\Madina\Desktop\PP2\labs\lab8\snake\resources\apple_score.png').convert_alpha()
game_font = pygame.font.Font(
    r'C:\Users\Madina\Desktop\PP2\labs\lab8\snake\resources\PoetsenOne-Regular.ttf', 25)

# the whole game (snake moving , apperince of fruits) is conluded in this class
main_game = MAIN()


SCREEN_UPDATE = pygame.USEREVENT


INC_SPEED = pygame.USEREVENT + 1
set_timer = pygame.time.set_timer(INC_SPEED, 3000)
speed = 150
#snake_speed = pygame.time.set_timer(SCREEN_UPDATE ,speed) # speed

# game loop
while True:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:  # cross is pressed -->  game is finished/closed
   pygame.quit
   sys.exit()
  snake_speed = pygame.time.set_timer(SCREEN_UPDATE, speed)  # speed
  if event.type == SCREEN_UPDATE:
     main_game.update()
     if level == 2:
      speed = 100  # speed
      snake_color = (255, 255, 0)
     if level == 3:
       snake_color = (0, 0, 0)
       speed = 70
  
       counter -= 1
       
       #if event.type == pygame.USEREVENT:
      #pygame.time.set_timer(pygame.USEREVENT, 1000)
       #font = pygame.font.SysFont('Consolas', 30)
      # screen.blit(font.render(text, True, (255, 0, 0)), (10, 10))
  # conditions when a user pressing a button(an arrow)
  if event.type == pygame.KEYDOWN:
   if event.key == pygame.K_UP:
    if main_game.snake.direction.y != 1:
       main_game.snake.direction = Vector2(0, -1)
   if event.key == pygame.K_RIGHT:
    if main_game.snake.direction.x != -1:
     main_game.snake.direction = Vector2(1, 0)
   if event.key == pygame.K_DOWN:
    if main_game.snake.direction.y != -1:
     main_game.snake.direction = Vector2(0, 1)
   if event.key == pygame.K_LEFT:
    if main_game.snake.direction.x != 1:
     main_game.snake.direction = Vector2(-1, 0)

# game going to ignore when the snake tries to pass through itself

 screen.fill((102, 167, 67))  # color of the screen
 text = str(counter).rjust(3)
 screen.blit(font.render(text, True, (255, 0, 0)), (10, 10))
 main_game.draw_element()  # our elements of the game will appear
 pygame.display.update()
 clock.tick(60)  # 60 loops per minute
