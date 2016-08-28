class Player:

    def __init__(self, name):
        self.name = name
        self.guess_count = 7
        self.guess_list = []

    def player_guess(self):
        guess = input("Please guess a letter\n")

        while True:
            if guess.isalpha() and len(guess) == 1:
                self.guess_list.insert(0, guess)
                break
            else:
                print("Please try again")
                guess = input("Please guess a letter\n")
