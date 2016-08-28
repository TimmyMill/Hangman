from player import Player


class Game:

    def __init__(self):
        self.player = Player('')

    def player_guess(self):
        guess = input("Please guess a letter\n")

        while True:
            if guess.isalpha() and len(guess) == 1:
                self.player.guess_list.insert(0, guess)
                break
            else:
                print("Please try again")
                guess = input("Please guess a letter\n")
