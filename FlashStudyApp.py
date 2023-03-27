import random

class Deck:
    def __init__(self):
        #run deck stuff
        pass

    def createCard(self):
        #newfile = input('Choose a file to send the card: ')
        #outFile = open(newfile, 'w')
        
        #create empty dictionary
        card = {}
        
        #card = {question, answer}
        #question = "2 + 2"
        #answer = "4" 

        while True:
            question = input("\nEnter the question: ") #ask the user for a question
            if question == 'Q':
                break
            answer = input("Enter the answer: ") #ask the user for answer
            
            card[question] = answer
        
        self.outFile.write(str(card))
        self.outFile.close()
        
        #save and return card dictionary
        return card

        

        

    def createDeck(self):
        #ask user for new deck name
        newfile = input('Choose a file to send the card: ')
        
        #create txt file
        self.outFile = open(newfile, 'w')

        #save and return deck
        return self.outFile
    
    def existingDeck():
        #ask user to choose an existing deck file
        #return deck.file
        pass

    def modifyCard():
        #lets user modify the card dictionary
        pass

    def deleteCard():
        #delete chosen card dictionary
        pass

    def nextCard():
        #go through all the cards
        pass

    def scoreScreen(): 
        #counter for times completed deck
        #if user input == main screen:
        #    start game all over
        #    exit to main screen
        #elif user input == go through same deck again:
        #    start chosen deck for loop again
        #else:
        #    close game
        pass


class FlashStudyApp:
    def __init__(self):
        self.deck = Deck()
        self.outFile = ""
        #deck.shuffle()
        #pass

    def play(self):
        while True:
            newDeck = self.deck.createDeck()
            newCard = self.deck.createCard()
            print(newCard)
            return newDeck
        #ask user to create a new deck or choose an existing deck
        #if user input == createDeck:
        #    createDeck()
        #    make cards until user is done loop:
        #        createCard()
        #elif user input == existingDeck:
        #    existingDeck()
        #    ask user if they want to modify, delete, add card, or continue
        #    if modify:
        #        modifyCard()
        #    elif delete:
        #        deleteCard()
        #    elif add:
        #        createCard()
        #    elif continue:
        #        continue

        #for every card in chosen deck loop:
        #    nextCard()
        
        #scorescreen()
        #    pass
            break

if __name__ == '__main__':
    #inter = GraphicsInterface()
    #app = FlashStudyApp(self)
    #app.run()
    app = FlashStudyApp()
    app.play()