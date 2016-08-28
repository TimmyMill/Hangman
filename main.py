from game import Game
from words import Words

words = Words()


def main():
    new_game()


def new_game():
    words.select_word()
    words.print_word()
    
    # create a game object
    game = Game()



main()
