import pygame
import random
from settings import *

class Apple:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        return (x, y)

    def draw(self, surface):
        x, y = self.position
        center = (x + CELL_SIZE // 2, y + CELL_SIZE // 2)
        radius = CELL_SIZE // 2 - 2

        # Obuolys
        pygame.draw.circle(surface, (255, 50, 50), center, radius)

        # Lapelis
        leaf_width = 4
        leaf_height = 6
        leaf_x = x + CELL_SIZE // 2 - 2
        leaf_y = y - 3
        pygame.draw.ellipse(surface, (0, 200, 0), (leaf_x, leaf_y, leaf_width, leaf_height))
