import pgzrun, pygame
from blackjack import Card, Deck, Player

#constants
WIDTH=1280
HEIGHT=720
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2
CENTER = (CENTER_X,CENTER_Y)
BOTTOM_CENTER=(CENTER_X,HEIGHT-50)


#flags
clicked_play = False
draw_two = True
both_hit = True
dealer_stay = False
player_stay = False
#global vars
counter = 0

#initiate
deck = Deck()
deck.build()
deck.shuffle()
dealer = Player(True,'Dealer',deck)
player = Player(False, 'Player', deck)


two_of_clubs = Actor('2_of_clubs_small', pos=(CENTER_X,CENTER_Y))
two_of_diamonds = Actor('2_of_diamonds_small',pos=CENTER)
two_of_hearts = Actor('2_of_hearts_small',pos=CENTER)
two_of_spades = Actor('2_of_spades_small',pos=CENTER)
three_of_clubs = Actor('2_of_clubs_small',pos=CENTER)
three_of_diamonds = Actor('2_of_diamonds_small',pos=CENTER)
three_of_hearts = Actor('2_of_hearts_small',pos=CENTER)
three_of_spades = Actor('2_of_spades_small',pos=CENTER)
four_of_clubs = Actor('4_of_clubs_small',pos=CENTER)
four_of_diamonds = Actor('4_of_diamonds_small',pos=CENTER)
four_of_hearts = Actor('4_of_hearts_small',pos=CENTER)
four_of_spades = Actor('4_of_spades_small',pos=CENTER)
five_of_clubs = Actor('5_of_clubs_small',pos=CENTER)
five_of_diamonds = Actor('5_of_diamonds_small',pos=CENTER)
five_of_hearts = Actor('5_of_hearts_small',pos=CENTER)
five_of_spades = Actor('5_of_spades_small',pos=CENTER)
six_of_clubs = Actor('6_of_clubs_small',pos=CENTER)
six_of_diamonds = Actor('6_of_diamonds_small',pos=CENTER)
six_of_hearts = Actor('6_of_hearts_small',pos=CENTER)
six_of_spades = Actor('6_of_spades_small',pos=CENTER)
seven_of_clubs = Actor('7_of_clubs_small',pos=CENTER)
seven_of_diamonds = Actor('7_of_diamonds_small',pos=CENTER)
seven_of_hearts = Actor('7_of_hearts_small',pos=CENTER)
seven_of_spades = Actor('7_of_spades_small',pos=CENTER)
eight_of_clubs = Actor('8_of_clubs_small',pos=CENTER)
eight_of_diamonds = Actor('8_of_diamonds_small',pos=CENTER)
eight_of_hearts = Actor('8_of_hearts_small',pos=CENTER)
eight_of_spades = Actor('8_of_spades_small',pos=CENTER)
nine_of_clubs = Actor('9_of_clubs_small',pos=CENTER)
nine_of_diamonds = Actor('9_of_diamonds_small',pos=CENTER)
nine_of_hearts = Actor('9_of_hearts_small',pos=CENTER)
nine_of_spades = Actor('9_of_spades_small',pos=CENTER)

play_button = Actor('play_button_small', pos=(CENTER_X,CENTER_Y+100))





def draw():
    screen.clear()
    screen.fill('dark green')
    ·two_of_hearts.draw()
    if clicked_play == False:
        play_button.draw()
        screen.draw.text('Welcome to The Black Jack Table!', fontsize=60, center=BOTTOM_CENTER, color='black')
        screen.draw.text('Click the play button. ',center=(CENTER_X,CENTER_Y),)
    elif clicked_play == True:
        print('meow')

def on_mouse_down(pos):
    global clicked_play
    if play_button.collidepoint(pos):
        clicked_play=True

def update():
    pass


pgzrun.go()