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

        # Image
        self.brandImage = Image(Point(50,50), "FlashStudy.gif").draw(mainwin)
        
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
        
        # about the flashcard app
        about = Text(Point(50, 65), 'You will be able to study any\n'
                         'subject you want with this flashcard maker.')
        about.setSize(15)
        about.setTextColor("white")
        about.draw(self.mainwin)


    def run(self):
        p = Point(0, 0)
        while not self.quitButton.clicked(p):
            p = self.mainwin.getMouse()
            if self.existingDeckButton.clicked(p):
                existingDeckButton = DeckView()
                existingDeckButton.run()
            elif self.newDeckButton.clicked(p):
                newDeckButton = NewDeck()
                newDeckButton.run()
                
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

        # Graphics User Interface for adding cards

        # Add Card Window
        self.addcardwin = addcardwin = GraphWin("Create Flashcards", 500, 500)
        addcardwin.setCoords(0, 0, 100, 100), addcardwin.setBackground("midnight blue")

        # Image
        self.catImage = Image(Point(50,50), "FlashPaw.gif").draw(addcardwin)

        instruction = Text(Point(50, 75), 'Type your question or problem for the front\n'
                    'of the card. Then type the answer for the\n'
                    'back of the card.\n'
                    '\nPress "Save" AFTER EACH card.')
        instruction.setSize(15)
        instruction.setTextColor("white")
        instruction.draw(self.addcardwin)
        
        # Input fields
        self.question_input = Entry(Point(55, 50), 30).draw(addcardwin)
        self.question_input.setFill("white")
        self.question_input_label = Text(Point(20, 50), "Front:").draw(addcardwin)
        self.question_input_label.setTextColor("white")
        self.question_input_label.setSize(15)

        self.answer_input = Entry(Point(55, 40), 30).draw(addcardwin)
        self.answer_input_label = Text(Point(20, 40), "Back:").draw(addcardwin)
        self.answer_input_label.setTextColor("white")
        self.answer_input_label.setSize(15)

        # Buttons
        self.save_button = Button(addcardwin, Point(35, 10), 25, 10, "Save")
        self.answer_input.setFill("white")
        self.save_button.activate()

        self.quit_button = Button(addcardwin, Point(65, 10), 25, 10, "Quit")
        self.quit_button.activate()

    def saveInputs(self):
        question, answer = self.question_input.getText(), self.answer_input.getText()

        # Save the question and answer to a file
        with open(self.outfilename, "a") as f: f.write(f"{question},{answer}\n")

        # Clear the input fields
        self.answer_input.setText(""), self.question_input.setText("")


    def run(self):    
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