import pygame

from colors import Colors


class Snake(pygame.sprite.Sprite):
    def __init__(self, width: int, sprite_group: pygame.sprite.Group) -> None:
        super().__init__(sprite_group)
        self.width: int = width
        self.speed: int = self.width // 2
        self.direction: str = "right"
        self.move_timer: float = 0
        self.move_delay: float = 0.1

        self.body: list[pygame.sprite.Sprite] = []
        for i in range(3):
            segment = pygame.sprite.Sprite(sprite_group)
            segment.image = pygame.Surface((self.width, self.width))
            segment.image.fill(Colors.DARK_GREEN)
            pygame.draw.rect(segment.image, Colors.BLACK, segment.image.get_rect(), 1)
            segment.rect = segment.image.get_rect(topleft=(self.width * i, 0))
            self.body.append(segment)
        self.body[0].image.fill(Colors.LIGHT_GREEN)
        pygame.draw.rect(self.body[0].image, Colors.BLACK, self.body[0].image.get_rect(), 1)

        self.image: pygame.Surface = self.body[0].image
        self.rect: pygame.Rect = self.body[0].rect

    def update(self, screen_rect: pygame.Rect, dt: float) -> None:
        self.move_timer += dt
        self.movement()
        if self.move_timer >= self.move_delay:
            self.move_timer = 0
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i].rect.topleft = self.body[i - 1].rect.topleft
            self.body[0].rect.x += ((self.direction == "right") - (self.direction == "left")) * self.width
            self.body[0].rect.y += ((self.direction == "down") - (self.direction == "up")) * self.width

    def movement(self) -> None:
        """
        This method is responsible for changing the direction of the snake.
        :return:
        """
        keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.direction != "down":
            self.direction = "up"
        elif keys[pygame.K_DOWN] and self.direction != "up":
            self.direction = "down"
        elif keys[pygame.K_LEFT] and self.direction != "right":
            self.direction = "left"
        elif keys[pygame.K_RIGHT] and self.direction != "left":
            self.direction = "right"

    def detect_collision(self, rect: pygame.Rect) -> bool:
        return self.rect.colliderect(rect)
