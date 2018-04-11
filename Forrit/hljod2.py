import pygame
import sys
import time
import select
#import graphics
from graphics import *

red = (155, 50, 150)
done = False

pygame.init()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mixer.music.load('AllIdoiswin.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

#screen = pygame.display.set_mode((620,700))
win = GraphWin("Sigurvegari", 620, 700)
myImage = Image(Point(300,300), "winner.gif")
myImage.draw(win)
txt = Text(Point(300,650),'Til hamingju, þú hefur unnið leikjaland!')
txt.draw(win)
#pygame.time.wait(2000)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #haettir ekki fyrr en ytt er a close
            done = True


#        pygame.display.update()
#    pygame.display.flip()
win.close()
pygame.quit()
