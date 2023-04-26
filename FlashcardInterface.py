from graphics import *
from Button import Button

class GraphicInterface:
    
    def __init__(self):
        self.win = GraphWin('flashcard', 500, 500)
        self.win.setCoords(0, 0, 100, 100)
        self.win.setBackground('light blue')
        self.backButton = Button(self.win, Point(30, 10), 36, 10, 'Back')
        self.awnserButton = Button(self.win, Point(70, 10), 36, 10, 'Awnser')
    
    def drawCard(self):
        rect = Rectangle(Point(15, 30), Point(85, 70))
        rect.setFill('white')
        rect.draw(self.win)
    
    def text(self):
        self.text = Text(Point(50, 50), 'What was the release date of\n'
                     'the first Scream movie')
        self.text.draw(self.win)
        
    def run(self):
        self.drawCard()
        self.text()
        self.win.getMouse()
        self.win.close()
    
if __name__ == "__main__":
    app = GraphicInterface()
    app.run()