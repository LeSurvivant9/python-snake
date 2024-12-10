import pygame

from colors import Colors


class Snake(pygame.sprite.Sprite):
    def __init__(self, width: int, sprite_group: pygame.sprite.Group) -> None:
        super().__init__(sprite_group)
        self.width: int = width
        self.speed: int = 175
        self.direction: str = "right"
        self.move_timer: float = 0

        self.body: list[pygame.sprite.Sprite] = []
        for i in range(3):
            segment = pygame.sprite.Sprite(sprite_group)
            segment.image = pygame.Surface((self.width, self.width))
            segment.image.fill(Colors.DARK_GREEN)
            pygame.draw.rect(segment.image, Colors.BLACK, segment.image.get_rect(), 1)
            segment.rect = segment.image.get_rect(topleft=(self.width * (2 - i), 0))
            self.body.append(segment)
        self.body[0].image.fill(Colors.LIGHT_GREEN)
        pygame.draw.rect(self.body[0].image, Colors.BLACK, self.body[0].image.get_rect(), 1)

        self.image: pygame.Surface = self.body[0].image
        self.rect: pygame.Rect = self.body[0].rect
        self.position: pygame.Vector2 = pygame.Vector2(self.rect.topleft)

    def update(self, dt: float) -> None:
        self.detect_direction_keys()

        self.move_timer += dt
        movement_delay = self.width / self.speed
        if self.move_timer >= movement_delay:
            self.move_timer -= movement_delay
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i].rect.topleft = self.body[i - 1].rect.topleft
            self.position.x += ((self.direction == "right") - (self.direction == "left")) * self.width
            self.position.y += ((self.direction == "down") - (self.direction == "up")) * self.width
            self.body[0].rect.topleft = (round(self.position.x), round(self.position.y))

    def detect_direction_keys(self) -> None:
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

    def detect_head_collision(self, rect: pygame.Rect) -> bool:
        return self.rect.colliderect(rect)

    def detect_body_collision(self, rect: pygame.Rect) -> bool:
        return any(segment.rect.colliderect(rect) for segment in self.body[1:])
