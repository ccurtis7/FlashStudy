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
        
        ## Main Window
        self.mainwin = mainwin = GraphWin('FlashStudy - Start Menu', 500, 500)
        mainwin.setCoords(0, 0, 100, 100)
        self.mainwin.setBackground('midnight blue')

        ## Image
        self.brandImage = Image(Point(50,50), "FlashStudy.gif").draw(mainwin)

        ## About the flashcard app
        about = Text(Point(50, 65), 'Study any subject with this flashcard maker!')
        about.setSize(15)
        about.setTextColor("white")
        about.draw(self.mainwin)
        
        ## Buttons
        ### choose an existing deck
        self.chooseDeckButton = Button(self.mainwin, Point(20, 10), 25, 10, 'Choose Deck')
        self.chooseDeckButton.activate()

        ### create a new deck
        self.createDeckButton = Button(self.mainwin, Point(50, 10), 25, 10, 'Create Deck')
        self.createDeckButton.activate()
        
        ### quit to exit program
        self.quitButton = Button(self.mainwin, Point(80, 10), 25, 10, 'Quit')
        self.quitButton.activate()       

    def run(self):
        p = Point(0, 0)
        while not self.quitButton.clicked(p):
            p = self.mainwin.getMouse()
            if self.chooseDeckButton.clicked(p):
                chooseDeckButton = DeckMenu()
                chooseDeckButton.run()
            elif self.createDeckButton.clicked(p):
                createDeckButton = NewDeck()
                createDeckButton.run()
                
class DeckMenu:
    def __init__(self):
        # Open an existing deck file within a "deck" folder
        self.infilename = askopenfilename(initialdir=os.path.join(os.getcwd(), 'deck'))
        
        # Graphics User Interface for starting menu if user didn't "cancel"
        if self.infilename:
            ## Deck Window
            self.deckwin = deckwin = GraphWin('FlashStudy - Deck View', 500, 500)
            deckwin.setCoords(0, 0, 100, 100)
            self.deckwin.setBackground('midnight blue')

            ## Image
            self.indexImage = Image(Point(50,50), "FlashIndex.gif").draw(deckwin)
        
            ## Deck Name
            existingfilename = Path(self.infilename)
            existingDeckName = Text(Point(50, 31), existingfilename.name)
            existingDeckName.setSize(20)
            existingDeckName.setStyle("bold")
            existingDeckName.setTextColor("white")
            existingDeckName.draw(self.deckwin)

            ## Buttons
            ### review deck
            self.reviewDeckButton = Button(self.deckwin, Point(20, 10), 25, 10, 'Review')
            self.reviewDeckButton.activate()

            ### delete deck
            self.modifyDeckButton = Button(self.deckwin, Point(50, 10), 25, 10, 'Modify')
            self.modifyDeckButton.activate()
        
            ### close deck window to go back to main window
            self.backButton = Button(self.deckwin, Point(80, 10), 25, 10, 'Back')
            self.backButton.activate()

    def run(self):
        while True:
            if not self.infilename:
                break
            self.pt = self.deckwin.getMouse()
            if self.reviewDeckButton.clicked(self.pt):
                self.deckwin.close()
                self.reviewDeck()
                self.scoreScreen()
                break
            elif self.modifyDeckButton.clicked(self.pt):
                modifyDeckButton = ModifyDeck()
                modifyDeckButton.run()
            elif self.backButton.clicked(self.pt):
                self.deckwin.close()
                break

    def reviewDeck(self):
        # Graphics User Interface for starting menu if user didn't "cancel"
        ## Deck Window
        self.studywin = studywin = GraphWin('FlashStudy - Review', 500, 500)
        studywin.setCoords(0, 0, 100, 100)
        self.studywin.setBackground('midnight blue')

        ## Image
        self.booksImage = Image(Point(50,50), "FlashBooks.gif").draw(studywin)

        ### Card
        rect = Rectangle(Point(15, 50), Point(85, 90))
        rect.setFill('white')
        rect.draw(self.studywin)

        ## Buttons
        ### turn card
        self.turnCardButton = Button(self.studywin, Point(35, 10), 25, 10, 'Turn')
        self.turnCardButton.activate()
        
        ### previous card
        #self.backCardButton = Button(self.studywin, Point(50, 10), 25, 10, 'Back')
        #self.backCardButton.activate()

        ### quit review
        self.quitReviewButton = Button(self.studywin, Point(65, 10), 25, 10, 'Quit')
        self.quitReviewButton.activate()

        ## Flashcard Contents
        ### turn .txt file str into dictionaries
        if '.txt' in self.infilename:
            self.cards = {}
            infile = open(self.infilename, 'r')
            for line in infile.readlines():
                contents = line.replace('\n', '')
                contents = contents.split(',')
                self.cards[contents[0]] = contents[1]
            infile.close()
        else:
            self.studywin.close()

        ### create keys
        self.keys = []
        for front, back in self.cards.items():
            self.keys.append(front)
         
        self.frontText = Text(Point(50, 70), self.keys[0])

        p = Point(0,0)
        for front, back in self.cards.items():
            self.frontText = Text(Point(50, 70), front)
            self.frontText.draw(self.studywin)
            p = self.studywin.getMouse()
            if self.turnCardButton.clicked(p):
                ### undraw front of card
                self.frontText.undraw()
                ### show back of card
                self.backText = Text(Point(50, 70), back)
                self.backText.draw(self.studywin)
                ### deactivate turn card button, create and activate next button
                self.nextCardButton = Button(self.studywin, Point(35, 10), 25, 10, 'Next')
                self.nextCardButton.activate()
                p = self.studywin.getMouse()
                if self.nextCardButton.clicked(p):
                    self.backText.undraw()
                    self.turnCardButton = Button(self.studywin, Point(35, 10), 25, 10, 'Turn')
                    self.turnCardButton.activate()
                elif self.quitReviewButton.clicked(p):
                    self.studywin.close()
                    break
                else:
                    break
            if self.quitReviewButton.clicked(p):
                self.studywin.close()
                break
        self.studywin.close()
    
    def scoreScreen(self):
        # Graphics for end of review deck
        ## Score Window
        self.scorewin = scorewin = GraphWin('FlashStudy - Score Screen', 500, 500)
        scorewin.setCoords(0, 0, 100, 100)
        self.scorewin.setBackground('midnight blue')
        self.congratsImage = Image(Point(50,50), "FlashCongrats.gif").draw(self.scorewin)

        #p = Point(0,0)
        #p = self.scorewin.getMouse()
        while True:
            if self.scorewin.getMouse():
                self.scorewin.close()
                break
            
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
            ## Add Card Window
            self.addcardwin = addcardwin = GraphWin("Create Flashcards", 500, 500)
            addcardwin.setCoords(0, 0, 100, 100), addcardwin.setBackground("midnight blue")

            ## Deck Name
            newfilename = Path(self.outfilename)
            newDeckName = Text(Point(50, 90), newfilename.name)
            newDeckName.setSize(20)
            newDeckName.setStyle("bold")
            newDeckName.setTextColor("white")
            newDeckName.draw(self.addcardwin)
            
            ## Image
            self.pawImage = Image(Point(50,50), "FlashPaw.gif").draw(addcardwin)

            instruction = Text(Point(50, 75), 'Type your question or problem for the front\n'
                        'of the card. Then type the answer for the\n'
                        'back of the card.\n')
            instruction.setSize(15)
            instruction.setTextColor("white")
            instruction.draw(self.addcardwin)
        
            ## Input fields
            self.questionInput = Entry(Point(55, 60), 30).draw(addcardwin)
            self.questionInput.setFill("white")
            self.questionInputLabel = Text(Point(20, 60), "Front:").draw(addcardwin)
            self.questionInputLabel.setTextColor("white")
            self.questionInputLabel.setSize(15)

            self.answerInput = Entry(Point(55, 50), 30).draw(addcardwin)
            self.answerInputLabel = Text(Point(20, 50), "Back:").draw(addcardwin)
            self.answerInputLabel.setTextColor("white")
            self.answerInputLabel.setSize(15)

            ## Buttons
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