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
