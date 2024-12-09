import pygame

from colors import Colors
from fruit import Fruit
from snake import Snake


class Game:
    def __init__(self, screen_width: int) -> None:
        self.all_sprites: pygame.sprite.Group = pygame.sprite.Group()
        self.screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_width))
        self.screen_rect: pygame.Rect = self.screen.get_rect()
        self.is_running: bool = True
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.FPS: int = 60
        self.dt: float = self.clock.tick(self.FPS) / 1000
        self.cell_width: int = screen_width // 40
        self.fruit: Fruit = Fruit(width=self.cell_width, sprite_group=self.all_sprites)
        self.snake: Snake = Snake(width=self.cell_width, sprite_group=self.all_sprites)

    def update(self) -> None:
        self.screen.fill(Colors.DARK_BLUE)
        self.all_sprites.update(self.screen_rect, self.dt)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def detect_event(self):
        if self.snake.detect_collision(self.fruit.rect):
            self.fruit.position_update(self.screen_rect)
            segment = pygame.sprite.Sprite(self.all_sprites)
            segment.image = pygame.Surface((self.cell_width, self.cell_width))
            segment.image.fill(Colors.DARK_GREEN)
            pygame.draw.rect(segment.image, Colors.BLACK, segment.image.get_rect(), 1)
            segment.rect = segment.image.get_rect(topleft=self.snake.body[-1].rect.topleft)
            self.snake.body.append(segment)
        if self.is_game_over:
            # self.is_running = False
            print("Game Over!")

    @property
    def is_game_over(self) -> bool:
        if self.snake.rect.top < self.screen_rect.top:
            return True
        if self.snake.rect.bottom > self.screen_rect.bottom:
            print(self.snake.rect.bottom, self.screen_rect.bottom)
            return True
        if self.snake.rect.left < self.screen_rect.left:
            return True
        if self.snake.rect.right > self.screen_rect.right:
            return True
        return False

    def run(self) -> None:
        pygame.init()

        while self.is_running:
            self.dt = self.clock.tick(self.FPS) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.is_running = False
            self.detect_event()
            self.update()

        pygame.quit()
