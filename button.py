from graphics import *

class Button:
    def __init__(self, win, center, width, height, label):
        w, h = width / 2, height / 2
        x, y = center.getX(), center.getY()
        self.xmin, self.xmax = x - w, x + w
        self.ymin, self.ymax= y - h, y + h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(p1, p2).draw(win)
        self.rect.setFill("grey")

        self.label = Text(center, label).draw(win)

        self.deactivate()

    def clicked(self, pt):
        return ((self.active) & 
                (self.xmin <= pt.getX() <= self.xmax) & 
                (self.ymin <= pt.getY() <= self.ymax))

    def activate(self):
        self.active = True
        self.label.setFill("black")
        self.rect.setWidth(2)

    def deactivate(self):
        self.active = False
        self.label.setFill("grey")
        self.rect.setWidth(2)

    def getLabel(self):
        return self.label.setText()