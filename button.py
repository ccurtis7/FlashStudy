# button.py
# A generic Button class for creating button widgets
# in a graphics window
from graphics import *

class Button:

    def __init__(self, win, center, width, height, label):
        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmin, self.xmax = x - w, x + w
        self.ymin, self.ymax = y - h, y + h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(p1, p2)
        self.rect.draw(win)
        self.rect.setFill('lightgrey')

        self.label = Text(center, label)
        self.label.draw(win)

        self.deactivate()

    def clicked(self, p):
        return (self.active &
                (self.xmin <= p.getX() <= self.xmax) &
                (self.ymin <= p.getY() <= self.ymax))

    def activate(self):
        self.active = True
        self.label.setFill('black')
        self.rect.setWidth(2)

    def deactivate(self):
        self.active = False
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)

    def getLabel(self):
        return self.label.getText()
