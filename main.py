from game import Game


def main():
    new_game()


def new_game():
    # create a game object
    game = Game()

    if game.new_player:
        game.get_player_name()

    game.run_game()


main()
