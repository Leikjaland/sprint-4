# Útgáfa 1.1
import sys
import time
import select
import graphics
from graphics import *
from herbergi_2 import Herbergi_2
from herbergi_3 import Herbergi_3
from herbergi_4 import Herbergi_4
#from Herbergi_4 import Herbergi_4

# Hlutir sem þarf að satna í skólasofu og útiveru
bok = 0
blom = 0
leikmadur = 0
fot =''

class leikjaland(object):
    def __init__(self,bok,blom):
        self.bok = bok
        self.blom = blom

# Hér ver verið að taka á móti leikmanni og spyrja um kyn.
    win = GraphWin("Leikjaland", 600, 600)
    myImage = Image(Point(300,200), "castle.gif")
    myImage.draw(win)
    txt = Text(Point(300,550),'Velkomin\\n í Leikjaland!')
    txt.draw(win)
    time.sleep(6)
    win.close()
    def velja_kyn(self):
        #print('test 1')
        kyn = input('Veldu kyn, strákur eða stelpa: ')
        if kyn == 'strákur':
            win = GraphWin("strákur", 600, 600)
            myImage = Image(Point(300,200), "boy.gif")
            myImage.draw(win)
            txt = Text(Point(300,550),'Þú ert strákur!')
            txt.draw(win)
            time.sleep(3)
            win.close()
        elif kyn == 'stelpa':
            win = GraphWin("stelpa", 600, 600)
            myImage = Image(Point(300,300), "girl.gif")
            myImage.draw(win)
            txt = Text(Point(300,550),'Þú ert stelpa!')
            txt.draw(win)
            time.sleep(3)
            win.close()
        else:
            print('Vinsamlega veldu kyn: strákur eða stelpa')
            self.velja_kyn()

# Hér byrjar herbergi_1
    def Herbergi_1(self,bok,blom,herb2,herb3,herb4):
        #print('herb1-test#1')
        while (1):
            try:
                fot= input('Viltu fara í skólann eða út að leika, velja\\skrifa skolafot eða utifot: ')
                fot=fot
                break
            except:
                print ('Þú hefur ekki valið föt')

# leikmaður fer í skolastofuna(herbergi 2)
        if fot == 'skolafot':
            print('Þú ert komin\\n í skólann')
            herb2.mynd_1(bok,blom,herb3)
            #print('skoli')
            bok = 1
            self.skipta_um_fot(bok,blom,herb2,herb3,herb4)

# Leikmaður fer í útiveru(herbergi 3)
        elif fot == 'utifot':
            print('Þú ert komin\\n út')
            herb3.mynd_2(bok,blom,herb2)
            #print('úti')
            blom = 1
            self.skipta_um_fot(bok,blom,herb2,herb3,herb4)

# Ef ekki er valið skólaföt eða útiföt
        else:
            print ('Þú hefur ekki valið föt')
            self.Herbergi_1(bok,blom,herb2,herb3,herb4)


# Fallið leyfir leikmanni að koma til baka og skipta um föt til að fara í hitt herbergið
    def skipta_um_fot(self,bok,blom,herb2,herb3,herb4):
        #print('herb-test#2')
        #print(bok)
        #print(blom)
        if bok == 1 and blom != 1:
            herb3.mynd_2(bok,blom,herb2)
            blom=1
            self.skipta_um_fot(bok,blom,herb2,herb3,herb4)
        elif bok != 1 and blom == 1:
            print('Vonandi var gaman úti að leika, nú er tími til að fara í skólaföt að drífa sig í skólann.')
            herb2.mynd_1(bok,blom,herb3)
            bok=1
            self.skipta_um_fot(bok,blom,herb2,herb3,herb4)
        elif bok == 1 and blom == 1:
            print('Nú hefur þú klárað báðar þrautirnar og ert að fara í lokaborðið.')
            herb4.mynd_3(leikmadur)

def main():

    leikur =leikjaland(bok,blom)
    leikur.velja_kyn()
    herb2 = Herbergi_2(bok,blom)
    herb3 = Herbergi_3(bok,blom)
    herb4 = Herbergi_4(leikmadur)
    leikur.Herbergi_1(bok,blom,herb2,herb3,herb4)


if __name__  == '__main__':
    main()
