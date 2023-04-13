from graphics import *

class GraphicInterface:
    
    def __init__(self):
        self.win = GraphWin('flashcard', 500, 500)
        self.win.setCoords(0, 0, 100, 100)
        self.win.setBackground('light blue')
        
    def drawCard(self, text):
        rect = Rectangle(Point(15, 30), Point(85, 70))
        rect.setFill('white')
        rect.draw(self.win)
        quest = Text(Point(50, 50), 'What was the release date of\n'
                     'the first Scream movie')
        quest.draw(self.win)
    
    def run(self):
        self.drawCard()
        self.win.getMouse()
        self.win.close()
    
if __name__ == "__main__":
    GraphicInterface().run()
