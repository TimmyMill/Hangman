from player import Player
from words import Words


class Game:

    def __init__(self):
        self.player = Player('')
        self.words = Words()
        self.word = ''
        self.new_player = True

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

        # changes our player's name to that which was entered by the user
        self.player.name = name

    # starts the game by selecting a word
    def start_game(self):
        self.word = self.words.select_word()
        self.words.print_word()

    # calls the player_guess and evaluate_guess methods for each turn
    def player_turn(self):
        self.player.player_guess()
        self.evaluate_guess()

    # checks whether the letter that the player guessed is in the selected word
    def evaluate_guess(self):
        guess = self.player.guess_list[0]

        if self.word.__contains__(guess):  # if the letter guessed is in the word, this happens
            print("You're correct")

        # otherwise the player's guess count decreases by 1
        else:
            print("I'm sorry, there are no " + guess + "'s")
            # print("You guessed " + guess)
            self.player.guess_count -= 1
            print(self.player.guess_count)

    def run_game(self):
        self.start_game()

        while True:

            if self.player.guess_count == 0:
                self.game_over()
                break

            else:
                self.player_turn()

    def game_over(self):
        print("I'm sorry, it looks like you're all out of guesses")
        response = input("Would you like to play again? (y/n)\n").capitalize()  # capitalize to make validation easier

        # error validation
        # while response != 'Y' or response != 'N':
        while True:

            # if the user doesn't enter "y" or "n", this will loop until they do
            if response == 'Y':
                self.reload()  # method call to reset the game
                break

            elif response == 'N':
                print("Thanks for playing!")
                break

            else:
                response = input("Would you like to play again? (y/n)\n").capitalize()

    # resets the game if the user would like to play again
    def reload(self):
        self.player.guess_count = 7  # resets guess count
        del self.words.wordlist[0]   # removes the word that was just used
        self.run_game()
