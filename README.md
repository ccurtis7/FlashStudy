# FlashStudy
A **flash card** app used to help students study

# To-Do List
* Brainstorm session
* Figure out the template for the flashcards
* Build user interface
* Outline algorithm with pseudocode

# Pseudocode
import random

class Deck:
    def __init__():
        run deck stuff

    def createCard():
        question = ""
        answer = "" 
        create empty dictionary

        ask the user for a question
        ask the user for answer

        save and return card dictionary

    def newDeck():
        ask user for new deck name
        create txt file
        save and return deck
    
    def existingDeck():
        ask user to choose an existing deck file
        return deck.file

    def modifyCard():
        lets user modify the card dictionary

    def deleteCard():
        delete chosen card dictionary

    def nextCard():
        go through all the cards

    def scoreScreen(): 
        counter for times completed deck
        if user input == main screen:
            start game all over
            exit to main screen
        elif user input == go through same deck again:
            start chosen deck for loop again
        else:
            close game


class FlashStudyApp:
    def __init__():
        deck.shuffle()

    def play():
        ask user to create a new deck or choose an existing deck
        if user input == newDeck:
            newDeck()
            make cards until user is done loop:
                createCard()
        elif user input == existingDeck:
            existingDeck()
            ask user if they want to modify, delete, add card, or continue
            if modify:
                modifyCard()
            elif delete:
                deleteCard()
            elif add:
                createCard()
            elif continue:
                continue

        for every card in chosen deck loop:
            nextCard()
        
        scorescreen()

