WALLET = 0

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        self.blackjack = False
        self.bust = False
        self.wallet = WALLET