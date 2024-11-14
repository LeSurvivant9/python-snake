import pygame

from colors import Colors
from fruit import Fruit


class Game(pygame.sprite.Sprite):
    def __init__(self, screen_width: int) -> None:
        super().__init__()
        self.all_sprites: pygame.sprite.Group = pygame.sprite.Group()
        self.screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_width))
        self.screen_rect: pygame.Rect = self.screen.get_rect()
        self.is_running: bool = True
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.FPS: int = 60
        self.dt: float = self.clock.tick(self.FPS) / 1000
        self.cell_width: int = screen_width // 40
        self.fruit: Fruit = Fruit(width=self.cell_width, sprite_group=self.all_sprites)

    def update(self) -> None:
        self.screen.fill(Colors.DARK_BLUE)
        self.all_sprites.update(self.screen_rect)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def run(self) -> None:
        pygame.init()

        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.is_running = False

            self.update()
            self.clock.tick(self.FPS)

        pygame.quit()
