import pgzrun, pygame
from blackjack import Card, Deck, Player

WIDTH=800
HEIGHT=600
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2
CENTER = (CENTER_X,CENTER_Y)
BOTTOM_CENTER=(CENTER_X,HEIGHT-50)


#flags
clicked_play = False


two_of_clubs = Actor('2_of_clubs_small', pos=(CENTER_X,CENTER_Y))
play_button = Actor('play_button_small', pos=(CENTER_X+100,CENTER_Y))





def draw():
    screen.clear()
    screen.fill('dark green')
    two_of_clubs.draw()
    play_button.draw()
    # screen.draw.text('Welcome to The Black Jack Table!', fontsize=60, center=BOTTOM_CENTER, color='black')
    screen.draw.text('Click the play button. ',pos=(0,0))

def on_mouse_down(pos):
    if play_button.collidepoint(pos):
        print('true')



pgzrun.go()