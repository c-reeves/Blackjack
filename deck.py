from random import shuffle

SUIT = [11,10,10,10,10,9,8,7,6,5,4,3,2]
DECK = SUIT * 4
DECK_COUNT = 1

class Deck():

    def __init__(self):
        self.cards = DECK * DECK_COUNT
        self.card_count = len(self.cards)
        self.deck_left = len(self.cards)
        self.percent_left = self.deck_left / self.card_count
        self.shuffle()
    

    def shuffle(self):
        shuffle(self.cards)


    def card(self):
        new_card = self.cards.pop()
        self.deck_left -= 1
        self.percent_left = self.deck_left / self.card_count
        return new_card


    def reset(self):
        self.cards = DECK * DECK_COUNT
        self.deck_left = len(self.cards)
        self.percent_left = self.deck_left / self.card_count
        self.shuffle()