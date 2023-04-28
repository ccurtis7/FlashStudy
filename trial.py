import sys
sys.path.insert(0, '..')
from graphics import *
from button import Button
#from FlashStudyApp import Deck
#from Interface2 import DisplayBackCard
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

class StartMenu:
    def __init__(self):
        # Graphics User Interface for starting menu
        
        # Main Window
        self.mainwin = mainwin = GraphWin('FlashStudy - Start Menu', 500, 500)
        mainwin.setCoords(0, 0, 100, 100)
        self.mainwin.setBackground('midnight blue')
        
        # Buttons
        # continue to bring up existing deck
        self.existingDeckButton = Button(self.mainwin, Point(20, 10), 25, 10, 'Existing Deck')
        self.existingDeckButton.activate()

        # add to create a new deck
        self.newDeckButton = Button(self.mainwin, Point(50, 10), 25, 10, 'New Deck')
        self.newDeckButton.activate()
        
        # quit to exit program
        self.quitButton = Button(self.mainwin, Point(80, 10), 25, 10, 'Quit')
        self.quitButton.activate()
        
    def text(self):
        title = Text(Point(50, 90), 'FlashStudy')
        title.setSize(18)
        title.setStyle("bold")
        title.setTextColor("light blue")
        title.draw(self.mainwin)
        
        instruction = Text(Point(50, 50), 'You will be able to study any\n'
                         'subject you want this flashcard maker.')
        instruction.setSize(15)
        instruction.setTextColor("light blue")
        instruction.draw(self.mainwin)


    def run(self):
        self.text()
        p = Point(0, 0)
        while not self.quitButton.clicked(p):
            p = self.mainwin.getMouse()
            if self.existingDeckButton.clicked(p):
                existingDeckButton = DeckView()
                existingDeckButton.run()
            elif self.newDeckButton.clicked(p):
                newDeckButton = NewDeck()
                newDeckButton.run()
            else:
                break
                
class DeckView:
    def __init__(self):
        self.infilename = askopenfilename(initialdir=os.path.join(os.getcwd(), 'deck'))
        # deckwin

    def run(self):
        # DeckView
        pass

class NewDeck:
    def __init__(self):
        # Create and save a new deck file
        self.outfilename = asksaveasfilename(initialdir=os.path.join(os.getcwd(), 'deck'))

        # Graphics User Interface for Add window
        self.addcardwin = addcardwin = GraphWin("Create Flashcards", 500, 500)
        addcardwin.setCoords(0, 0, 500, 500), addcardwin.setBackground("midnight blue")
        
        # Input fields
        self.question_input = Entry(Point(250, 300), 15).draw(addcardwin)
        self.question_input.setFill("white")
        self.question_input_label = Text(Point(145, 300), "Question:").draw(addcardwin)
        self.question_input_label.setTextColor("light blue")

        self.answer_input = Entry(Point(250, 250), 15).draw(addcardwin)
        self.answer_input_label = Text(Point(145, 250), "Answer:").draw(addcardwin)
        self.answer_input_label.setTextColor("light blue")

        # Buttons
        self.save_button = Button(addcardwin, Point(150, 150), 45, 32, "Save")
        self.answer_input.setFill("white")
        self.save_button.activate()

        self.quit_button = Button(addcardwin, Point(350, 150), 45, 32, "Quit")
        self.quit_button.activate()

    def saveInputs(self):
        question, answer = self.question_input.getText(), self.answer_input.getText()

        # Save the question and answer to a file
        with open("Sample.txt", "a") as f: f.write(f"Question: {question}\nAnswer: {answer}\n")

        # Clear the input fields
        self.answer_input.setText(""), self.question_input.setText("")


    def run(self):
        # NewCardWin
        #self.pt = self.addcardwin.getMouse()
        
        while True:
            self.pt = self.addcardwin.getMouse()
            if self.save_button.clicked(self.pt):
                self.saveInputs()
            elif self.quit_button.clicked(self.pt):
                self.addcardwin.close()
                break
             
                
if __name__ == "__main__":
    flashstudy = StartMenu()
    flashstudy.run()