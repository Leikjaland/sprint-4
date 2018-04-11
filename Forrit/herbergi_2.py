#print('test 1')
import graphics
from graphics import *
bok=0
blom = []
herb3 = 0
class Herbergi_2():
    #print('herb2-test#1')
    def __init__(self,bok,blom):
        self.bok = bok
        self.blom = blom


    def mynd_1(self,bok,blom,herb3):
        #print('herb2-test#2')
        win = GraphWin("skólastofa", 600, 600)
        myImage = Image(Point(300,300), "School.gif")
        myImage.draw(win)
        txt = Text(Point(310,50),'Velkomin\\n í skólann!')
        txt1 = Text(Point(310,550),'Nú ert þú í stærðfræði og þú átt að reikna þrjú dæmi, gangi þér vel!')
        txt.draw(win)
        txt1.draw(win)
        time.sleep(5)
        win.close()
        self.skolastofa(bok,blom,herb3)

    # Leikmaðurinn fer í skólastofu
    def skolastofa(self,bok,blom,herb3):
        #print('herb2-test#3')
        daemi_1 = input('Hvað er 5+6? ')
        daemi_2 = input('hvað er 10+2-4? ')
        daemi_3 = input('Hvað er 15-3? ')
        if daemi_1 == '11' and daemi_2=='8' and daemi_3 =='12':
            print('Það er rétt! Vel gert!')
            bok =+ 1
            bok=bok
        elif daemi_1 != '11' and daemi_2=='8' and daemi_3 =='12':
            print('Dæmi 1 er ekki rétt. Reyndu aftur:')
            self.skolastofa(bok,blom,herb3)
        elif daemi_1 == '11' and daemi_2 !='8' and daemi_3 =='12':
            print('Dæmi 2 er ekki rétt. Reyndu aftur:')
            self.skolastofa(bok,blom,herb3)
        elif daemi_1 == '11' and daemi_2=='8' and daemi_3 !='12':
            print('Dæmi 3 er ekki rétt. Reyndu aftur:')
            self.skolastofa(bok,blom,herb3)
        elif daemi_1 != '11' and daemi_2 !='8' and daemi_3 =='12':
            print('Dæmi 1 og 2 eru ekki rétt. Reyndu aftur:')
            self.skolastofa(bok,blom,herb3)
        elif daemi_1 != '11' and daemi_2=='8' and daemi_3 !='12':
            print('Dæmi 1 og 3 eru ekki rétt. Reyndu aftur:')
            self.skolastofa(bok,blom,herb3)
        elif daemi_1 == '11' and daemi_2 !='8' and daemi_3 !='12':
            print('Dæmi 2 og 3 eru ekki rétt. Reyndu aftur:')
            self.skolastofa(bok,blom,herb3)
        else:
            print('Ekkert dæmi er rétt. Reyndu aftur:')
            skolastofa(bok,blom,herb3)

def  main():
    bord2=Herbergi_2(bok,blom)
    bord2.mynd_1(bok,blom,herb3)
    bord2.skolastofa(bok,blom,herb3)

if __name__  == '__main__':
    main()
