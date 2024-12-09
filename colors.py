from dataclasses import dataclass


@dataclass
class Colors:
    BLACK: tuple[int, int, int] = (0, 0, 0)
    WHITE: tuple[int, int, int] = (255, 255, 255)
    RED: tuple[int, int, int] = (175, 0, 0)
    GREEN: tuple[int, int, int] = (0, 255, 0)
    DARK_GREEN: tuple[int, int, int] = (0, 128, 0)
    LIGHT_GREEN: tuple[int, int, int] = (144, 238, 144)
    BLUE: tuple[int, int, int] = (0, 0, 255)
    DARK_BLUE: tuple[int, int, int] = (0, 0, 128)
    LIGHT_BLUE: tuple[int, int, int] = (173, 216, 230)
    YELLOW: tuple[int, int, int] = (255, 255, 0)
