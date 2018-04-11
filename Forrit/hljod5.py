import pygame
import sys
import time

pygame.init()

grey = (211,211,211)
red =  (155, 50, 150)
blue = (0,0,238)
black = (0,0,0)
size = [600, 700]
done = False
txt = 'Til hamingju, þú hefur unnið leikjaland!'
txt1 = 'Sigurvegari'

str1= pygame.font.get_default_font()
gameDisplay = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.mixer.music.load('AllIdoiswin.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

def text_objects(text,font):
    textSurface=font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def message_display(text):
    texti = pygame.font.Font(str1,20)
    TextSurf, TextRect = text_objects(text, texti)
    TextRect.center = ((600/2),(700/2))
    if text==txt1:
        TextRect.center = ((300),(670))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

myImage = pygame.image.load('winner.gif')
myImage = pygame.transform.scale(myImage,size)
gameDisplay.blit(myImage,(0,0))
pygame.display.update()
message_display(txt)
message_display(txt1)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #haettir ekki fyrr en ytt er a close
            done = True
pygame.quit()
