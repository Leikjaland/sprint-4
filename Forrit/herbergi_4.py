import random
import graphics
from graphics import *
import pygame
import sys
import time

leikmadur = 0
class Herbergi_4():
    #print('herb4-test#1')
    def __init__(self,leikmadur):
        self.leikmadur= leikmadur

    def mynd_3(self,leikmadur):
        #print('herb4-test#2')
        win = GraphWin("Lokaborð", 800, 700)
        myImage = Image(Point(400,350), "lokaherbergi.gif")
        myImage.draw(win)
        txt = Text(Point(400,50),'Til hamingju! Þú hefur náð að klára þrautirnar og ert því komin/n í lokaherbergið')
        txt1 = Text(Point(400,650),'Leikjaland')
        txt.draw(win)
        txt1.draw(win)
        time.sleep(11)
        win.close()
        win = GraphWin("Lokaborð", 1000, 500)
        myImage = Image(Point(500,250), "lokamynd.gif")
        myImage.draw(win)
        txt = Text(Point(460,50),'Hér bíða þín nokkrir skemmtilegir leikmenn sem vilja spila við þig:')
        txt1 = Text(Point(450,450),'Haraldur Pottur, Hans, Gréta, Sigmundur Davíð og Gylfi Sig landsliðsmaður. Við hvaða leikmann viltu spila?')
        txt.draw(win)
        txt1.draw(win)
        time.sleep(11)
        win.close()
        self.lokaherbergi(leikmadur)

    def lokaherbergi(self,leikmadur):
        #print('herb4-test#3')
        n = random.randint(1, 99)
        #print(n)
        #print("Haraldur Pottur, Hans, Greta, Sigmundur David, Gylfi Sig landslidsmadur")
        leikmadur = int(input("Veldu 1 fyrir Harald, 2 fyrir Hans, 3 fyrir Grétu, 4 fyrir Simma D og 5 fyrir Gylfa "))
        if leikmadur == 1:
            print("Þú hefur valið að spila við Harald Pott. Hann velur nú tölu. ")
        elif leikmadur == 2:
            print("Þú hefur valið að spila við Hans. Hann velur nú tölu. ")
        elif leikmadur == 3:
            print("Þú hefur valið að spila við Grétu. Hún velur nú tölu. ")
        elif leikmadur == 4:
            print("Þú hefur valið að spila við Sigmund Davíð. Hann velur nú tölu. ")
        elif leikmadur == 5:
            print("Þú hefur valið að spila við Gylfa Sig landliðsmann. Hann velur nú tölu. ")
        else:
            print("Vinsamlegast veldu leikmann")
            self.lokaherbergi(leikmadur)
        guess = int(input("Reyndu að giska á töluna. Veldu tölu a milli 1 og 99: "))
        while n != "guess":
            if guess < n:
                print("Þessi tala er of lág. Reyndu aftur: ")
                guess = int(input("Veldu tölu a milli 1 og 99: "))
            elif guess > n:
                print("Þessi tala er of há. Reyndu aftur: ")
                guess = int(input("Veldu tölu a milli 1 og 99: "))
            else:
                print("Allt rétt meistari!")
                self.hljod()

    def hljod(self):
        pygame.init()

        grey = (211,211,211)
        red =  (155, 50, 150)
        blue = (0,0,238)
        black = (0,0,0)
        size = [600, 700]
        done = False
        txt = 'Til hamingju! Þú hefur unnið Leikjaland!'
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

    def endir(self):
        print('Leikurinn er búinn.')

def  main():
    loka = Herbergi_4(leikmadur)
    loka.mynd_3(leikmadur)
    loka.lokaherbergi(leikmadur)
    loka.hljod()
    loka.endir()

if __name__  == '__main__':
    main()
