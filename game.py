from player import Player
from words import Words


class Game:

    def __init__(self):
        self.player = Player('')
        self.words = Words()

    # prompts the user to enter a name for their player
    def get_player_name(self):
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

        # change our player's name to that which was entered by the user
        self.player.name = name
