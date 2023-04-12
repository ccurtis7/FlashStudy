from graphics import *

class DisplayBackCard:
    
    def __init__(self):
        self.win = GraphWin('flashcard', 500, 500)
        self.win.setCoords(0, 0, 100, 100)
        self.win.setBackground('light blue')
        
    
    def drawCard(self):
        rect = Rectangle(Point(15, 30), Point(85, 70))
        rect.setFill('white')
        rect.draw(self.win)
        
    def text(self):
        self.text = Text(Point(50, 50), 'December 20, 1996')
        self.text.draw(self.win)
    
    def button(self):
        l = 36
        w = 10
        c = Point(30, 10)
        
        xlo, xhi = c.getX() - l/2, c.getX() + l/2
        ylo, yhi = c.getY() - w/2, c.getY() + w/2
        button = Rectangle(Point(xlo, ylo), Point(xhi, yhi))
        button.setFill('white')
        button.draw(self.win)

        l2 = 36
        w2 = 10
        c2 = Point(70, 10)

        xlo2, xhi2 = c2.getX() - l/2, c2.getX() + l/2
        ylo2, yhi2 = c2.getY() - w/2, c2.getY() + w/2
        button2 = Rectangle(Point(xlo2, ylo2), Point(xhi2, yhi2))
        button2.setFill('white')
        button2.draw(self.win)

        Clabel = Text(c, "Back")
        Clabel.draw(self.win)
        Clabel2 = Text(c2, "Next")
        Clabel2.draw(self.win)
    
    def run(self):
        self.drawCard()
        self.text()
        self.button()
        self.win.getMouse()
        self.win.close()
    
if __name__ == "__main__":
    DisplayBackCard().run()