import random

class Card:
    def __init__(self,suit,val):
        self.suit=suit
        self.value =val

    def show(self):
        print('{} of {}'.format(self.value,self.suit),end='')


    def get_value(self):
        dict = {
            'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
            '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10
        }
        return dict[self.value]



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

    def shuffle(self): #shuffle the cards
        #Fishe-Yates shuffle algorithm
        for i in range(len(self.cards)-1,0,-1): # for int i=len(card)-1 i>0 i--
            #pick a random index from 0 to i
            rand_int = random.randint(0,i+1)
            #swap with current i
            self.cards[i],self.cards[rand_int]=self.cards[rand_int],self.cards[i]

    def draw(self): #draw the cards
        return self.cards.pop() #return the top card of the deck

    #the maximum number of cards you can hold in a hand without busting is 11: 4 aces, 4 2's and 3 3's






class Player:
    def __init__(self, isDealer, name, deck):
        self.isDealer = isDealer
        self.name = name
        self.deck = deck
        self.total = 0
        self.hand = []


    def show_Hand(self):
        if self.isDealer:
            print('Dealer is dealt a ', end='')
            self.hand[0].show()
            print(' and a ', end='')
            self.hand[1].show()
        else:
            print('Player is dealt a ', end='')
            self.hand[0].show()
            print(' and a ', end='')
            self.hand[1].show()
        print()

    def handle_ace(self):
        if self.total + 11 < 21:
            return 11
        else:
            return 1

    def calculate_total(self):
        for card in self.hand:
            if card.value == 'A':
                self.total+=self.handle_ace()
            else:
                self.total+=card.get_value()
        print('{}s total is {}'.format(self.name, self.total))
        return self.total


    def dealer_check_total(self):
        pass


    def hit_or_stand(self):
        print('{}, would you like to hit or stand? Enter h or s'.format(self.name))
        response = input()
        if response == 'h':
            self.hand.append(self.deck.draw())
            return 'h'
        else:
            return 's'




