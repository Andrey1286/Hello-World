import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Класс игрока
class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 20, 20))

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed

# Функция для рисования стен
def draw_walls(screen):
    pygame.draw.rect(screen, BLACK, (0, 0, 640, 20), 0)
    pygame.draw.rect(screen, BLACK, (0, 460, 640, 20), 0)
    pygame.draw.rect(screen, BLACK, (0, 0, 20, 480), 0)
    pygame.draw.rect(screen, BLACK, (620, 0, 20, 480), 0)

# Основная функция игры
def game_loop():
    player = Player(320, 240, RED)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            player.move(1, 0)
        if keys[pygame.K_UP]:
            player.move(0, -1)
        if keys[pygame.K_DOWN]:
            player.move(0, 1)

        screen.fill(WHITE)
        draw_walls(screen)
        player.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

# Запуск игры
game_loop()
