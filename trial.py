from graphics import *
from button import Button
#from FlashStudyApp import Deck
#from Interface2 import DisplayBackCard
from tkinter.filedialog import askopenfilename, asksaveasfilename
from pathlib import Path
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
        # choose an existing deck
        self.chooseDeckButton = Button(self.mainwin, Point(20, 10), 25, 10, 'Choose Deck')
        self.chooseDeckButton.activate()

        # create a new deck
        self.createDeckButton = Button(self.mainwin, Point(50, 10), 25, 10, 'Create Deck')
        self.createDeckButton.activate()
        
        # quit to exit program
        self.quitButton = Button(self.mainwin, Point(80, 10), 25, 10, 'Quit')
        self.quitButton.activate()
        
        # about the flashcard app
        about = Text(Point(50, 65), 'Study any subject with this flashcard maker!')
        about.setSize(15)
        about.setTextColor("white")
        about.draw(self.mainwin)


    def run(self):
        p = Point(0, 0)
        while not self.quitButton.clicked(p):
            p = self.mainwin.getMouse()
            if self.chooseDeckButton.clicked(p):
                chooseDeckButton = DeckView()
                chooseDeckButton.run()
            elif self.createDeckButton.clicked(p):
                createDeckButton = NewDeck()
                createDeckButton.run()
                
class DeckView:
    def __init__(self):
        # Open an existing deck file within a "deck" folder
        self.infilename = askopenfilename(initialdir=os.path.join(os.getcwd(), 'deck'))
        
        # Graphics User Interface for starting menu if user didn't "cancel"
        if self.infilename:
            # Deck Window
            self.deckwin = deckwin = GraphWin('FlashStudy - Deck View', 500, 500)
            deckwin.setCoords(0, 0, 100, 100)
            self.deckwin.setBackground('midnight blue')

            # Image
            self.indexImage = Image(Point(50,50), "FlashIndex.gif").draw(deckwin)
        
            # Deck Name
            existingfilename = Path(self.infilename)
            existingDeckName = Text(Point(50, 31), existingfilename.name)
            existingDeckName.setSize(20)
            existingDeckName.setStyle("bold")
            existingDeckName.setTextColor("white")
            existingDeckName.draw(self.deckwin)

            # Buttons
            # review deck
            self.reviewDeckButton = Button(self.deckwin, Point(20, 10), 25, 10, 'Review')
            self.reviewDeckButton.activate()

            # delete deck
            self.modifyDeckButton = Button(self.deckwin, Point(50, 10), 25, 10, 'Modify')
            self.modifyDeckButton.activate()
        
            # close deck window to go back to main window
            self.backButton = Button(self.deckwin, Point(80, 10), 25, 10, 'Back')
            self.backButton.activate()

    def run(self):
        while True:
            if not self.infilename:
                break
            self.pt = self.deckwin.getMouse()
            if self.reviewDeckButton.clicked(self.pt):
                reviewDeckButton = Review()
                reviewDeckButton.run()
            elif self.modifyDeckButton.clicked(self.pt):
                modifyDeckButton = ModifyDeck()
                modifyDeckButton.run()
            elif self.backButton.clicked(self.pt):
                self.deckwin.close()
                break

class Review:
    def __init__(self):
        pass

    def run(self):
        pass

class ModifyDeck:
    def __init__(self):
        pass

    def run(self):
        pass

class NewDeck:
    def __init__(self):
        # Create and save a new deck file
        self.outfilename = asksaveasfilename(initialdir=os.path.join(os.getcwd(), 'deck'))

        # Graphics User Interface for adding cards if user didn't "cancel"
        if self.outfilename:
            # Add Card Window
            self.addcardwin = addcardwin = GraphWin("Create Flashcards", 500, 500)
            addcardwin.setCoords(0, 0, 100, 100), addcardwin.setBackground("midnight blue")

            # Deck Name
            newfilename = Path(self.outfilename)
            newDeckName = Text(Point(50, 90), newfilename.name)
            newDeckName.setSize(20)
            newDeckName.setStyle("bold")
            newDeckName.setTextColor("white")
            newDeckName.draw(self.addcardwin)
            
            # Image
            self.pawImage = Image(Point(50,50), "FlashPaw.gif").draw(addcardwin)

            instruction = Text(Point(50, 75), 'Type your question or problem for the front\n'
                        'of the card. Then type the answer for the\n'
                        'back of the card.\n')
            instruction.setSize(15)
            instruction.setTextColor("white")
            instruction.draw(self.addcardwin)
        
            # Input fields
            self.questionInput = Entry(Point(55, 60), 30).draw(addcardwin)
            self.questionInput.setFill("white")
            self.questionInputLabel = Text(Point(20, 60), "Front:").draw(addcardwin)
            self.questionInputLabel.setTextColor("white")
            self.questionInputLabel.setSize(15)

            self.answerInput = Entry(Point(55, 50), 30).draw(addcardwin)
            self.answerInputLabel = Text(Point(20, 50), "Back:").draw(addcardwin)
            self.answerInputLabel.setTextColor("white")
            self.answerInputLabel.setSize(15)

            # Buttons
            self.addButton = Button(addcardwin, Point(35, 10), 25, 10, "Add")
            self.answerInput.setFill("white")
            self.addButton.activate()

            self.closeButton = Button(addcardwin, Point(65, 10), 25, 10, "Close")
            self.closeButton.activate()

    def saveInputs(self):
        question, answer = self.questionInput.getText(), self.answerInput.getText()

        # Save the question and answer to a file
        with open(self.outfilename, "a") as f: f.write(f"{question},{answer}\n")

        # Clear the input fields
        self.answerInput.setText(""), self.questionInput.setText("")


    def run(self):    
        while True:
            if not self.outfilename:
                break
            self.pt = self.addcardwin.getMouse()
            if self.addButton.clicked(self.pt):
                self.saveInputs()
            elif self.closeButton.clicked(self.pt):
                self.addcardwin.close()
                break
             
                
if __name__ == "__main__":
    flashstudy = StartMenu()
    flashstudy.run()