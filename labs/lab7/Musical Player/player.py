from os import curdir
import pygame , re
from pygame import mixer

# Initializing pygame
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 18)
font_for_guide = pygame.font.Font('freesansbold.ttf', 16)


# Creating screen
WIDTH = 780
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
music_note = pygame.image.load('images/musical-note.png')
music_noteX = 262
music_noteY = 65

waves = pygame.image.load('images/sound-waves.png')
wavesX = 700
wavesY = 375

book = pygame.image.load('images/book.png')
bookX = 660
bookY = 490
#coordinates for images + display
def images(image , x , y):
	screen.blit(image , (x , y))

# Loading playlist
music_list = ['playlist/Hat Trick Remix feat Jadakiss Cam James Clyde Kelly J Writin.mp3', 
              'playlist/I Just Died In Your Arms - Cutting Crew.mp3',
              'playlist/Peaches   Justin Bieber feat. Daniel Caesar, Giveon.mp3']

# song names
names=[]
for name in music_list:														
 names.append(re.sub(".mp3" , "" , f'{name}'))

def guide(x, y):
    text = ("Space-Press To Start; P-To Pause; C-To Continue; Right/Left Arrow For Next/Prev")
    guide_text = font_for_guide.render(text, True, (0, 0, 0))
    screen.blit(guide_text, (x, y))

#playlist
number = 0
def currentmusic(number):
    music_name = font.render(re.sub('playlist/' , ''  , f'Song name : {names[number]}'), True, (0, 0, 0))
    screen.blit(music_name, (20 , 400))


# Game loop
running = True
while running:
  screen.fill((255, 255, 255))
 #event handeler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
                mixer.music.load(music_list[number])
                mixer.music.play()
                mixer.music.queue(music_list[number + 1])
                mixer.music.queue(music_list[number + 2])

      if event.key == pygame.K_p:
                mixer.music.pause()
      if event.key == pygame.K_c:
                mixer.music.unpause()
      if event.key == pygame.K_RIGHT:
                mixer.music.stop()
                if number < len(music_list) - 1:
                    mixer.music.load(music_list[number + 1])
                    mixer.music.play()
                    number += 1
                else:
                    number = 0

                    mixer.music.load(music_list[number])
                    mixer.music.play()

      if event.key == pygame.K_LEFT:
                mixer.music.stop()
                if number > 0:
                    mixer.music.load(music_list[number - 1])
                    mixer.music.play()
                    number -= 1
                elif number == 0:
                    mixer.music.load(music_list[len(music_list) - 1])
                    mixer.music.play()
                    number = len(music_list) - 1

    guide(20, 520)
    if number == 0:
        currentmusic(number)
        wavesX = 700
    if number == 1:
        currentmusic(number)
        wavesX = 500
    if number == 2:
        currentmusic(number)		
        wavesX = 600
   	
    images(music_note, music_noteX, music_noteY)
    images(waves , wavesX , wavesY)
    images(book , bookX , bookY)
    
    pygame.display.update()


