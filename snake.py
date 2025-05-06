from game_object import GameObject
from settings import *
import pygame

class Snake(GameObject):
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (CELL_SIZE, 0)
        self.grow_snake = False

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body.insert(0, new_head)
        if not self.grow_snake:
            self.body.pop()
        else:
            self.grow_snake = False

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def draw(self, surface):
        for i, segment in enumerate(self.body):
            x, y = segment
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            if i == 0:
                pygame.draw.rect(surface, (180, 0, 255), rect, border_radius=6)
                eye_radius = 2
                dx, dy = self.direction
                if dx > 0:
                    eye1 = (x + CELL_SIZE - 6, y + 5)
                    eye2 = (x + CELL_SIZE - 6, y + CELL_SIZE - 6)
                    tongue = (x + CELL_SIZE, y + CELL_SIZE // 2 - 2, 4, 4)
                elif dx < 0:
                    eye1 = (x + 5, y + 5)
                    eye2 = (x + 5, y + CELL_SIZE - 6)
                    tongue = (x - 4, y + CELL_SIZE // 2 - 2, 4, 4)
                elif dy > 0:
                    eye1 = (x + 5, y + CELL_SIZE - 6)
                    eye2 = (x + CELL_SIZE - 6, y + CELL_SIZE - 6)
                    tongue = (x + CELL_SIZE // 2 - 2, y + CELL_SIZE, 4, 4)
                else:
                    eye1 = (x + 5, y + 5)
                    eye2 = (x + CELL_SIZE - 6, y + 5)
                    tongue = (x + CELL_SIZE // 2 - 2, y - 4, 4, 4)
                pygame.draw.circle(surface, (255, 255, 255), eye1, eye_radius)
                pygame.draw.circle(surface, (255, 255, 255), eye2, eye_radius)
                pygame.draw.rect(surface, (255, 0, 0), tongue)
            else:
                pygame.draw.rect(surface, (130, 0, 200), rect, border_radius=4)

    def grow(self):
        self.grow_snake = True

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:]

    def check_bounds(self):
        x, y = self.body[0]
        return x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT