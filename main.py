from player import Player
from words import Words

words = Words()


def main():
    new_game()


def new_game():
    words.select_word()
    words.print_word()
    player = Player(get_player())


def get_player():
    print("Welcome to Hangman!\n")

    name = input("Please enter your player name\n")

    # error validation
    while True:

        if name.isalpha():
            break

        else:
            print("I'm sorry, I didn't catch that.\n")
            name = input("Please enter your player name using only letters\n")

    return name

main()
