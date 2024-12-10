import pygame

from colors import Colors


class Header:
    def __init__(self, screen: pygame.Surface, height: int) -> None:
        pygame.init()
        self.screen: pygame.Surface = screen
        self.width: int = screen.get_width()
        self.height: int = height
        self.box_surface: pygame.Surface = pygame.Surface((self.width, self.height))
        self.box_surface.fill(Colors.BLACK)
        self.font: pygame.Font = pygame.font.Font(None, 36)
        self.informations: dict[str, dict[str, str | tuple[int, int]]] = {}

    def add_text(self, key: str, content: str, x_position: int) -> None:
        text_surface: pygame.Surface = self.font.render(content, True, Colors.WHITE)
        _, text_height = text_surface.get_size()
        centered_position = (x_position, self.height // 2 - text_height // 2)
        self.informations[key] = {"content": content, "position": centered_position}

    def update_text(self, key: str, content: str) -> None:
        if key in self.informations:
            self.informations[key]["content"] = content

    def draw(self) -> None:
        self.box_surface.fill(Colors.BLACK)
        for info in self.informations.values():
            text_surface: pygame.Surface = self.font.render(info["content"], True, Colors.WHITE)
            self.box_surface.blit(text_surface, info["position"])
        self.screen.blit(self.box_surface, (0, 0))
