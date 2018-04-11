import graphics
from graphics import *

#print('test 1')
bok=[]
blom = 0
herb2 = 0
class Herbergi_3():
    #print('herb3-test#1')
    def __init__(self,bok,blom):
        self.bok = bok
        self.blom = blom

    def mynd_2(self,bok,blom,herb2):
        #print('herb3-test#2')
        win = GraphWin("útivera", 600, 600)
        myImage = Image(Point(300,300), "playground.gif")
        myImage.draw(win)
        txt = Text(Point(310,50),'Þú ert komin\\n út')
        txt1 = Text(Point(310,550),'Nú þarft þú að leysa þrjár myndaþrautir.')
        txt.draw(win)
        txt1.draw(win)
        time.sleep(5)
        win.close()
        self.utivera(bok,blom,herb2)

    def utivera(self,bok,blom,herb2):
        #print('herb3-test#3')
        win = GraphWin("Blóm", 400, 400)
        myImage = Image(Point(200,100), "flow.gif")
        myImage.draw(win)
        txt = Text(Point(200,300),'Teldu hvað það eru mörg gul blóm á myndinni.')
        txt.draw(win)
        time.sleep(5)
        win.close()
        spurning1 = input('Hvað voru mörg gul blóm á myndinni? ')
        win = GraphWin("Dýr", 600, 600)
        myImage = Image(Point(300, 300), "dyr.gif")
        myImage.draw(win)
        txt = Text(Point(300,550),'Teldu hvað það eru mörg svín á myndinni.')
        txt.draw(win)
        time.sleep(5)
        win.close()
        spurning2 = input('Hvað eru mörg svín á myndinni? ')
        win = GraphWin("Himinn", 600, 600)
        myImage = Image(Point(300, 300), "himinn.gif")
        myImage.draw(win)
        txt = Text(Point(300,550),'Skoðaðu vel hvað er á myndinni.')
        txt.draw(win)
        time.sleep(5)
        win.close()
        spurning3 = input('Hvað passar ekki inn í? Ský, himinn, bíll eða stjörnur? ')
        if spurning1 == '3' and spurning2 == '4' and spurning3 == 'bíll':
            print('Það er rétt! Vel gert!')
            blom =+ 1
            blom = blom
        elif spurning1 != '3' and spurning2 == '4' and spurning3 == 'bíll':
            print('Þraut 1 er ekki rétt. Reyndu aftur:')
            self.utivera(bok,blom,herb2)
        elif spurning1 == '3' and spurning2 != '4' and spurning3 == 'bíll':
            print('Þraut 2 er ekki rétt. Reyndu aftur:')
            self.utivera(bok,blom,herb2)
        elif spurning1 == '3' and spurning2 == '4' and spurning3 != 'bíll':
            print('Þraut 3 er ekki rétt. Reyndu aftur:')
            self.utivera(bok,blom,herb2)
        elif spurning1 == '3' and spurning2 != '4' and spurning3 != 'bíll':
            print('Þrautir 2 og 3 eru ekki réttar. Reyndu aftur:')
            self.utivera(bok,blom,herb2)
        elif spurning1 != '3' and spurning2 == '4' and spurning3 != 'bíll':
            print('Þrautir 1 og 3 eru ekki réttar. Reyndu aftur:')
            self.utivera(bok,blom,herb2)
        elif spurning1 != '3' and spurning2 != '4' and spurning3 == 'bíll':
            print('Þrautir 1 og 2 eru ekki réttar. Reyndu aftur:')
            self.utivera(bok,blom,herb2)
        else:
            print('Engin þraut er rétt. Reyndu aftur:')
            self.utivera(bok,blom,herb2)

def  main():
    bord3=Herbergi_3(bok,blom)
    bord3.mynd_2(bok,blom,herb2)
    bord3.utivera(bok,blom,herb2)

if __name__  == '__main__':
    main()
