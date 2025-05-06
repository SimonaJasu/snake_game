import pygame
from snake import Snake
from apple import Apple
from settings import *

class Game:
    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Game, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()
        self.score = 0
        self.font = pygame.font.SysFont('Arial', 25)

    def handle_input(self, event):
        if event.key == pygame.K_UP:
            self.snake.change_direction((0, -CELL_SIZE))
        elif event.key == pygame.K_DOWN:
            self.snake.change_direction((0, CELL_SIZE))
        elif event.key == pygame.K_LEFT:
            self.snake.change_direction((-CELL_SIZE, 0))
        elif event.key == pygame.K_RIGHT:
            self.snake.change_direction((CELL_SIZE, 0))

    def update(self):
        self.snake.move()
        if self.snake.body[0] == self.apple.position:
            self.snake.grow()
            self.apple = Apple()
            self.score += 1

    def draw(self, surface, player_name, best_score):
        surface.fill((34, 139, 34))  # Background color
        for obj in [self.snake, self.apple]:
            obj.draw(surface)
        self.draw_score(surface, player_name, best_score)

    def draw_score(self, surface, player_name, best_score):
        score_text = self.font.render(f"{player_name}'s Score: {self.score}  |  Best: {best_score}", True, (255, 255, 255))
        surface.blit(score_text, (10, 10))

    def draw_game_over(self, surface, font, player_name, best_score, top_scores):
        surface.fill((0, 0, 0))
        title = font.render("Game Over! Press R to Restart", True, (255, 255, 255))
        surface.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 2 - 90))

        score_font = pygame.font.SysFont('Arial', 24)
        score_text = score_font.render(f"{player_name}'s Score: {self.score}  |  Best: {best_score}", True, (200, 200, 200))
        surface.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 - 40))

        top_title = score_font.render("Top 3 players:", True, (255, 255, 255))
        surface.blit(top_title, (SCREEN_WIDTH // 2 - top_title.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

        for i, (name, score) in enumerate(top_scores):
            entry = score_font.render(f"{i+1}. {name}: {score}", True, (180, 180, 180))
            surface.blit(entry, (SCREEN_WIDTH // 2 - entry.get_width() // 2, SCREEN_HEIGHT // 2 + 40 + i * 30))

    def is_game_over(self):
        return self.snake.check_collision() or self.snake.check_bounds()

    def current_speed(self):
        level = self.score // 5
        return min(12 + level * 2, 30)