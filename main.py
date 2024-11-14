from game import Game


def main() -> None:
    game: Game = Game(SCREEN_WIDTH)
    game.run()

if __name__ == '__main__':
    SCREEN_WIDTH: int = 900
    main()
