# SSF100 Python Lab 8a

# Advanced Lab

# Create a deck of cards, shuffle deck, and then deal a single hand of 5 cards.
# Note use of tuples, lists, and dicts to create a hand.
# Play a game between user and computer.

import random

# Variables with groups of tuples)
cardfaces = ("A","K","Q","J","10","9","8","7","6","5","4","3","2")
cardsuits = ("H","S","D","C")

# define function init.
def init():
    # this deck created into a List.
    thisdeck = []
    # For 1 particular suit inside "cardsuits" Tuple:
    for suit in cardsuits:
        # for 1 particular face card inside "cardfaces" Tuple
        for face in cardfaces:
            # add a face and suit card to "thisdeck" with 2 columns.
            thisdeck.append(face+suit)
    return thisdeck

# define shuffle function to involve mycards.
def shuffle(mycards):
    unshuffled = mycards
    # create shuffled list.
    shuffled = []

    for count in range (0,len(unshuffled)):
        pick = ''
        while (pick == ''):
            pick = random.choice(unshuffled)
            shuffled.append(pick)
            unshuffled.remove(pick)
    return shuffled


if __name__ == '__main__':
    hand = {}
    cards = init()
    cards = shuffle(cards)
    count = 0
    for deal in range(0,5):
        hand["card" + str(deal)] = cards[deal]
        count += 1
print (hand)
