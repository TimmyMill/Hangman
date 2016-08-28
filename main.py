from game import Game
from words import Words

words = Words()


def main():
    new_game()


def new_game():
    words.select_word()
    words.print_word()
    player = get_player()
    game = Game()
    game.player.name = player
    game.player_guess()


def get_player():
    print("Welcome to Hangman!\n")

    name = input("Please enter your player name\n")

    # error validation
    # if the user enters a player name that doesn't contain only letters, they will be prompted to try again
    while True:

        if name.isalpha():
            break

        else:
            print("I'm sorry, I didn't catch that.\n")
            name = input("Please enter your player name using only letters\n")

    return name

main()
