import time

import pygame

from colors import Colors
from fruit import Fruit
from header import Header
from snake import Snake


class Game:
    def __init__(self, cell_width: int, cells_number: int) -> None:
        screen_width: int = cell_width * cells_number
        pygame.display.set_caption("Snake")
        self.screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_width))
        self.screen_rect: pygame.Rect = self.screen.get_rect()
        self.header_height: int = 50
        self.header: Header = Header(screen=self.screen, height=self.header_height)
        self.game_width: int = screen_width - self.header_height
        self.game_surface: pygame.Surface = pygame.Surface((screen_width, self.game_width))
        self.game_surface_rect: pygame.Rect = self.game_surface.get_rect()
        self.cell_width: int = cell_width
        self.all_sprites: pygame.sprite.Group = pygame.sprite.Group()
        self.fruit: Fruit = Fruit(width=self.cell_width, sprite_group=self.all_sprites)
        self.snake: Snake = Snake(width=self.cell_width, sprite_group=self.all_sprites)

        self.is_running: bool = True
        self.pause: bool = False
        self.score: int = 0
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.FPS: int = 240
        self.last_fps_update_time: float = time.time()

        self.header.add_text("score", f"Score : {self.score}", 10)
        self.header.add_text("fps", f"FPS : {self.FPS}", screen_width // 2 - 125)

    def spawn_food(self):
        while self.snake.detect_body_collision(self.fruit.rect) or self.snake.detect_head_collision(self.fruit.rect):
            self.fruit.position_update(self.game_surface_rect)

    def update(self, dt: float) -> None:
        current_time = time.time()
        if current_time - self.last_fps_update_time >= 0.3:
            self.header.update_text("fps", f"FPS : {1 / dt:.0F}")
            self.last_fps_update_time = current_time
        self.header.draw()
        self.all_sprites.update(dt)
        self.game_surface.fill(Colors.DARK_BLUE)
        self.all_sprites.draw(self.game_surface)
        self.screen.blit(self.game_surface, (0, self.header_height))
        pygame.display.flip()

    def detect_event(self):
        if self.snake.detect_head_collision(self.fruit.rect):
            self.score += 1
            self.header.update_text("score", f"Score : {self.score}")
            self.spawn_food()
            segment = pygame.sprite.Sprite(self.all_sprites)
            segment.image = pygame.Surface((self.cell_width, self.cell_width))
            segment.image.fill(Colors.DARK_GREEN)
            pygame.draw.rect(segment.image, Colors.BLACK, segment.image.get_rect(), 1)
            segment.rect = segment.image.get_rect(topleft=self.snake.body[-1].rect.topleft)
            self.snake.body.append(segment)
        if self.is_game_over:
            self.pause = True
            print("Game Over!")

    @property
    def is_game_over(self) -> bool:
        if self.snake.rect.top < self.game_surface_rect.top:
            return True
        if self.snake.rect.bottom > self.game_surface_rect.bottom:
            return True
        if self.snake.rect.left < self.game_surface_rect.left:
            return True
        if self.snake.rect.right > self.game_surface_rect.right:
            return True
        if self.snake.detect_body_collision(self.snake.rect):
            return True
        return False

    def run(self) -> None:
        pygame.init()
        self.spawn_food()

        previous_time: float = time.time()
        while self.is_running:
            dt: float = time.time() - previous_time
            previous_time = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.is_running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.pause = not self.pause

            if not self.pause:
                self.detect_event()
                self.update(dt)

            self.clock.tick(self.FPS)

        pygame.quit()
