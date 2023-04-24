from graphics import *
from Button import Button

class MainWin:
    def __init__(self):
        self.win = win = GraphWin('Main Window', 200, 400)
        win.setCoords(0, 0, 2, 4)
        self.quitButton = Button(win, Point(1, 1), 0.5, 0.3, 'Quit')
        self.quitButton.activate()

        self.addButton = Button(win, Point(1, 3), 0.5, 0.3, 'Add')
        self.addButton.activate()

        self.openButton = Button(win, Point(1, 2), 0.5, 0.3, 'Open')
        self.openButton.activate()

    def run(self):
        p = Point(0, 0)
        while not self.quitButton.clicked(p):
            p = self.win.getMouse()
            if self.addButton.clicked(p):
                addwin = AddWin()
            elif self.openButton.clicked(p):
                openwin = OpenWin()

class AddWin:
    def __init__(self):
        self.win = win = GraphWin('Add Card', 200, 200)

class OpenWin:
    def __init__(self):
        self.win = win = GraphWin('Open', 200, 200)


if __name__ == '__main__':
    mainwin = MainWin()
    mainwin.run()
