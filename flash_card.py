
class FlashCard:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def play(self):
        create_deck = input("Do you want to create a new deck of flash cards ('y', 'n'): ").lower()

        while create_deck not in ["y", "n"]: create_deck = input("Try again! \
                                                                 Do you want to create a new deck of flash cards ('y', 'n'): ").lower()
            
        if create_deck == "y": self.deck.newDeck()

        if create_deck == "n":
            self.deck.existingDeck()
            modify_deck = input("Do you want to create, delete, add, modify, or move on to the next card? ").lower()

            if modify_deck == "add": self.deck.add()
            elif modify_deck == "create": self.deck.create()
            elif modify_deck == "modify": self.deck.modify()
            elif modify_deck == "next": self.deck.next()

        self.deck.score()