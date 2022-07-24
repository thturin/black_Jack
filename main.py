import random
from blackjack import Card, Deck
"""
Project No. BlackJack (non oop)

"""


#global vars
dealer_cards = []
player_cards = []
deck_dict = {'A': [1,11], '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,"Q":10,'K':10}
deck = []


#flags
game_over = False

card = Card('hearts','A')

deck = Deck()
deck.build()
#deck.show()

print(deck.cards[0].show)
#print(deck.cards[10].value)