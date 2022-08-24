import random
from blackjack import Card, Deck, Player
"""
Project No. BlackJack ( oop)

"""

#global vars
counter = 0
#flags
game_over = False
draw_two = True
both_hit = True
dealer_stay = False
player_stay = False
#initiate
deck = Deck()
deck.build()
deck.shuffle()
dealer = Player(True,'Dealer',deck)
player = Player(False, 'Player', deck)



def final_standings():
    print('----------------------')
    if dealer.total > player.total:
        print('Dealer wins')
    elif player.total > dealer.total:
        print('Player wins')
    elif player.total == dealer.total:
        print('Tie')
    print('----------------------')

def main():
    global game_over, draw_two, both_hit, dealer_stay, player_stay, counter
    while not game_over:
        while draw_two:
            dealer.first_two_draw()
            player.first_two_draw()
            dealer.show_Hand()
            player.show_Hand()
            draw_two = False

        while both_hit:
            dealer_turn = dealer.hit_or_stand()
            player_turn = player.hit_or_stand()

            if dealer_turn == 'h':
                dealer.show_Hand()
            elif dealer_turn == 's':
                counter+=1
                dealer_stay=True

            if player_turn == 'h':
                player.show_Hand()
            elif player_turn == 's':
                counter+=1
                player_stay=True

            if counter == 2: #both players are staying
                both_hit = False
                game_over = True
    final_standings()

main()

















