from player import Player
from deck import Deck
from strategy import hit_dict, bet_dict

DECK_RESHUFFLE = 0.3
bet = 1

class Table():
    def __init__(self):
        self.dealer = Player('dealer')
        self.player1 = Player('p1')
        self.deck = Deck()
        self.bet = bet


    def deal(self, player):
        if self.deck.percent_left < DECK_RESHUFFLE:
            self.deck.reset()
        player.hand = []
        player.blackjack = False
        player.bust = False
        self.game_on = True
        self.results = ''
        self.bet = bet
        for _ in range(2):
            player.hand.append(self.deck.card())
        self.score(player)
        self.bet = bet_dict.get(player.score) * self.bet
        if player.score == 21:
            player.blackjack = True


    def play_out(self, player):
        while hit_dict.get(player.score):
            player.hand.append(self.deck.card())
            self.score(player)


    def score(self, player):
        player.score = 0
        for card in player.hand:
            player.score += card
        if player.score > 21 and 11 in player.hand:
            player.score -= 10
        elif player.score > 21:
            player.bust = True


    def evaluate(self, dealer, player1):
        if dealer.blackjack and player1.blackjack:
            self.results = 'Draw'
        elif dealer.blackjack:
            self.results = 'Dealer BJ'
            player1.wallet -= self.bet
        elif player1.blackjack:
            self.results = 'Player BJ'
            player1.wallet += self.bet * 1.5
        elif player1.bust:
            self.results = 'Dealer Win'
            player1.wallet -= self.bet
        elif dealer.bust:
            self.results = 'Player Win'
            player1.wallet += self.bet
        elif dealer.score == player1.score:
            self.results = 'Draw'
        elif dealer.score < player1.score:
            self.results = 'Player Win'
            player1.wallet += self.bet
        else:
            self.results = 'Dealer Win'
            player1.wallet -= self.bet