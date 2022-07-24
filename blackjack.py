class Card:
    def __init__(self,suit,val):
        self.suit=suit
        self.value =val

    def show(self):
        print('{} of {}'.format(self.value,self.suit))

    def get_value(self):
        dict = {
            'A':[1,11], '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
            '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10
        }

        print(dict)




class Deck:
    def __init__(self):
        self.cards = []

    def build(self):
        for suit in ["♠","♣","♥","♦"]:
           for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
               self.cards.append(Card(suit,value))

    def show(self):
        for card in self.cards:
            card.show()