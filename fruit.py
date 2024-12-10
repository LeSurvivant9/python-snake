import random

import pygame.sprite

from colors import Colors


class Fruit(pygame.sprite.Sprite):
    def __init__(self, width: int, sprite_group: pygame.sprite.Group) -> None:
        super().__init__(sprite_group)
        self.width: int = width
        self.image: pygame.Surface = pygame.Surface((self.width, self.width))
        self.image.fill(Colors.RED)
        pygame.draw.rect(self.image, Colors.BLACK, self.image.get_rect(), 1)
        self.position: dict[str, int] = {'x': 0, 'y': 0}
        self.rect: pygame.Rect = self.image.get_rect(topleft=(self.position['x'], self.position['y']))
        self.position_update()

    def position_update(self) -> None:
        screen_rect: pygame.Rect = pygame.display.get_surface().get_rect()
        self.position['x'] = random.randint(0, (screen_rect.width // self.width) - 1) * self.width
        self.position['y'] = random.randint(0, (screen_rect.height // self.width) - 1) * self.width
        self.rect.topleft = (self.position['x'], self.position['y'])
