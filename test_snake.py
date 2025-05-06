import unittest
from snake import Snake
from settings import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_initial_length(self):
        self.assertEqual(len(self.snake.body), 3)

    def test_move_forward(self):
        original_head = self.snake.body[0]
        self.snake.move()
        expected = (original_head[0] + CELL_SIZE, original_head[1])
        self.assertEqual(self.snake.body[0], expected)

    def test_grow(self):
        self.snake.grow()
        self.snake.move()
        self.assertEqual(len(self.snake.body), 4)

    def test_collision_with_self(self):
        self.snake.body = [(100, 100), (80, 100), (60, 100), (100, 100)]
        self.assertTrue(self.snake.check_collision())

    def test_bounds_check(self):
        self.snake.body[0] = (-20, 100)
        self.assertTrue(self.snake.check_bounds())
        self.snake.body[0] = (SCREEN_WIDTH + 1, 100)
        self.assertTrue(self.snake.check_bounds())
        self.snake.body[0] = (100, -20)
        self.assertTrue(self.snake.check_bounds())
        self.snake.body[0] = (100, SCREEN_HEIGHT + 1)
        self.assertTrue(self.snake.check_bounds())

if __name__ == '__main__':
    unittest.main()