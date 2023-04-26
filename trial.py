from graphics import *
from Button import Button
from FlashStudyApp import Deck
from Interface2 import DisplayBackCard
from tkinter.filedialog import askopenfilename, asksaveasfilename
import sys
import os

class MainWin:
    def __init__(self):
        self.win = win = GraphWin('Main Window', 500, 500)
        win.setCoords(0, 0, 100, 100)
        self.win.setBackground('midnight blue')
        self.quitButton = Button(self.win, Point(20, 10), 20, 10, 'Quit')
        self.quitButton.activate()
        self.addButton = Button(win, Point(50, 10), 20, 10, 'Add')
        self.addButton.activate()
        self.continueButton = Button(self.win, Point(80, 10), 20, 10, 'Continue')
        self.continueButton.activate()
        
    def text(self):
        title = Text(Point(50, 90), 'FlashStudy')
        title.setSize(18)
        title.setStyle("bold")
        title.setTextColor("light blue")
        title.draw(self.win)
        
        instruction = Text(Point(50, 50), 'In this app you will be able to study any\n'
                         'subject you want. Click continue for\n'
                          'exsiting deck or add to make a new deck')
        instruction.setSize(15)
        instruction.setTextColor("light blue")
        instruction.draw(self.win)


    def run(self):
        self.text()
        p = Point(0, 0)
        while not self.quitButton.clicked(p):
            p = self.win.getMouse()
            if self.continueButton.clicked(p):
                continuewin = ContinueWin()
                continuewin.run()
            elif self.addButton.clicked(p):
                addwin = AddWin()
                addwin.run()
                
class ContinueWin:
    def __init__(self):
        self.infilename = askopenfilename(initialdir=os.path.join(os.getcwd(), 'deck'))

    def run(self):
        pass

class AddWin:
    def __init__(self):
        self.outfilename = asksaveasfilename(initialdir=os.path.join(os.getcwd(), 'deck'))
       
                
if __name__ == "__main__":
    mainwin = MainWin()
    mainwin.run()