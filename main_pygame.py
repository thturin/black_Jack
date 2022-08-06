import pgzrun, pygame
from blackjack import Card, Deck, Player

WIDTH=800
HEIGHT=600
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2




two_of_clubs = Actor('2_of_clubs_small', pos=(CENTER_X,CENTER_Y))
# pygame.transform.scale()
# two_of_clubs._surf = pygame.transform.scale(two_of_clubs._surf,(100,200))
# two_of_clubs._update_pos()

def draw():
    screen.fill('green')
    two_of_clubs.draw()

def update():
    pass



pgzrun.go()