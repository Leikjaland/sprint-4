import sys
import time
import pygame
from pygame.locals import QUIT
from pygame.mixer import Sound


def main():
    pygame.init()
    size = 680, 680
    rCBack = ( 27, 27, 27 )

    screen = pygame.display.set_mode( size )
    screen.fill( rCBack )
    pygame.display.set_caption( "Play Sound using PyGame" )

    #  Load image
    img = pygame.image.load( "winner.gif" )

    #  Create Sound Object and play sound
    #sound = Sound( "AllIdoiswin.mp3" )
    #sound.play()

    #  Stop music after 1 sec
    #time.sleep( 0.2 )
    #sound.stop()

    #  Play the sound again
    #sound.play()

    #  Load background music
    pygame.mixer.music.load( "AllIdoiswin.mp3" )
    pygame.mixer.music.play()

    while True:
        screen.blit( img, ( 30, 30 ) )

        for evt in pygame.event.get():
            if evt.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    main()
