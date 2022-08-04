import random
from blackjack import Card, Deck, Player
"""
Project No. BlackJack ( oop)

"""


#global vars

#flags
game_over = False
draw_two = True

deck = Deck()
deck.build()
deck.shuffle()


dealer = Player(True,'Dealer',deck)
player = Player(False, 'Player', deck)

flag = True
dealer_stay = False
player_stay = False

#deal first two cards for player and dealer
# dealer.hand.append(deck.draw())
# dealer.hand.append(deck.draw())
# player.hand.append(deck.draw())
# player.hand.append(deck.draw())

# dealer.show_Hand()
# player.show_Hand()

counter = 0
while not game_over:
    while draw_two:
        for i in range(2):
            dealer.hand.append(deck.draw())
            player.hand.append(deck.draw())
        dealer.show_Hand()
        player.show_Hand()
        draw_two = False

    while flag:
        dealer_turn = dealer.hit_or_stand()
        player_turn = player.hit_or_stand()

        if dealer_stay == False:
            if dealer_turn == 'h':
                dealer.hand.append(deck.draw())
                dealer.calculate_total()
            elif dealer_turn == 's':
                counter+=1
                dealer_stay=True
        if player_turn == False:
            if player_turn == 'h':
                player.hand.append(deck.draw())
                player.calculate_total()
            elif player_turn == 's':
                counter+=1
                dealer_stay = True

        if counter == 2:
            game_over = True
            flag = False











    # dealer_total = dealer.calculate_total()
    # player_total = player.calculate_total()


    game_over = True






#player_next_card = Input('Player hit or stay? Enter h or t: ')



    #dealer draws

    #player draws


#create a draw method



#print(deck.cards[10].value)