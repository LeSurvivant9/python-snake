from game import Game


def main() -> None:
    game: Game = Game(CELL_WIDTH, CELLS_NUMBER)
    game.run()


if __name__ == '__main__':
    CELL_WIDTH: int = 30
    CELLS_NUMBER: int = 20
    main()
