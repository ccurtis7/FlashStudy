from graphics import *

class Graphics:
    
    def __init__(self):
        self.win = GraphWin('flashcard', 500, 500)
        self.win.setCoords(0, 0, 100, 100)
        self.win.setBackground('light blue')
        
    
    def card(self):
        rect = Rectangle(Point(15, 30), Point(85, 70))
        rect.setFill('white')
        rect.draw(self.win)
    
    def text(self):
        quest = Text(Point(50, 50), 'What was the release date of\n'
                     'the first Scream movie')
        quest.draw(self.win)
    
    def draw(self):
        pass
    
    def undraw(self):
        pass
    
    def run(self):
        self.card()
        self.text()
        self.win.getMouse()
        self.win.close()
    
if __name__ == "__main__":
    Graphics().run()