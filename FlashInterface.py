from graphics import *
from Button import Button

class GraphicInterface:
    
    def __init__(self):
        self.win = GraphWin('flashcard', 500, 500)
        self.win.setCoords(0, 0, 100, 100)
        self.win.setBackground('light blue')
        self.closeButton = Button(self.win, Point(30, 10), 36, 10, 'Close')
    
    def drawCard(self):
        rect = Rectangle(Point(15, 30), Point(85, 70))
        rect.setFill('white')
        rect.draw(self.win)
    
    def text(self):
        self.text = Text(Point(50, 50), 'What was the release date of\n'
                     'the first Scream movie')
        self.text.draw(self.win)
        
#     def button(self):
#         l, w, c = 36, 10, Point(30, 10)
        
#         xlo, xhi,  ylo, yhi = c.getX() - l/2, c.getX() + l/2, c.getY() - w/2, c.getY() + w/2
#         button = Rectangle(Point(xlo, ylo), Point(xhi, yhi))
#         button.setFill('white')
#         button.draw(self.win)

#         l2, w2, c2 = 36, 10, Point(70, 10)

#         xlo2, xhi2, ylo2, yhi2 = c2.getX() - l/2, c2.getX() + l/2, c2.getY() - w/2, c2.getY() + w/2
#         button2 = Rectangle(Point(xlo2, ylo2), Point(xhi2, yhi2))
#         button2.setFill('white')
#         button2.draw(self.win)

#         Clabel, Clabel2 = Text(c, "Back"), Text(c2, "Anwser")
#         Clabel.draw(self.win)
#         Clabel2.draw(self.win)
    
    def run(self):
        self.drawCard()
        self.text()
        self.win.getMouse()
        self.win.close()
    
if __name__ == "__main__":
    app = GraphicInterface()
    app.run()
    