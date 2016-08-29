class Player:

    def __init__(self, name):
        self.name = name
        self.guess_count = 7
        self.guess_list = []

    def player_guess(self):
        guess = input("Please guess a letter\n")

        # error validation
        while True:
            # if the player guesses a single letter, it is added to the player's guess list
            if guess.isalpha() and len(guess) == 1:
                self.guess_list.insert(0, guess)
                break

            else:  # otherwise it loops and prompts them again
                print("Please try again")
                guess = input("Please guess a letter\n")
