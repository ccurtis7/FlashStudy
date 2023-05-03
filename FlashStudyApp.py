import random

class Deck:
    def __init__(self, filename):
        #run deck stuff
        if filename == '':
            print('Creating empty deck.')
            self.cards = {}
        elif '.txt' in filename:
            self.cards = {}
            infile = open(filename, 'r')
            for line in infile.readlines():
                contents = line.replace('\n', '')
                contents = contents.split(',')
                self.cards[contents[0]] = contents[1]
            infile.close()
        else:
            raise ValueError('Invalid filename provided. Cannot create Deck.')

    def addCard(self, front, back):
        # Adds or modifies an existing card, identified by front.
        self.cards[front] = back

    def deleteCard(self, front):
        #delete chosen card dictionary
        del self.cards[front]

    def writeDeck(self, filename):
        outfile = open(filename, 'w')
        contents = ''
        for front, back in self.cards.items():
            contents += '{},{}\n'.format(front, back)
        print(contents, file=outfile)
        outfile.close()

    #def nextCard(self, front, back):
    #    for front, back in self.cards():
    #        if next.clicked():
    #            return front
    #        if turn.clicked():
    #            return back

class FlashStudyApp:
    def __init__(self):
        self.deck = Deck()
        filename = ''
        self.deck()
        #self.outFile =  ""
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
