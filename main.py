import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pygame
from settings import *
from game import Game
from registration import registration_screen
from file_io import load_scores, save_scores, get_top_scores

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 28)

player_name = registration_screen(screen, font)
scores = load_scores()
best_score = scores.get(player_name, 0)
game = Game()
running = True
game_active = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif game_active and event.type == pygame.KEYDOWN:
            game.handle_input(event)
        elif not game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            game = Game()
            game_active = True

    if game_active:
        game.update()
        if game.is_game_over():
            game_active = False
            if game.score > best_score:
                best_score = game.score
                scores[player_name] = best_score
                save_scores(scores)
        game.draw(screen, player_name, best_score)
    else:
        game.draw_game_over(screen, font, player_name, best_score, get_top_scores(scores))

    clock.tick(game.current_speed())
    pygame.display.update()

pygame.quit()